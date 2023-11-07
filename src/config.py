from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    mip_i_ex,
)

LIST_NAMES_DEVICES = [
    ip535_07ea_rs.SignalingDeviceIP53_507EA_RS.NAME,
    ip535_07ea_rs_START.SignalingDeviceIP53_507EA_Start.NAME,
    ip329_330_1_1.FireDetektorFlameIP329_330_re.NAME,
    mip_i_ex.InterfaceFirefighterModule.NAME,
]

SPEEDS = (1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200)
PARITY = ("N", "E", "O")
BITS = (1, 2)

BAUDRATE_SIGMA = 9600
PARITY_SIGMA = "N"
S_BITS_SIGMA = 1

# Colors
main_window_color = "#A1ABAA"
# frame_up_bg_color = "yellow"
# frame_info_bg_color = "#ff7d00"
text_color = "#050990"

# Label
lbl_bg_color = "#ff7d00"
lbl_conf = {
    "background": lbl_bg_color,
    "width": 15,
    "justify": "right",
    "padding": 5,
    "font": 10,
}

#Button
button_color = "#AEE0DB"
btn_conf = {
    'background': button_color,
    "borderwidth": 2,
    "width": 30,
    "padx": 2,
    "pady": 2,
    "font": 8,
}
# combobox
combobox_conf_sm = {
    "width": 20,
    "height": 10,
}

combobox_conf_long = {
    "width": 50,
    "height": 10,
}
# Texts
error_enter_address = "Вводить нужно число от 1 до хз"

# TABS
HEADS_TABLE = ["Параметр", "Значение"]
COLUMNS_TABLE = ["Параметр", "Значение"]
