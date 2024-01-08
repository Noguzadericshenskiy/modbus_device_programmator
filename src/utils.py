import serial

from serial.tools import list_ports_windows
from pymodbus.client import ModbusSerialClient
from pymodbus.framer import ModbusRtuFramer, rtu_framer
from pymodbus.exceptions import ConnectionException
from typing import Any

from src.devices import (
    mip_i_ex,
    ipp_07ea_330_1_gelios,
    ip535_07ea_rs_START,
    ip_330_3_2_3_ik_specpribor,
    ip329_330_1_1,
    ip535_07ea_rs,
    ipes_ik_uv,
    ip101_07a_rs,
    nls_16ai_i,
)


def get_value_stop_bits_dev(dev, stop_bits: str) -> int:
    """Возвращает значение стоп бита из списка устройства"""
    for s_bit in dev.STOP_BITS:
        if s_bit[1] == stop_bits:
            return s_bit[0]


def get_value_parity_dev(dev, parity: str) -> int :
    """ Возвращает значение проверки на четность
        из списка скоростей конкретного устройства"""
    for par in dev.VERIFICATION_BITS:
        if par[1] == parity:
            return par[0]


def get_value_baudrate_dev(dev, bdr: int) -> int:
    """ Возвращает значение скорости
        из списка скоростей конкретного устройства"""
    for spd in dev.SPEEDS_DEVICE:
        if spd[1] == bdr:
            return spd[0]


def get_device(name: str, port: Any, **kwargs):
    "Получить объект устройства по названию"
    if name == "ИП535-07еа-RS":
        return ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port, **kwargs)
    if name == "ИП535-07еа-RS-ПУСК":
        return ip535_07ea_rs_START.SignalingDeviceIP53_507EA_Start(port, **kwargs)
    if name == "ИП101-07а-RS":
        return ip101_07a_rs.SignalDeviceIP101_07A_RS(port, **kwargs)
    if name == "ИП329/330-1-1 (Феникс)":
        return ip329_330_1_1.FireDetektorFlameIP329_330_re(port, **kwargs)
    if name == "МИП-И-Ех":
        return mip_i_ex.InterfaceFirefighterModule(port, **kwargs)
    if name == "ИП330-3-2-ЗИК(Кречет)":
        return ip_330_3_2_3_ik_specpribor.SignalingDeviceIP330_3_2_3IK(port, **kwargs)
    if name == "ИПП-07еа-330-1(Гелиос-3 ИК)":
        return ipp_07ea_330_1_gelios.SignalingDeviceIPP_07_330_1(port, **kwargs)
    if name == "ИПЭС–ИК/УФ (Электронстандарт)":
        return ipes_ik_uv.FireDetektorFlame_IPES_IK_UV(port, **kwargs)
    if name == "NLS-16AI-I RealLab":
        return nls_16ai_i.Analog_Input_NLS_16AII(port, **kwargs)


def get_ports_info() -> list[Any]:
    "Получить список портов"
    ports = []
    usb_port = list_ports_windows.comports()
    for i_port in usb_port:
        ports.append((i_port.device, i_port.description))
    return ports


def get_port(port_info: str) -> str:
    "Получить название порта из строки"
    port = ""
    pattern = port_info[0:5]
    for char in pattern:
        if char != " " and char != "":
            port += char
    return port


def device_dcon(port, slave, baudrate, parity, bits):
    "Получает данные(ответ) от устройства dcon"
    dev = serial.Serial(
        port=port,
        baudrate=baudrate,
        bytesize=8,
        parity=parity,
        stopbits=bits,
        timeout=0.5
    )
    s_comm = "^" + format(slave, "x").zfill(2) + "M\r"
    dev.write(s_comm.encode("ASCII"))
    data: bytes = dev.readline(16)
    dev.close()
    return data


def device_mb(port, slave,  baudrate, parity, bits):
    client = ModbusSerialClient(
        port=port,
        baudrate=baudrate,
        parity=parity,
        stopbits=bits,
        timeout=0.2
    )
    # if (not client.read_holding_registers(address=0, slave=i_slave).isError()) or \
    if not client.read_input_registers(slave=slave, address=0).isError():
        client.close()
        return True
    else:
        client.close()
        return False


def send_decon_command(
        command: bytes,
        address: int,
        port: str,
        speed: int,
        parity: str,
        s_bits: int) -> str:
    conn = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    conn.write(command)
    data = conn.readline(16)
    conn.close()
    return str(data.decode("ASCII"))


def nls_change_protocol_mb(address, port, speed, parity, s_bits) -> Any:
    "Установить протокол ModBus"
    string_command: str = "~" + format(address, "x").zfill(2) + "P1\r"
    command: bytes = string_command.encode("ASCII")
    conn = serial.Serial(port, speed, 8, parity, s_bits, timeout=0.5)
    conn.write(command)
    data = conn.readline(16)
    conn.close()
    check_str = str(data.decode("ASCII"))
    if check_str[:3] == "!" + format(address, "x").zfill(2):
        return check_str
    else:
        raise ValueError


def nls_change_protocol_dcon(address, port, speed, parity, s_bits) -> None:
    "Установить протокол DCON"
    dev = nls_16ai_i.Analog_Input_NLS_16AII(port=port, baudrate=speed, parity=parity, stopbits=s_bits)
    dev.nls_change_protocol_on_dcon(address)
    protocol = dev.read_holding_registers(address=517, slave=address).registers[0]
    dev.close()
    if protocol != 0:
        raise ValueError






