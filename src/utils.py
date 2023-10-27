import serial.tools.list_ports
import serial.tools.list_ports_windows
from typing import Any

from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    mip_i_ex,
)

def get_device(name: str):
    "Получить устройство"
    device = None
    if name == "ИП535-07еа-RS":
        device = ip535_07ea_rs.SignalingDeviceIP53_507EA_RS()
    if name == "ИП535-07еа-RS-ПУСК":
        device = ip535_07ea_rs_START.SignalingDeviceStart()
    if name == "ИП329/330-1-1":
        device = ip329_330_1_1.FireDetektorFlameIP329_330_re()
    if name == "МИП-И-Ех":
        device = mip_i_ex.InterfaceFirefighterModule()
    return device


def get_port_info() -> list[Any]:
    ports = []
    usb_port = serial.tools.list_ports_windows.comports()
    for i_port in usb_port:
        ports.append((i_port.device, i_port.description))
    return ports


def get_port(port_info: str) -> str:
    port = ""
    pattern = port_info[0:5]

    for char in pattern:
        if char != " " and char != "":
            port += char

    return port
