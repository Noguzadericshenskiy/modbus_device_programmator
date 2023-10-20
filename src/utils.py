import serial.tools.list_ports
import serial.tools.list_ports_windows
from typing import Any


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
