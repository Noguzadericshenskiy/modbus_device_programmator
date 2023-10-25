from devices import (
    ip535_07ea_rs,
    ip535_07ea_rs_START,
    ip329_330_1_1,
    mip_i_ex,
)

LIST_NAMES_DEVICES = [
    ip535_07ea_rs.SignalingDeviceIP53_507EA_RS.NAME,
    ip535_07ea_rs_START.SignalingDeviceStart.NAME,
    ip329_330_1_1.FireDetektorFlameIP329_330_re.NAME,
    mip_i_ex.InterfaceFirefighterModule.NAME,
]

# Colors
main_window_color = "#A1ABAA"
# frame_up_bg_color = "yellow"
# frame_info_bg_color = "#ff7d00"
text_color = "#050990"

# Label
lbl_bg_color = "#ff7d00"
lbl_conf = {
    "background": lbl_bg_color,
    "width": 30,
    "justify": "right",
    "padding": 5,
    "font": 10,
}

#Button
button_color = "#AEE0DB"
btn_conf = {
    'background': button_color,
    "borderwidth": 4,
    "width": 15,
    "padx": 5,
    "pady": 5,
    "font": 10,
}

# Texts
error_enter_address = "Вводить нужно число от 1 до хз"

# TABS
HEADS_TABLE = ["Параметр", "Значение"]
COLUMNS_TABLE = ["Параметр", "Значение"]
