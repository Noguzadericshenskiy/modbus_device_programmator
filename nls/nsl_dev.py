import loguru
from loguru import logger
import serial
import serial.rs485
import time

import pymodbus.framer
from pymodbus.client import ModbusSerialClient


SPEEDS = (
    (4, 2400),
    (5, 4800),
    (6, 9600),
    (7, 19200),
    (8, 38400),
    (9, 57600),
    (10, 115200),
)

port = "COM6"
speed = 9600
parity = "N"
address = 1
s_bits = 1
com_c_prot = "~01P1\r"
com_det_name = "^01M\r"
com_reset = "^01RS\r"
# data = bytearray(b'\x24\x30\x31\x4d')
data = bytearray(b'\x5e\x30\x31\x4d\r')


def dcon_read():
    with serial.Serial(
        port=port,
        baudrate=speed,
        bytesize=serial.EIGHTBITS,
        parity=parity,
        stopbits=s_bits,
        timeout=0.5,
    ) as conn:

        value = conn.read(10)
    print(value)


def dcon_1():
    com_det_name_b = com_det_name.encode("ASCII")
    com_port = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    no = com_port.write(com_det_name_b)
    ans = com_port.readline(16)
    print("Ans", ans)
    com_port.close()


def dcon_1_1():
    com_port = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    no = com_port.write(data)
    ans = com_port.readline(16)
    print("Ans", ans)
    com_port.close()


@logger.catch()
def dcon_2(comm):
    com_det_name_b = comm.encode("ASCII")
    ser = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    ser.rs485_mode = serial.rs485.RS485Settings()
    no = ser.write(com_det_name_b)
    ans = ser.readline(16)
    print("Ans", ans)
    ser.close()


@logger.catch()
def dcon_2_1():
    ser = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    ser.rs485_mode = serial.rs485.RS485Settings()
    no = ser.write(data)
    ans = ser.readline(16)
    print("Ans", ans)
    ser.close()


# dcon_1()
# print("==============dcon_1_1()")
# time.sleep(1)
# dcon_1_1()
# print("==============dcon_2()")
# time.sleep(1)
# dcon_2(com_det_name)
# time.sleep(1)
# # dcon_2(command_write)
# dcon_2(com_reset)
# print("===============dcon_2_1()")
# time.sleep(1)
# dcon_2_1()


# dcon_2(com_c_prot)
# dcon_2(com_reset)
dcon_2(com_det_name)