class ParameterDevice:
    speed: int = 9600
    bits_in_byte: int = 8
    control_bits: str = "нет" #TODO: изменить значение на реалььное согласно тех. док.
    nums_stop_bits: int = 1
    address_modbus_slave: str
