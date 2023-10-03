import pymodbus.framer
from pymodbus.client import ModbusSerialClient

# from md_prog.devices.ip535_07ea_rs import SignalingDeviceIP53507ears


client = ModbusSerialClient(port="COM6",
                            baudrate=19200,
                            framer=pymodbus.framer.ModbusRtuFramer,
                            parity="E",
                            timeout=0.5
                            )

conn = client.connect()
print("connect", conn)
value = client.read_holding_registers(address=0, slave=1)
client.write_registers()
print(value.registers)
client.close()
print("connect", conn)

# val = SignalingDeviceIP53507ears(port="COM5").get_info()
#
# print(val.registers)

# value = client.read_holding_registers(34,  slave=5)
# print(value.registers)
# client.close()

