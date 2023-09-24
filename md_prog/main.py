import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# port = "ttyUSB0"
# port = "/dev/bus/usb/b'002'/b'002'"
port = "COM6"
slave1 = 10
function_code = 0
starting_address = 0
quantity_of_x = None


# Product Vendor ID(VID) Product ID(PID)
# I-7561U 0x1B5C 0x0104
def main():
    # logger = modbus_tk.utils.create_logger("console")
    # try:
        master = modbus_tk.modbus_rtu.RtuMaster(
            serial.Serial(
                port=port,
                baudrate=8,
                parity="N",
                stopbits=1,
                xonxoff=0,

            )
        )
        master.set_timeout(0.2)
        master.set_verbose(True)
        info = master.execute(slave1, cst.READ_HOLDING_REGISTERS, 0, 10)
        print(info)
        # logger.info(info)


    # except modbus_tk.modbus.ModbusError as err:
        # logger.error("%s- Code=%d", err, err.get_exception_code())
        # Exception(err)
def main1():
    master = modbus_tk.modbus_rtu.RtuMaster(
        serial.Serial(
            port=port,
            baudrate=8,
            parity="N",
            stopbits=1,
            xonxoff=0,

        )
    )
    master.set_timeout(0.2)
    master.set_verbose(True)
    info = master.execute(slave1, cst.READ_HOLDING_REGISTERS, 0, 10)
    print(info)


if __name__ == "__main__":
    main1()
