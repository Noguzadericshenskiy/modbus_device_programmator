from src.devices import (
    mip_i_ex,
    ipp_07ea_330_1_gelios,
    ip535_07ea_rs_START,
    ip_330_3_2_3_ik_specpribor,
    ip329_330_1_1,
    ip535_07ea_rs,
    ipes_ik_uv,
    ip101_07a_rs,
    nls_16ai_i,
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
    nls_16ai_i.Analog_Input_NLS_16AII.NAME,
]

SPEEDS = (1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200)
PARITY = ("N", "E", "O")
BITS = ("1",  "2")

BAUDRATE_SIGMA = 9600
PARITY_SIGMA = "N"
S_BITS_SIGMA = "1"
