# Извещатель пламени ожарный оптический инфракрасный
# ИП 330-3--2-3ИК "Кречет"
# он же ИП СПИ 330/3-ЗИК

import pymodbus.framer
from pymodbus.client import ModbusSerialClient as Client_mb
from pymodbus import bit_read_message, bit_write_message, register_write_message

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
    switch = {1: "ВКЛ", 2: "ВЫКЛ"}

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

    def get_info(self, slave=SLAVE) -> tuple:
        # registr_setup = bin(self.read_holding_registers(address=2, slave=slave).registers[0])
        registr_setup = self.read_holding_registers(address=2, slave=slave).registers
        delay_triggering = 1

        signal_switch = 1
        bit = 1
        switching_relay = 1
        sensitivity = 1
        print(registr_setup)
        params = (
            ("Адрес устройства", self.read_holding_registers(address=0, slave=slave).registers[0]),
            ("Тип извещателя", self.read_input_registers(address=0, slave=slave).registers ),
            ("Статус", self.read_input_registers(address=2, slave=slave).registers),
            ("Подробный статус", self.read_input_registers(address=3, slave=slave).registers),
            ("Серийный номер", self.read_input_registers(address=1, slave=slave).registers),
            ("Внутренняя температура", self.read_input_registers(address=11, slave=slave).registers),
            ("Версия ПО", self.read_input_registers(address=257, count=31, slave=slave).registers),
            ("Задержка срабатывания сигнализации (сек)", delay_triggering),
            ("Сигнальная защелка", signal_switch),
            ("Автоматический и ручной БИТ", bit),
            ("Срабатывание реле от ручного разряда", switching_relay),
            ("Чувствительность обнаружения", sensitivity),
        )
        self.close()
        return params

    def get_delay_triggering(self, registers_data):
        mask0 = 0b0000000000000000
        mask1 = 0b0000000000010000
        mask3 = 0b0000000000100000
        mask5 = 0b0000000000110000
        mask10 = 0b0000000001000000
        mask15 = 0b0000000001010000
        mask20 = 0b0000000001100000
        mask30 = 0b0000000001110000

        if registers_data & mask0 == mask0:
            return "0 сек"
        if registers_data & mask1 == mask1:
            return "Защита от вспышек"
        if registers_data & mask3 == mask3:
            return "3 сек"
        if registers_data & mask5 == mask5:
            return "5 сек"
        if registers_data & mask10 == mask10:
            return "10 сек"
        if registers_data & mask15 == mask15:
            return "15 сек"
        if registers_data & mask20 == mask20:
            return "20 сек"
        if registers_data & mask30 == mask30:
            return "30 cек"

    def get_range_sensitivity(self, registers_data):
        mask1 = 0b0000000000000000
        mask2 = 0b0001000000000000
        mask3 = 0b0010000000000000
        mask4 = 0b0011000000000000

        if registers_data & mask1 == mask1:
            return "1- low"
        if registers_data & mask2 == mask2:
            return "2- low-middle"
        if registers_data & mask3 == mask3:
            return "3- high-middle"
        if registers_data & mask4 == mask4:
            return "4- high"



