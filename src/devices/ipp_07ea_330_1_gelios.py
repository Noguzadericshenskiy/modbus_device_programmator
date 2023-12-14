# Извещатель пламени пожарный взрывозащищенный
# ИПП 07еа-330-1- Vrs "Гелиос-3 ИК" (Эридан)

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb
from pymodbus import bit_read_message, bit_write_message, register_write_message

class SignalingDeviceIPP_07_330_1(Client_mb):
    """
    Извещатель пламени пожарный взрывозащищенный
    ИПП 07еа-330-1- Vrs "Гелиос-3 ИК" (Эридан)
    (протокол Modbus RTU)

    """

    SPEEDS_DEVICE = (
        (1, 1200),
        (2, 2400),
        (3, 4800),
        (4, 9600),
        (5, 14400),
        (6, 19200),
        (7, 28800),
        (8, 38400),
        (9, 57600),
        (10, 115200)
    )

    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    STOP_BITS = ((1, "1"),
                 # (2, "1.5"),
                 (3, '2'))
    NAME = "ИПП-07еа-330-1(Гелиос-3 ИК)"
    SPEED_DEFAULT = SPEEDS_DEVICE[5][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[0][1]
    NUMS_STOP_BIT = 1
    SLAVE = 1

    STATUS = {
        1: "Загрузка",
        2: "Тест",
        3: "Норма",
        5: "Сработал",
        6: "Неисправность"
    }

    MODELS = {49: "Гелиос-3ИК RS", 50: "Гелиос-ИК/УФ RS"}

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
            timeout=0.05
        )

    def get_info(self, slave=SLAVE) -> tuple:
        params = (
            ("Адрес устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Скорость интерфейса", self.SPEEDS_DEVICE[
                self.read_holding_registers(address=1, slave=slave).registers[0] - 1][1]),
            ("Проверочный бит", self.VERIFICATION_BITS[
                self.read_holding_registers(address=2, slave=slave).registers[0] - 1][1]),
            ("Количество стоп битов", self.STOP_BITS[
                self.read_holding_registers(address=3, slave=slave).registers[0] - 1][1]),
            ("Идентификатор оборудования", self.read_holding_registers(address=4, slave=slave).registers[0]),
            ("Версия протокола связи", self.read_holding_registers(address=5, slave=slave).registers[0]),
            ("Версия устройства", self.read_holding_registers(address=6, slave=slave).registers[0]),
            ("Версия ПО устройства", self.read_holding_registers(address=7, slave=slave).registers[0]),
            ("Серийный номер", self.read_holding_registers(address=8, slave=slave).registers[0]),
            ("Состояние устройства", self.STATUS[
                self.read_holding_registers(address=10, slave=slave).registers[0]]),
            ("Регистр диагностики", self.read_holding_registers(address=11, slave=slave).registers[0]),
            ("Регистр конфигурации", self.read_holding_registers(address=50, slave=slave).registers[0]),
            ("Реистр чувствительности", self.read_holding_registers(address=51, slave=slave).registers[0]),
            ("Регистр ИК канала", self.read_holding_registers(address=52, slave=slave).registers[0]),
            ("Регистр УФ канала", self.read_holding_registers(address=53, slave=slave).registers[0]),
            ("Регистр модели ИПП", self.read_holding_registers(address=54, slave=slave).registers[0]),
        )
        self.close()
        return params

    def set_slave(self, new_slave: int, slave: int) -> None:
        self.write_register(0, new_slave, slave)
        self.close()

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        self.write_register(1, new_spd, slave)
        self.close()

    def set_parity(self, new_parity: int, slave: int) -> None:
        self.write_register(2, new_parity, slave)
        self.close()

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        self.write_register(3, new_stop_bit, slave)
        self.close()

