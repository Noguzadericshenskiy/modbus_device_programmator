import pymodbus.framer
from pymodbus.client import ModbusSerialClient


def connect_dev():
    client = ModbusSerialClient(
        port="COM1",
        baudrate=9600,
        framer=pymodbus.framer.ModbusRtuFramer,
        timeout=0.05
    )
    conn = client.connect()
    yield conn
