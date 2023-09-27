import pymodbus.framer
from pymodbus.client import ModbusSerialClient
from devices import devases_setup


def get_info(port: str, params_def: dict):

    client = ModbusSerialClient(
        port=port,
        baudrate=params_def["baudrate"],
        framer=pymodbus.framer.ModbusRtuFramer,
        timeout=2
    )
    client.connect()
    data = client.read_holding_registers(address=, slave=params_def["slave"])
    data = client.read_holding_registers(address=, slave=params_def["slave"])
    data = client.read_holding_registers(address=, slave=params_def["slave"])
    data = client.read_holding_registers(address=, slave=params_def["slave"])
    client.close()
    return


