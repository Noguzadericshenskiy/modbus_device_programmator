speeds_modbus = {
    1: 1200,
    2: 2400,
    3: 4800,
    4: 9600,
    5: 14400,
    6: 19200,
    7: 28800,
    8: 38400,
    9: 57600,
    10: 115200
}

devices_def = [
    {
        "name": "ИП535-07еа-RS",
        "slave": 1,
        "baudrate": 19200,
        "stopbit": 2,
        "stopbit_str": "E",
        "stopbits": 1,
        "register_slave": 0,
        "register_baudrate": 1,
        "register_stopbit": 2,
        "register_stopbits": 3,
    },
    {
        "name": "ИП535-07еа-RS-“ПУСК”",
        "slave": 1,
        "baudrate": 19200,
        "stopbit": 2,
        "stopbits": 1,
        "register_slave": 0,
        "register_baudrate": 1,
        "register_stopbit": 2,
        "register_stopbits": 3,
    },
    {
        "name": "ИП101-07а-RS",
        "slave": 1,
        "baudrate": 19200,
        "stopbit": 2,
        "stopbits": 1,
        "register_slave": 0,
        "register_baudrate": 1,
        "register_stopbit": 2,
        "register_stopbits": 3,
    }
]
