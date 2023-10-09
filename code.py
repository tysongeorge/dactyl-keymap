import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
split = Split(
    data_pin=keyboard.data_pin,
    use_pio=True,
    uart_flip=True
)

keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(MediaKeys())

# settings up layers
MOMENTARY = KC.MO(1) 
MOD_LAYER = KC.LM(1, KC.LSFT)
MOD_LAYER2 = KC.LM(0, KC.LALT)
LAYER_TAP = KC.LT(1, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=250) # tap longer than 250ms to trigger
RCS = KC.HT(KC.RGUI, KC.RCTRL(KC.RSFT))

# for vim/kakoune
A = KC.HT(KC.A, KC.LSFT(KC.A), prefer_hold=False, tap_interrupted=True)
I = KC.HT(KC.I, KC.LSFT(KC.I), prefer_hold=False, tap_interrupted=True)

# Modified Workman Layout (US) 
keyboard.keymap = [
    [   # main layer
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3, KC.TRNS, KC.TRNS,                           KC.N6, KC.N7,   KC.N8,   KC.N9,   KC.N0,     MOD_LAYER2,
        KC.TAB,    KC.Q,    KC.D,    KC.R,  KC.W,    KC.B,                              KC.J,  KC.F,    KC.U,    KC.P,    KC.SCLN,   KC.BSLS,
        KC.ESC,    A,       KC.S,    KC.H,  KC.T,    KC.G,                              KC.Y,  KC.N,    KC.E,    KC.O,    I,         KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.M,  KC.C,    KC.V,                              KC.K,  KC.L,    KC.COMM, KC.DOT,  KC.TRNS,   KC.SLSH,
                        KC.LPRN, KC.LBRACKET,                                                           KC.RPRN, KC.RBRACKET,
                                               KC.LGUI,  KC.SPC,         KC.ENT,    KC.BSPC,
                                               KC.LCTRL, KC.TRNS,        LAYER_TAP, KC.LALT,
                                               KC.HOME,  MOD_LAYER,      RCS,       KC.END
    ], 

    [   # num layer
        KC.NO,   KC.NO,    KC.NO,    KC.NO,     KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.NO,   KC.NO,    KC.NO,   KC.TRNS,
        KC.NO,   KC.NO,    KC.NO,    KC.NO,     KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.MPRV, KC.MPLY,  KC.MNXT, KC.BSLS,
        KC.ESC,  KC.N1,    KC.N2,    KC.N3,     KC.N4,  KC.N5,                              KC.N6,  KC.N7,    KC.N8,   KC.N9,    KC.N0,   KC.PMNS,
        KC.TRNS, KC.NO,    KC.EQL,   KC.MINUS,  KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.RALT, KC.NO,    KC.NO,   KC.NO,
                        KC.UP, KC.DOWN,                                                           KC.LEFT, KC.RIGHT,
                                              KC.TRNS,     KC.TRNS,         KC.ENT,   KC.BSPC,
                                              KC.TRNS,     KC.TRNS,            KC.TRNS,  KC.TRNS,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,  KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()

