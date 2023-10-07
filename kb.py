import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP4, # board.GP9,
        board.GP5, #board.GP8,
        board.GP6, # board.GP7,
        board.GP7, # board.GP6,
        board.GP8, # board.GP5,
        board.GP9, # board.GP4,
    )

    row_pins = (
        board.A1,
        board.A0,
        board.GP22,
        board.GP20,
        board.GP23,
        board.GP21,
    )

    data_pin = board.GP3
    diode_orientation = DiodeOrientation.COL2ROW
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,            36, 37, 38, 39, 40, 41,
        6,  7,  8,  9, 10, 11,            42, 43, 44, 45, 46, 47,
        12, 13, 14, 15, 16, 17,           48, 49, 50, 51, 52, 53,
        18, 19, 20, 21, 22, 23,           54, 55, 56, 57, 58, 59,
                26, 27,                           62, 63,
                            28, 29,   60, 61,
                            34, 35,   66, 67,
                            32, 33,   68, 69
    ]
