#ИЗВЕЩАТЕЛЬ пожарный ручной взрывозащищенный адресный
# ИП535-07еа-RS
import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class FireDetektorFlameIP329_330_re(Client_mb):
    """
    ИЗВЕЩАТЕЛЬ пожарный пламени ИП329-330-re
    (протокол Modbus RTU)
    """
    SPEEDS_DEVICE = (
        (1, 1200),
        (2, 2400),
        (4, 4800),
        (8, 9600),
        (10, 19200),
    )
    # VERIFICATION_BITS = (1, "N")
    STATUS_D2 = ((1, "Фиксация"), (0, "Фиксаця отключена"),)
    STATUS_D1 = ((1, "Далеко"), (0, "Близко"),)
    STATUS_D0 = ((1, "Быстро"), (0, "Медленно"),)
    NAME = "ИП329/330-1-1"
    SPEED_DEFAULT = SPEEDS_DEVICE[3][1]
    # AV_VERIFICATION_BIT = VERIFICATION_BITS[0]
    NUMS_STOP_BIT = 1
    SLAVE = 1


    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            # paryty=AV_VERIFICATION_BIT,
            stopbits=NUMS_STOP_BIT
    ):
        Client_mb.__init__(
            self,
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            # parity=1,
            framer=pymodbus.framer.ModbusRtuFramer,
            # framer=pymodbus.framer.ModbusBinaryFramer,
            timeout=0.05
        )

    def get_info(self):
        adress = self.read_holding_registers(1, slave=9)
        # stetus = self.read_device_information()
        print(adress)
        info = self.read_holding_registers(address=2, slave=9)
        print(info)
        # print(adress.bits)
        # print(adress.registers)

