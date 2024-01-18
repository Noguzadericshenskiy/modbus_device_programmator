"""
ИЗВЕЩАТЕЛЬ ПОЖАРНЫй РУЧНОЙ
ВЗРЫВОЗАЩИЩЁННЫЙ АДРЕСНЫЙ
ExИП535-1В-А
Руководство по эксплуатации
908.3065.00.000 РЭ
"""

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalDeviceEXIP535_1V_A(Client_mb):
    """
    Извещатель пожарный ручной взрывозащищенный адресный
    ExИП535-1В-А
    """

    NAME = "ИП101-07а-RS"
    SPEEDS_DEVICE = (
        (0, 9600),
        (1, 14400),
        # (2, 19200), #эта скорость заяввлена, но нет в таблице модбас
        (2, 38400),
        (3, 57600),
        (4, 115200)
    )
    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    STOP_BITS = ((1, "1"),
                 # (2, "1.5"),
                 (3, '2'))

    SLAVE = 1
    SPEED_DEFAULT = 9600
    PARITY = "N"
    NUMS_STOP_BIT = 1


    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            parity=PARITY,
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
            ("Адрес устройства", self.read_holding_registers(address=1, slave=slave).registers[0]),
            ("Скорость интерфейса", self.SPEEDS_DEVICE[
                self.read_holding_registers(address=4, slave=slave).registers[0]][1]),
            ("Проверочный бит", self.PARITY),
            ("Количество стоп битов", self.NUMS_STOP_BIT),
            ("Идентификатор устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),

            ("Версия протокола связи", self.read_holding_registers(address=5, slave=slave).registers[0]),
            ("Версия устройства", self.read_holding_registers(address=6, slave=slave).registers[0]),
            ("Версия ПО устройства", self.read_holding_registers(address=7, slave=slave).registers[0]),
            ("Серийный номер", self.read_holding_registers(address=8, slave=slave).registers[0]),
            ("Состояние устройства", self.STATUS[
                self.read_holding_registers(address=10, slave=slave).registers[0]]),
            ("Значение порога ВНИМАНИЕ", self.read_holding_registers(address=51, slave=slave).registers[0]),
            ("Значение порога СРАБОТАЛ", self.read_holding_registers(address=52, slave=slave).registers[0]),
            ("Скорость нарастания температуры", self.read_holding_registers(address=53, slave=slave).registers[0]),
            ("Температура", self.read_holding_registers(address=54, slave=slave).registers[0]),
            ("Скорость нарастания x10", self.read_holding_registers(address=56, slave=slave).registers[0]),
        )
        self.close()
        return params

