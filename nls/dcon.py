"""
RealLab NLS-16AI-I модуль аналогового ввода
Протоколы: DCON, ModBus
ТУ 26.51.70-004-24171143-2021
"""


import serial
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb

comm_get_name = "^01M\r"
comm_current_protokol = "~01P1\r"
class Analog_Input_SLS_16AII(Client_mb):
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
            framer=pymodbus.framer.ModbusRtuFramer,
            timeout=0.05
          )

    def get_info(self, slave=SLAVE) -> tuple:
        ...

    def set_slave(self, new_slave: int, slave: int) -> None:
        ...

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        ...

    def set_parity(self, new_parity: int, slave: int) -> None:
        ...

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        ...


