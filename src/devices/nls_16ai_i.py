"""
RealLab NLS-16AI-I модуль аналогового ввода
Протоколы: DCON, ModBus
ТУ 26.51.70-004-24171143-2021
"""

import time
from pymodbus.framer import ModbusRtuFramer
from pymodbus.client import ModbusSerialClient as Client_mb
from loguru import logger


class Analog_Input_NLS_16AII(Client_mb):
    """NLS-16AI-I модуль аналогового ввода RealLab"""
    NAME = "NLS-16AI-I RealLab"
    SPEEDS_DEVICE = (
        (4, 2400),
        (5, 4800),
        (6, 9600),
        (7, 19200),
        (8, 38400),
        (9, 57600),
        (10, 115200),
    )
    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    STOP_BITS = ((1, "1"),
                 # (2, "1.5"),
                 (3, '2'))
    SLAVE = 1
    SPEED_DEFAULT = 9600
    PARITY = "E"
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
            framer=ModbusRtuFramer,
            timeout=0.5
          )

    @logger.catch()
    def get_info(self, slave=SLAVE) -> tuple:
        time.sleep(0.5)
        data_conn = bin(self.read_holding_registers(address=522, slave=slave).registers[0])[2:].zfill(16)
        time.sleep(0.05)
        address = self.read_holding_registers(address=512, slave=slave).registers[0]
        time.sleep(0.05)
        name = self._get_string(self.read_holding_registers(address=200, slave=slave, count=4).registers)
        time.sleep(0.05)
        speed = self._get_speed(self.read_holding_registers(address=513, slave=slave).registers[0])
        time.sleep(0.05)
        protocol = self._get_protocol(self.read_holding_registers(address=517, slave=slave).registers[0])
        time.sleep(0.05)
        count = self.read_holding_registers(address=521, slave=slave).registers[0]
        time.sleep(0.05)
        deley = self.read_holding_registers(address=800, slave=slave).registers[0]
        time.sleep(0.05)
        version = self._get_string(self.read_holding_registers(address=212, slave=slave, count=4).registers)

        params = (
            ("Имя устройства", name),
            ("Адрес устройства", address),
            ("Паритет", self._get_parity(data_conn)),
            ("Кол-во стоп бит", self._get_s_bit(data_conn)),
            ("Скорость интерфейса", speed),
            ("Протокол", protocol),
            ("Счетчик ответов на команды", count),
            ("Задержка ответа на команды", deley),
            ("Версия программы", version),
        )
        # time.sleep(0.05)
        self.close()
        return params

    def set_slave(self, new_slave: int, slave: int) -> None:
        self.write_register(512, new_slave, slave)
        time.sleep(1)
        self.write_register(288, 43981, slave)
        time.sleep(2)
        self.close()

    @logger.catch()
    def set_baudrate(self, new_spd: int, slave: int) -> None:
        "(6, 9600),(7, 19200), "
        for i_speed in self.SPEEDS_DEVICE:
            if i_speed[1] == new_spd:
                self.write_register(513, i_speed[0], slave)
                time.sleep(1)
                self.close()

    def set_parity(self, new_parity: int, slave: int) -> None:
        data = bin(self.read_holding_registers(address=522, slave=slave).registers[0])[2:].zfill(16)
        print(data)

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        ...

    def _get_parity(self, data: str) -> str:
        hb = int(data[8:], 2)
        for i in self.VERIFICATION_BITS:
            if i[0] == hb:
                return i[1]

    def _get_s_bit(self, data: str) -> str:
        if int(data[8:16], 2) == 1:
            return "1"
        if int(data[8:16], 2) == 2:
            return "2"
        else:
            raise AttributeError

    def _get_speed(self, speed_dev: int) -> str:
        for i_spd in self.SPEEDS_DEVICE:
            if i_spd[0] == speed_dev:
                return str(i_spd[1])

    def _get_protocol(self, data: int) -> str:
        if data == 1:
            return "ModBus"
        else:
            return "DCON"

    def _get_string(self, data: list) -> str:
        string = ""
        for i in data:
            string += i.to_bytes(2, "big").decode()
        return string


def change_protocol_mb():
    ...