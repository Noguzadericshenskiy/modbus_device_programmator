import minimalmodbus
import minimalmodbus as mmb
import serial

instrument = mmb.Instrument("COM5",10)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.timeout = 0.05
instrument.debug = True


class HZ1(minimalmodbus.Instrument):
    """Instrument class  for   controller
    Args:
        baudrate (int): speed modbus
        portname (str): port name
        slaveaddress (int): slave address
    """

    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    def get_address(self):
        return self.read_register(1,0)
    def get_serial(self):
        ...
    def get_dev_type(self):
        ...
    def get_soft(self):
        ...
    def get_hard(self):
        return "ok"
    def get_atatus(self):
        ...
    def set_address(self):
        ...



try:
    # address_ins = HZ1("COM5", 10)
    # address = address_ins.get_address()
    # print(address)

    value = instrument.read_register(7,  1)
    print(repr(value))
    print(hex(value), " "*10, hex(value >> 8), " "*10, hex(value & 0xff))
    val = instrument.


except IOError:
    print("Не удалось счиать данные с прибора")

