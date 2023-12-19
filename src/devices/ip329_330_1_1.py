#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный Феникс ИК УФ
# Феникс ИК/УФ (ИП 329/330-1-1)

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class FireDetektorFlameIP329_330_re(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный пламени ИП329-330-re
    (протокол Modbus RTU)
    Феникс ИК/УФ (ИП 329/330-1-1)
    """
    SPEEDS_DEVICE = (
        (1, 4800),
        (2, 9600),
        (4, 19200),
        (12, 57600),
        (24, 115200),
    )
    VERIFICATION_BITS = (1, "N")
    NAME = "ИП329/330-1-1 (Феникс)"
    SPEED_DEFAULT = SPEEDS_DEVICE[3][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[0]
    NUMS_STOP_BIT = 1
    SLAVE = 3

    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            parity=AV_VERIFICATION_BIT,
            stopbits=NUMS_STOP_BIT
    ):
        Client_mb.__init__(
            self,
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            parity=parity,
            framer=pymodbus.framer.ModbusRtuFramer,
        )

    def get_info(self, slave=SLAVE) -> tuple:
        status_data = [int(i) for i in bin(
            self.read_holding_registers(address=6, slave=slave).registers[0])[2:].zfill(16)]
        add_flags = [int(i) for i in bin(self.read_holding_registers(address=7, slave=slave).registers[0])[2:].zfill(16)]
        params = (
            ("Адрес устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Скорость", self.get_speed(int(self.read_holding_registers(address=1, slave=slave).registers[0]))),
            ("Серийный номер", self.read_holding_registers(address=2, slave=slave).registers[0]),
            ("DevType", self.read_holding_registers(address=3, slave=slave).registers[0]),
            ("DevHard", self.read_holding_registers(address=4, slave=slave).registers[0]),
            ("DevSoft", self.read_holding_registers(address=5, slave=slave).registers[0]),
            ("Пожар", "ВКЛ" if status_data[15] == 1 else "ВЫКЛ"),
            ("Предпожар", "ВКЛ" if status_data[14] == 1 else "ВЫКЛ"),
            ("Ошибка FAULT", "ВКЛ" if status_data[13] == 1 else "ВЫКЛ"),
            ("Авария BREAK", "ВКЛ" if status_data[12] == 1 else "ВЫКЛ"),
            ("Сработал ИК канал", "ВКЛ" if status_data[11] == 1 else "ВЫКЛ"),
            ("Сработал УФ канал", "ВКЛ" if status_data[10] == 1 else "ВЫКЛ"),
            ("Идет самотестирование", "ВКЛ" if status_data[9] == 1 else "ВЫКЛ"),
            ("Установлен магнит", "ВКЛ" if status_data[8] == 1 else "ВЫКЛ"),
            ("Включен тестовый режим", "ВКЛ" if status_data[7] == 1 else "ВЫКЛ"),
            ("Запыленность (с V1.14)", "ВКЛ" if status_data[6] == 1 else "ВЫКЛ"),
            ("Flash память исправна", "ВКЛ" if status_data[5] == 1 else "ВЫКЛ"),
            ("Память программ исправна", "ВКЛ" if status_data[4] == 1 else "ВЫКЛ"),
            ("Каналы ИК и УФ калиброваны", "ВКЛ" if status_data[3] == 1 else "ВЫКЛ"),
            ("Есть калибровка тестовых каналов", "ВКЛ" if status_data[2] == 1 else "ВЫКЛ"),
            ("Есть установка нуля тестовых каналов", "ВКЛ" if status_data[1] == 1 else "ВЫКЛ"),
            ("SD карта установлена", "ВКЛ" if status_data[0] == 1 else "ВЫКЛ"),
            ("Реле Пожар включено", "ВКЛ" if add_flags[15] == 1 else "ВЫКЛ"),
            ("Реле Исправность включено", "ВКЛ" if add_flags[14] == 1 else "ВЫКЛ"),
            ("Реле Запыленность включено", "ВКЛ" if add_flags[13] == 1 else "ВЫКЛ"),
            ("Мигающий LED", "ВКЛ" if add_flags[12] == 1 else "ВЫКЛ"),
            ("20 мА включено", "ВКЛ" if add_flags[11] == 1 else "ВЫКЛ"),
            ("Аварийная запыленность (чувствительность <50%)", "ВКЛ" if add_flags[4] == 1 else "ВЫКЛ"),
            ("Запыленность (чувствительность <70%)", "ВКЛ" if add_flags[3] == 1 else "ВЫКЛ"),
            ("Ошибка температуры", "ВКЛ" if add_flags[2] == 1 else "ВЫКЛ"),
            ("Ошибка питания УФ", "ВКЛ" if add_flags[1] == 1 else "ВЫКЛ"),
            ("Ошибка питания 24В", "ВКЛ" if add_flags[0] == 1 else "ВЫКЛ"),
        )
        print(status_data)
        print(add_flags)
        self.close()
        return params

    def set_slave(self, new_slave: int, slave: int) -> None:
        self.write_register(1, new_slave, slave)
        self.close()

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        self.write_register(2, new_spd, slave)
        self.close()

    def set_parity(self, new_parity: int, slave: int) -> None:
        self.close()

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        self.close()

    @classmethod
    def get_speed(self, spd: int) -> int:
        for i_speed in self.SPEEDS_DEVICE:
            if i_speed[0] == spd:
                return i_speed[1]
