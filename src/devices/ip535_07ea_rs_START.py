#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS-“ПУСК”:
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalingDeviceIP53_507EA_Start(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS-“ПУСК”:
    (протокол Modbus RTU)
    Руководство по эксплуатации
    4371-006-43082497-04-04 РЭ, 2021 г.
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
    STATUS = {
        1: "Загрузка",
        2: "Тест",
        3: "Норма",
        4: "Требование квитирования",
        5: "Сработал",
        6: "Неисправность"
    }
    NAME = "ИП535-07еа-RS-ПУСК"
    SPEED_DEFAULT = SPEEDS_DEVICE[5][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[1][1]
    NUMS_STOP_BIT = 1
    SLAVE = 1

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
            ("Количество стоп битов", self.read_holding_registers(address=3, slave=slave).registers[0]),
            ("Идентификатор устройства", self.read_holding_registers(address=4, slave=slave).registers[0]),
            ("Версия устройства", self.read_holding_registers(address=6, slave=slave).registers[0]),
            ("Версия ПО устройства", self.read_holding_registers(address=7, slave=slave).registers[0]),
            ("Серийный номер", self.read_holding_registers(address=8, slave=slave).registers[0]),
            ("Состояние устройства", self.STATUS[
                self.read_holding_registers(address=10, slave=slave).registers[0]]),
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

    def clear_status(self):
        self.write_registers(address=12, values=4, slave=1)
        self.close()
