# Извещатель пламени пожарный ИП 329/330-1-1, ИПЭС – ИК/УФ
# ИПЭС-ИК/УФ электронстандарт прибор
# он же ИП 329/330-1-1

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class FireDetektorFlame_IPES_IK_UV(Client_mb):
    """
    Извещатель пламени пожарный ИП 329/330-1-1, - ИПЭС – ИК/УФ
    ИПЭС-ИК/УФ (электронстандарт прибор)
    Руководство по эксплуатации
    ЖСКФ.425248.001 РЭ
    """

    SPEEDS_DEVICE = (
        (1, 1200),
        (2, 2400),
        (4, 4800),
        (8, 9600),
        (10, 19200),
    )
    VERIFICATION_BITS = (1, "N")
    NAME = "ИПЭС–ИК/УФ (Электронстандарт)"
    SPEED_DEFAULT = SPEEDS_DEVICE[3][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[0]
    NUMS_STOP_BIT = 1
    SLAVE = 3

    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            parity=AV_VERIFICATION_BIT,
            stopbits=NUMS_STOP_BIT
    ):
        Client_mb.__init__(
            self,
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            parity=parity,
            framer=pymodbus.framer.ModbusRtuFramer,
        )

    def get_info(self, slave=SLAVE) -> tuple:
        data_reg_0: str = bin(self.read_holding_registers(address=0, slave=slave).registers[0])[2:].zfill(16)
        data_reg_1: str = bin(self.read_holding_registers(address=1, slave=slave).registers[0])[2:].zfill(16)
        params = (
            ("Адрес устройства", self.get_slave(data_reg_0)),
            ("Скорость", self.get_speed(data_reg_0)),
            ("Скорость срабатывания", "Быстор" if data_reg_1[7] == "1" else "Медленно"),
            ("Расстояние", "Далеко" if data_reg_1[6] == "1" else "Близко"),
            ("Фиксация", "Вкл" if data_reg_1[5] == "1" else "ВЫКЛ"),
            ("Стекло", "Загрязнение стекла" if data_reg_1[13] == "1" else "Норма"),
            ("Авария", "Авария" if data_reg_1[14] == "1" else "Норма"),
            ("Пожар", "Пожар" if data_reg_1[15] == "1" else "Норма"),
        )
        self.close()
        return params

    @classmethod
    def get_speed(self, data: str) -> int:
        hb = int(data[8:], 2)
        for i in self.SPEEDS_DEVICE:
            if i[0] == hb:
                return i[1]

    @classmethod
    def get_slave(self, data: str) -> int:
        return int(data[:8], 2)

    def set_slave(self, new_slave: int, slave: int) -> None:
        """
        H - slave
        L - speed
        """
        data_reg_0: int = self.read_holding_registers(address=0, slave=slave).registers[0]
        h_byte, l_byte = data_reg_0.to_bytes(2, "big")
        data = ((new_slave & 0xff) << 8) | (l_byte & 0xff)
        self.write_register(0, data, slave)
        self.close()

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        """
        H - slave
        L - speed
        """
        data_reg_0: int = self.read_holding_registers(address=0, slave=slave).registers[0]
        h_byte, l_byte = data_reg_0.to_bytes(2, "big")
        data = ((h_byte & 0xff) << 8) | (new_spd & 0xff)
        self.write_register(0, data, slave)
        self.close()

    def set_parity(self, new_parity: int, slave: int) -> None:
        self.close()

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        self.close()
