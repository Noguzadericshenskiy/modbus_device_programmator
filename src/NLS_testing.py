import time
from pymodbus.framer import ModbusRtuFramer
from pymodbus.client import ModbusSerialClient as Client_mb
from loguru import logger


class NLS(Client_mb):

    def __init__(self):
        Client_mb.__init__(
            self,
            port="COM14",
            baudrate=9600,
            stopbits=1,
            parity="N",
            # framer=ModbusRtuFramer,
            timeout=0.2
        )

    @logger.catch()
    def get_info(self, slave):
        # time.sleep(0.5)
        # data_conn = bin(self.read_holding_registers(address=522, slave=slave).registers[0])[2:].zfill(16)
        # time.sleep(0.05)
        address = self.read_holding_registers(address=512, slave=slave, ).registers[0]
        print("1", address)
        time.sleep(0.5)
        name = self.read_holding_registers(address=200, slave=slave, count=4, ).registers
        print("2", name)
        time.sleep(0.5)
        speed = self.read_holding_registers(address=513, slave=slave, ).registers[0]
        print("3", speed)
        time.sleep(0.5)
        protocol = self.read_holding_registers(address=517, slave=slave,).registers[0]
        print("4", protocol)
        time.sleep(0.5)
        count = self.read_holding_registers(address=521, slave=slave, ).registers[0]
        print("5", count)
        time.sleep(0.5)
        deley = self.read_holding_registers(address=800, slave=slave, ).registers[0]
        print("6", deley)
        time.sleep(0.5)
        version = self.read_holding_registers(address=212, slave=slave, count=4, ).registers
        print("7", version)
        time.sleep(0.5)
        input_data: int = self.read_holding_registers(address=522, slave=slave, ).registers[0]
        h_byte, l_byte = input_data.to_bytes(2, "big")
        print("8", h_byte, l_byte)
        print("OK", h_byte, l_byte)


dev = NLS()
dev.get_info(1)
dev.close()
