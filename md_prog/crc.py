# вычисление контрольной суммы для пакета modbas

# Таблица значений для high-order byte
auch_CRC_hi = []

# Таблица значений для low-order byte
auch_CRC_lo = []

def crc16(data: list) -> int:
    "Расчитывает контрольную сумму, которую нужно прибавить к пакету"

    uch_CRC_hi = 0xff
    uch_CRC_lo = 0xff
    u_index = 0x0000

    for ch in data:
        u_index = uch_CRC_lo ^ ord(ch)
        uch_CRC_lo = uch_CRC_hi ^ auch_CRC_hi[u_index]
        uch_CRC_hi = auch_CRC_lo[u_index]

    return (uch_CRC_hi << 8 | uch_CRC_lo)


def crc16_bt(dt: bytes) -> int:
    "Расчитывает контрольную сумму, если на входе число"

    uch_CRC_hi = 0xff
    uch_CRC_lo = 0xff
    u_index = 0x0000

    for bt in dt:
        u_index = uch_CRC_lo ^ bt
        uch_CRC_lo = uch_CRC_hi ^ auch_CRC_hi[u_index]
        uch_CRC_hi = auch_CRC_lo[u_index]

    return (uch_CRC_hi << 8 | uch_CRC_lo)

def add_crc(bt: list) -> list:
    "Вычисляет младший и старший байт и добавляет в конец списка"
    crc = crc16(bt)
    crc_lo = crc & 0xff
    crc_hi = (crc >> 8) & 0xff
    bt.append(crc_lo)
    bt.append(crc_hi)
    return bt
    