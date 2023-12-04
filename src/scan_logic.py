from pymodbus.client import ModbusSerialClient


address = [i for i in range(10)]
baudrate = [1200, 2400, 4800, 9600, 14400, 19200, ]
PARITY = ("N", "E", "O")
BITS = ("1", "1.5", "2")


def wer2():
    client = ModbusSerialClient(
        port="COM6",
        baudrate=9600,
        # framer=pymodbus.framer.ModbusRtuFramer,
        parity="N",
        # timeout=0.002
    )
    print(client.connect())
    print(client.is_active())
    print(client.read_holding_registers(address=0, slave=8),)


def wer1():
    for i_bits in BITS:
        for i_parity in PARITY:
            for i_baudrate in baudrate:
                for i_slave in address:
                    client = ModbusSerialClient(
                        port="COM6",
                        baudrate=i_baudrate,
                        # framer=pymodbus.framer.ModbusRtuFramer,
                        parity=i_parity,
                        # timeout=0.02
                    )
                    if not client.read_holding_registers(address=0, slave=i_slave).isError():
                        print("connect:",  "slave-", i_slave, "baudrate-",
                              i_baudrate, "parity-", i_parity, "stop bits-", i_bits)
                    client.close()

wer1()

