#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb

class SignalingDeviceIP53507ears(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный ИП535-07еа-RS
    (протокол Modbus RTU)
    Руководство по эксплуатации
    4371-006-43082497-04-04 РЭ, 2021 г.
    """
    def __init__(self, port):
        baudrate_def = 19200
        stopbits_def = 1
        Client_mb.__init__(
            self,
            port,
            baudrate=9600,
            stopbits=1,
            framer=pymodbus.framer.ModbusRtuFramer,
            timeout=2
        )

    def get_info(self, slave=5):
        params = dict()
        params["address"] = self.read_holding_registers(address=0, slave=slave)
        params["protocol_version"] = self.read_holding_registers(address= , slave=slave)
        params["device_version"] = self.read_holding_registers(address= , slave=slave)
        params["po_version"] = self.read_holding_registers(address= , slave=slave)
        params["serial_number"] = self.read_holding_registers(address= , slave=slave)
        params["status_device"] = self.read_holding_registers(address= , slave=slave)

        return params



    id: int = 1
    protocol_version: int = 2
    device_version: int = 3
    po_version: str = 3
    serial_number: str
    status_device: str
    configuration: str


