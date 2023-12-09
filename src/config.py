from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    ip_330_3_2_3_ik_specpribor,
    ip101_07a_rs,
    mip_i_ex,
    ipp_07ea_330_1_gelios,
    ipes_ik_uv,
)

LIST_NAMES_DEVICES = [
    ip535_07ea_rs.SignalingDeviceIP53_507EA_RS.NAME,
    ip535_07ea_rs_START.SignalingDeviceIP53_507EA_Start.NAME,
    ip329_330_1_1.FireDetektorFlameIP329_330_re.NAME,
    ip101_07a_rs.SignalDeviceIP101_07A_RS.NAME,
    mip_i_ex.InterfaceFirefighterModule.NAME,
    ip_330_3_2_3_ik_specpribor.SignalingDeviceIP330_3_2_3IK.NAME,
    ipp_07ea_330_1_gelios.SignalingDeviceIPP_07_330_1.NAME,
    ipes_ik_uv.FireDetektorFlame_IPES_IK_UV.NAME,
]

SPEEDS = (1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200)
PARITY = ("N", "E", "O")
BITS = ("1", "1.5", "2")

BAUDRATE_SIGMA = 9600
PARITY_SIGMA = "N"
S_BITS_SIGMA = "1"

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
error_enter_address = "Вводить нужно число от 1 до 254"

# TABS
HEADS_TABLE = ["Параметр", "Значение"]
COLUMNS_TABLE = ["Параметр", "Значение"]
