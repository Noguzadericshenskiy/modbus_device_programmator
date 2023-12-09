# Извещатель пламени ожарный оптический инфракрасный
# ИП 330-3--2-3ИК "Кречет"
# он же ИП СПИ 330/3-ЗИК

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb


class SignalingDeviceIP330_3_2_3IK(Client_mb):
    """
    Извещатель пламени ожарный оптический инфракрасный:
    ИП 330-3--2-3ИК "Кречет"
    ОН ЖЕ
    ИП СПИ 330/3-ЗИК
    (протокол Modbus RTU)
    Руководство по эксплуатации
    26.30.50.121-007-16676952-2020 РЭ
    """

    SPEEDS_DEVICE = (
        (1, 9600),
    )

    VERIFICATION_BITS = ((1, "N"),)

    NAME = "ИП330-3-2-ЗИК(Кречет)"
    SPEED_DEFAULT = SPEEDS_DEVICE[0][1]
    AV_VERIFICATION_BIT = VERIFICATION_BITS[0][1]
    NUMS_STOP_BIT = 1
    SLAVE = 1

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
            timeout=0.05
        )

    def set_slave(self, new_slave: int, slave: int) -> None:
        self.write_register(0, new_slave, slave)
        self.close()

    def set_baudrate(self, new_spd: int, slave: int) -> None:
        self.close()

    def set_parity(self, new_parity: int, slave: int) -> None:
        self.close()

    def set_stop_bit(self, new_stop_bit: int, slave: int) -> None:
        self.close()

    def get_info(self, slave=SLAVE) -> tuple:
        register_setup = self.read_holding_registers(address=1, slave=slave).registers[0]
        delay_triggering = 1
        signal_switch = 1
        bit = 1
        switching_relay = 1
        sensitivity = 1
        params = (
            ("Адрес устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Тип извещателя", self.read_input_registers(address=0, slave=slave).registers),
            ("Статус", self.read_input_registers(address=2, slave=slave).registers),
            ("Подробный статус", self.read_input_registers(address=3, slave=slave).registers),
            ("Серийный номер", self.read_input_registers(address=1, slave=slave).registers[0]),
            ("Внутренняя температура", self.read_input_registers(address=11, slave=slave).registers[0]),
            ("Версия ПО", self.read_input_registers(address=257, count=31, slave=slave).registers),
            ("Задержка срабатывания сигнализации (сек)", self.get_delay_triggering(register_setup)),
            ("Сигнальная защелка", self.get_signal_switch(register_setup)),
            ("Автоматический и ручной БИТ", self.get_hand_bit(register_setup)),
            ("Срабатывание реле от ручного разряда", self.get_manual_switch(register_setup)),
            ("Чувствительность обнаружения", self.get_range_sensitivity(register_setup)),
        )
        self.close()
        return params

    @classmethod
    def get_manual_switch(self, data):
        mask0 = 0b0000100000000000
        mask1 = 0b0000000000000000

        if data & mask0 == mask0:
            return "Ручной разряд ВКЛ"
        if data & mask1 == mask1:
            return "Ручной разряз ВЫКЛ"

    @classmethod
    def get_signal_switch(self, data):
        mask0 = 0b0000000010000000
        mask1 = 0b0000000000000000

        if data & mask0 == mask0:
            return "ВКЛ"
        if data & mask1 == mask1:
            return "ВЫКЛ"

    @classmethod
    def get_hand_bit(self, data):
        mask0 = 0b0000010000000000
        mask1 = 0b0000000000000000

        if data & mask0 == mask0:
            return "Автоматический и ручной"
        if data & mask1 == mask1:
            return "Только ручной"

    @classmethod
    def get_delay_triggering(self, data):
        mask0 = 0b0000000000000000
        mask1 = 0b0000000000010000
        mask3 = 0b0000000000100000
        mask5 = 0b0000000000110000
        mask10 = 0b0000000001000000
        mask15 = 0b0000000001010000
        mask20 = 0b0000000001100000
        mask30 = 0b0000000001110000

        if data & mask0 == mask0:
            return "0 сек"
        if data & mask1 == mask1:
            return "Защита от вспышек"
        if data & mask3 == mask3:
            return "3 сек"
        if data & mask5 == mask5:
            return "5 сек"
        if data & mask10 == mask10:
            return "10 сек"
        if data & mask15 == mask15:
            return "15 сек"
        if data & mask20 == mask20:
            return "20 сек"
        if data & mask30 == mask30:
            return "30 cек"

    @classmethod
    def get_range_sensitivity(self, data):
        mask1 = 0b0000000000000000
        mask2 = 0b0001000000000000
        mask3 = 0b0010000000000000
        mask4 = 0b0011000000000000

        if data & mask1 == mask1:
            return "1- low"
        if data & mask2 == mask2:
            return "2- low-middle"
        if data & mask3 == mask3:
            return "3- high-middle"
        if data & mask4 == mask4:
            return "4- high"
