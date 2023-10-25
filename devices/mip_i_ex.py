"""МОДУЛЬ ИНТЕРФЕЙСНЫЙ ПОЖАРНЫЙ
«МИП»
"""

import  pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb

class InterfaceFirefighterModule(Client_mb):
    """
    МОДУЛЬ ИНТЕРФЕЙСНЫЙ ПОЖАРНЫЙ
    «МИП»
    интерфейс RS485
    ( версия 2.1 для модулей с ID=13,14,15hex )
    СПР.425521.007 Д1-01
    """

    SPEEDS_DEVICE = {
        1: 1200,
        2: 2400,
        3: 4800,
        4: 9600,
        5: 14400,
        6: 19200,
    }
    SPEED_DEFAULT = SPEEDS_DEVICE[3][1]
    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    NAME = "МИП-И-Ех"
    NUMS_STOP_BIT = 1
    SLAVE = 1
    AV_VERIFICATION_BIT = VERIFICATION_BITS[0][1]
    SLAVE_STATUS = {
        0: "Не определен",
        1: "Короткое замыкание",
        2: "Обрыв",
        3: "Норма",
        5: "Тревога",
    }
    POWER_STATUS = {
        3: "Норма",
        6: "Неисправность"
    }

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

    def get_speed(self):
        return [speed[1] for speed in self.SPEEDS_DEVICE]

    def get_info(self, slave: int = 1) -> tuple:
        params = tuple()
        params = (
            ("ID устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Адрес устройства", self.read_holding_registers(address=1, slave=slave).registers[0]),
            ("Скорость интерфейса", self.read_holding_registers(address=2, slave=slave).registers[0]),
            ("Статус шлейфа 1", self.SLAVE_STATUS[self.read_holding_registers(address=3, slave=slave).registers[0]]),
            ("Статус шлейфа 2", self.SLAVE_STATUS[self.read_holding_registers(address=4, slave=slave).registers[0]]),
            ("Статус шлейфа 3", self.SLAVE_STATUS[self.read_holding_registers(address=5, slave=slave).registers[0]]),
            ("Статус источника 1", self.POWER_STATUS[self.read_holding_registers(address=6, slave=slave).registers[0]]),
            ("Статус источника 2", self.POWER_STATUS[self.read_holding_registers(address=7, slave=slave).registers[0]]),
            ("Длинна кабеля (ТРЕВОГА) 1", self.read_holding_registers(address=8, slave=slave).registers),
            ("Длинна кабеля (ТРЕВОГА) 2", self.read_holding_registers(address=9, slave=slave).registers),
            ("Длинна кабеля (ТРЕВОГА) 3", self.read_holding_registers(address=10, slave=slave).registers),
        )
        self.close()

        return params
