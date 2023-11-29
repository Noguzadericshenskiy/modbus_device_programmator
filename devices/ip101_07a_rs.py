"""
Извещатель пожарный тепловой взрывозащищенный
программируемый адресный
ИП101-07а-RS
"""

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb
from pymodbus import bit_read_message, bit_write_message, register_write_message

class SignalDeviceIP101_07A_RS(Client_mb):
    """
    Извещатель пожарный тепловой взрывозащищенный
    программируемый адресный
    Руководство по эксплуатации 4371-008-43082497-05-05 РЭ, 2022 г.
    """
    NAME = "ИП101-07а-RS"
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
    STOP_BITS = ((1, "1"), (2, "1.5"), (3, '2'))

    SLAVE = 1
    SPEED_DEFAULT = 19200
    PARITY = "E"
    NUMS_STOP_BIT = 1

    STATUS = {
        1: "Загрузка",
        2: "Тест",
        3: "Норма",
        4: "Внимание",
        5: "Сработал",
        6: "Неисправность"
    }

    CONTROL_REGISTER = (
        (0, "норма"),
        (1, "пеезагрузка"),
        (2, "сброс настроек по умолчанию"),
        (4, "сброс зафиксированных событий"),
        (16, "установка адреса МВ равного последним 2 цифрам сер.№"))

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
            ("Адрес устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Скорость интерфейса", self.SPEEDS_DEVICE[
                self.read_holding_registers(address=1, slave=slave).registers[0] - 1][1]),
            ("Проверочный бит", self.VERIFICATION_BITS[
                self.read_holding_registers(address=2, slave=slave).registers[0] - 1][1]),
            ("Количество стоп битов", self.STOP_BITS[
                self.read_holding_registers(address=3, slave=slave).registers[0] - 1][1]),
            ("Идентификатор устройства", self.read_holding_registers(address=4, slave=slave).registers[0]),
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

    def get_diagnostic_info(self):
        per = self.read_holding_registers(address=11, slave=5).registers[0]
        print(bin(per))
