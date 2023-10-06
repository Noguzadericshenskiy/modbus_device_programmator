import pymodbus.framer
from pymodbus.client import ModbusSerialClient
from devices import devices_def


def get_client(port: str, name_dev: str):
    baudrate_dev = 0
    stopbits_dev = 0
    stopbit_str_dev = ""
    dev_settings = {}

    for i_dev in devices_def:
        if i_dev["name"] == name_dev:
            dev_settings = i_dev
            baudrate_dev = i_dev["baudrate"]
            stopbits_dev = i_dev["stopbits"]
            stopbit_str_dev = i_dev["stopbit_str"]
            break

    client = ModbusSerialClient(
        port=port,
        baudrate=baudrate_dev,
        stopbits=stopbits_dev,
        parity=stopbit_str_dev,
        framer=pymodbus.framer.ModbusRtuFramer,
        timeout=0.05
    )

    return client, dev_settings


def get_info(connect, settings):
    print(connect, settings)
    slave = connect.read_holding_registers(address=settings["register_slave"], slave=settings["slave"])
    baudrate = connect.read_holding_registers(address=settings["register_baudrate"], slave=settings["slave"])
    stopbit = connect.read_holding_registers(address=settings["register_stopbit"], slave=settings["slave"])
    stopbits = connect.read_holding_registers(address=settings["register_stopbits"], slave=settings["slave"])
    id_dev = connect.read_holding_registers(address=4, slave=settings["slave"])
    version_dev = connect.read_holding_registers(address=6, slave=settings["slave"])
    snl = connect.read_holding_registers(address=8, slave=settings["slave"])
    snh = connect.read_holding_registers(address=9, slave=settings["slave"])
    list_info = [
        ("Адрес", slave.registers),
        ("Скорость", baudrate.registers),
        ("Наличие и тип проверочного бита", stopbit.registers),
        ("Количество стоп битов", stopbits.registers),
        ("Идентификатор оборудования", id_dev.registers),
        ("Версия устройства", version_dev.registers),
        ("Серийны номер Lo", snl.registers),
        ("Серийный номер Hi", snh.registers),
    ]
    return list_info

def set_value_register(conn, settings):
    conn.write_registers()


