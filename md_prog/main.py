import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# port = "ttypUSB0"
# port = "/dev/bus/usb/b'002'/b'002'"
port = "tty0"
slave = 10
function_code = 0
starting_address = 0
quantity_of_x = None


# Product Vendor ID(VID) Product ID(PID)
# I-7561U 0x1B5C 0x0104
def main():
    logger = modbus_tk.utils.create_logger("console")
    try:
        master = modbus_tk.modbus_rtu.RtuMaster(
            serial.Serial(
                port=port,
                baudrate=8,
                parity="N",
                stopbits=1,
                # xonxoff=0,

            )
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 3))

    except modbus_tk.modbus.ModbusError as err:
        logger.error("%s- Code=%d", err, err.get_exception_code())
        Exception(err)

if __name__ == "__main__":
    main()
