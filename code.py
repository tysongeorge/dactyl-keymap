import board

# from kmk.kmk_keyboard import KMKKeyboard
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()
split = Split(
    data_pin=keyboard.data_pin,
    use_pio=True,
    uart_flip=True
)

keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

# settings up layers
MOMENTARY = KC.MO(1)  # enter layer to press one key
MOD_LAYER = KC.LM(1, KC.LSFT)
MOD_LAYER2 = KC.LM(0, KC.LALT)


A = KC.HT(KC.A, KC.LSFT(KC.A), prefer_hold=False, tap_interrupted=True)
I = KC.HT(KC.I, KC.LSFT(KC.I), prefer_hold=False, tap_interrupted=True)
LAYER_TAP = KC.LT(1, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=250) # tap longer than 250ms to trigger
# RCD = KC.HT(KC.DEL, KC.CTRL)
RCA = KC.HT(KC.RGUI, KC.RCTRL(KC.RSFT))

# Workman Layout (US) 
keyboard.keymap = [
    [   # main layer
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,                             KC.N6, KC.N7,   KC.N8,  KC.N9,   KC.N0,  KC.EQL,
        KC.TAB,   KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,                              KC.Y,  KC.U,   I,   KC.O,    KC.P, KC.BSLS,
        KC.ESC,  A,    KC.S,    KC.D,  KC.F,  KC.G,                              KC.H,  KC.J,    KC.K,   KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,                              KC.N,  KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.SLSH,
                        KC.LPRN, KC.LBRACKET,                                                           KC.RPRN, KC.RBRACKET,
                                               KC.LGUI,  KC.SPC,         KC.ENT, KC.BSPC,
                                               KC.LCTRL,  KC.LALT,        KC.DEL,  MOMENTARY,
                                               KC.HOME, MOD_LAYER,         RCA,  KC.END
    ], 

    [   # num layer
        KC.NO,  KC.NO,   KC.NO,   KC.NO, KC.NO, KC.NO,                                   KC.NO,  KC.NO,    KC.NO,   KC.NO,    KC.NO, KC.TRNS,
        KC.NO,   KC.NO,    KC.NO,    KC.NO,  KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.NO,   KC.NO,    KC.NO, KC.BSLS,
        KC.ESC,  KC.N1,    KC.N2,    KC.N3,  KC.N4,  KC.N5,                              KC.N6,    KC.N7,   KC.N8,  KC.N9,    KC.N0, KC.PMNS,
        KC.TRNS,  KC.NO,    KC.EQL,    KC.MINUS,  KC.NO,  KC.NO,                       KC.NO,  KC.NO,    KC.RPRN, KC.RBRACKET, KC.NO, KC.NO,
                        KC.UP, KC.DOWN,                                                           KC.LEFT, KC.RIGHT,
                                              KC.TRNS,  KC.TRNS,         KC.ENT, KC.BSPC,
                                               MOD_LAYER2,  KC.TRNS,        KC.TRNS,  KC.TRNS,
                                               KC.TRNS, KC.TRNS,         KC.TRNS,  KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()
