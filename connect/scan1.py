import serial.tools.list_ports
import serial.tools.list_ports_windows

ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device, port.hwid, port.name)

usb_port = serial.tools.list_ports_windows.comports()
for p in usb_port:
    print(p)
