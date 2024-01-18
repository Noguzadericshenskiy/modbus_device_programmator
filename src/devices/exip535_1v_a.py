"""
ИЗВЕЩАТЕЛЬ ПОЖАРНЫй РУЧНОЙ
ВЗРЫВОЗАЩИЩЁННЫЙ АДРЕСНЫЙ
ExИП535-1В-А
Руководство по эксплуатации
908.3065.00.000 РЭ
"""

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalDeviceEXIP535_1V_A(Client_mb):
    """
    Извещатель пожарный ручной взрывозащищенный адресный
    ExИП535-1В-А
    """

    NAME = "ИП101-07а-RS"
    SPEEDS_DEVICE = (
        (0, 9600),
        (1, 14400),
        # (2, 19200), #эта скорость заяввлена, но нет в таблице модбас
        (2, 38400),
        (3, 57600),
        (4, 115200)
    )
    VERIFICATION_BITS = ((1, "N"), (2, "E"), (3, "O"))
    STOP_BITS = ((1, "1"),
                 # (2, "1.5"),
                 (3, '2'))

    SLAVE = 1
    SPEED_DEFAULT = 9600
    PARITY = "N"
    NUMS_STOP_BIT = 1


    def __init__(
            self,
            port,
            baudrate=SPEED_DEFAULT,
            parity=PARITY,
            stopbits=NUMS_STOP_BIT
    ):
        Client_mb.__init__(
            self,
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            parity=parity,
            framer=pymodbus.framer.ModbusRtuFramer,
            timeout=0.05
        )

    def get_info(self, slave=SLAVE) -> tuple:
        params = (
            ("Адрес устройства", self.read_holding_registers(address=1, slave=slave).registers[0]),
            ("Скорость интерфейса", self.SPEEDS_DEVICE[
                self.read_holding_registers(address=4, slave=slave).registers[0]][1]),
            ("Проверочный бит", self.PARITY),
            ("Количество стоп битов", self.NUMS_STOP_BIT),
            ("Идентификатор устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Управление вкл. светодиодной индикации срабатывания извещателя", self._value_lcd_indication(
             self.read_holding_registers(address=3, slave=slave).registers[0])),
            ("Период мигания светодиода мс", self.read_holding_registers(address=5, slave=slave).registers[0]),
            ("Время удержания признака срабатывания при установленном в регистре 14 значении «Не удерживать»",
             self.read_holding_registers(address=11, slave=slave).registers[0]),
            ("Признак срабатывания извещателя",
             self._mark_enabling_detector(self.read_holding_registers(address=12, slave=slave).registers[0])),
            ("Удержание тревожного режима ",
             self._hold_alarm_mode(self.read_holding_registers(address=14, slave=slave).registers[0])),
            ("Тип сброса состояния извещателя",
             self._type_reset_mode(self.read_holding_registers(address=15, slave=slave).registers[0])),
        )
        self.close()
        return params

    def set_slave(self, new_slave: int, slave: int) -> None:
        self.write_register(1, new_slave, slave)
        self._set_key()
        self.close()

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        self.write_register(4, new_spd, slave)
        self.close()

    def set_parity(self,) -> None:
        self.close()

    def set_stop_bit(self,) -> None:
        self.close()

    def _set_key(self) -> None:
        self.write_register(13, 7518)
        # self.close()

    def _value_lcd_indication(self, data) -> str:
        if data == 1:
            return "включено"
        if data == 0:
            return "выключено"

    def _mark_enabling_detector(self, mark_data) -> str:
        if mark_data == 0:
            return "дежурный режим"
        if mark_data == 1:
            return "извещатель в тревожном режиме"

    def _hold_alarm_mode(self, mark_mode) -> str:
        if mark_mode == 0:
            return "yне удерживать"
        if mark_mode == 1:
            return "удерживать"

    def _type_reset_mode(self, mark_type) -> str:
        if mark_type == 0:
            return "Без подтверждения ключом (регистр 13)"
        if mark_type == 1:
            return "С подтверждением ключом"
