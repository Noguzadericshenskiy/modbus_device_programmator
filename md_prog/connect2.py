import pymodbus.framer
from pymodbus.client import ModbusSerialClient

from md_prog.devices.ip535_07ea_rs import SignalingDeviceIP53507ears


client = ModbusSerialClient(port="COM5", baudrate=9600, framer=pymodbus.framer.ModbusRtuFramer, timeout=2)

conn = client.connect()
print("connect", conn)
value = client.read_holding_registers(2, slave=5)
print(value.registers)
client.close()

val = SignalingDeviceIP53507ears(port="COM5").get_info()

print(val.registers)

# value = client.read_holding_registers(34,  slave=5)
# print(value.registers)
# client.close()

