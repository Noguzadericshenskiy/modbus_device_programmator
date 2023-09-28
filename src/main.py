import pymodbus.framer
from pymodbus.client import ModbusSerialClient
from devices import devases_setup


def get_info(port: str, params_def: dict) -> dict:
    info = {}

    client = ModbusSerialClient(
        port=port,
        baudrate=params_def["baudrate"],
        framer=pymodbus.framer.ModbusRtuFramer,
        timeout=2
    )
    client.connect()
    info["slave"] = client.read_holding_registers(address=params_def["register_slave"], slave=params_def["slave"])
    info["baudrate"] = client.read_holding_registers(address=params_def["register_baudrate"], slave=params_def["slave"])
    info["stopbit"] = client.read_holding_registers(address=params_def["register_stopbit"], slave=params_def["slave"])
    info["stopbits"] = client.read_holding_registers(address=params_def["register_stopbits"], slave=params_def["slave"])

    client.close()
    return info


def change_parameters(port: str, address: int, params_def: dict) -> str:
    client = ModbusSerialClient(
        port=port,
        baudrate=params_def["baudrate"],
        framer=pymodbus.framer.ModbusRtuFramer,
        timeout=0.5
    )
    client.connect()
    client.write_registers(
        address=params_def["register_slave"],
        values=[address, 9600, 1, 1],
        slave=params_def["slave"]
    )
    client.close()

    return "ok"


