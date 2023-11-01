import serial.tools.list_ports
import serial.tools.list_ports_windows
from typing import Any

from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    mip_i_ex,
)

# def get_device(name: str, port: str, baudrate: Any, parity: Any, stopbits: Any):
def get_device(name, port, **kwargs):
    "Получить устройство"
    device = None
    if name == "ИП535-07еа-RS":
        device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS(port **kwargs)
    if name == "ИП535-07еа-RS-ПУСК":
        device = ip535_07ea_rs_START.SignalingDeviceStart(port, **kwargs)
    if name == "ИП329/330-1-1":
        device = ip329_330_1_1.FireDetektorFlameIP329_330_re(port, **kwargs)
    if name == "МИП-И-Ех":
        device = mip_i_ex.InterfaceFirefighterModule(port, **kwargs)
    return device


def get_ports_info() -> list[Any]:
    "Получить информацию о портах"
    ports = []
    usb_port = serial.tools.list_ports_windows.comports()
    for i_port in usb_port:
        ports.append((i_port.device, i_port.description))
    return ports


def get_port(port_info: str) -> str:
    "Получить порт"
    port = ""
    pattern = port_info[0:5]

    for char in pattern:
        if char != " " and char != "":
            port += char

    return port


def check_slave(slave: str) -> bool:
    if slave.isdigit():
        if int(slave) > 0 and int(slave) <= 254:
            return True
        return False
    return False
