
def get_bt(data: str):
    bt_0 = "0000" + data
    bt = int(bt_0[-2:])
    return bt

print(get_bt("1234"))

# преобразовать число в 2 байта
number = 1234
print(hex(number), hex(number >> 8), hex(number & 0xff))