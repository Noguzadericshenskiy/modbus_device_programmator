from pymodbus.client.serial import ModbusSerialClient

from pymodbus.constants import DeviceInformation


client = ModbusSerialClient(
    port="COM1",
    baudrate=19200,
    bytesize=8,
    parity="N",
    stopbits=1
)
client.connect()

hh = client.read_holding_registers(
    address=245,
    count=8,
    slave=0
)

hh1 = hh.registers[0]/10
hh2 = hh.registers[0]/10
