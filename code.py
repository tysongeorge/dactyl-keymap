from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split
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
MOMENTARY_2 = KC.MO(2)
MOD_LAYER = KC.LM(1, KC.LSFT)
RCS = KC.HT(KC.RCTRL, KC.RSFT(KC.RCTRL), tap_time=250, prefer_hold=False)
LCG = KC.HT(KC.LALT, KC.LGUI(KC.LCTRL), tap_time=250, prefer_hold=False)

# for vim/kakoune
# A = KC.HT(KC.A, KC.LSFT(KC.A), prefer_hold=False, tap_interrupted=True)
# I = KC.HT(KC.I, KC.LSFT(KC.I), prefer_hold=False, tap_interrupted=True)

# Modified Workman Layout (US) 
keyboard.keymap = [
    [   # main layer
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3, KC.TRNS, KC.TRNS,                           KC.N6, KC.N7,   KC.N8,   KC.N9,   KC.N0,     MOMENTARY_2,
        KC.TAB,    KC.Q,    KC.D,    KC.R,  KC.W,    KC.B,                              KC.J,  KC.F,    KC.U,    KC.P,    KC.SCLN,   KC.BSLS,
        KC.ESC,    KC.A,    KC.S,    KC.H,  KC.T,    KC.G,                              KC.Y,  KC.N,    KC.E,    KC.O,    KC.I,      KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.M,  KC.C,    KC.V,                              KC.K,  KC.L,    KC.COMM, KC.DOT,  KC.SLSH,   KC.MINUS,
                        KC.LPRN, KC.LBRACKET,                                                           KC.RBRACKET, KC.RPRN,
                                               KC.LGUI,  KC.SPC,        KC.ENT,    KC.BSPC,
                                               KC.LCTRL, KC.NO,         MOMENTARY, KC.RSFT,
                                               KC.HOME,  LCG,           RCS,    KC.END
    ], 

    [   # num layer
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,                              KC.NO,  KC.NO,    KC.NO,   KC.NO,    KC.NO,   KC.TRNS,
        KC.TRNS,  KC.NO,    KC.VOLD,  KC.NO,    KC.VOLU,  KC.NO,                              KC.NO,  KC.NO,    KC.MPRV, KC.MPLY,  KC.MNXT, KC.BSLS,
        KC.TRNS,  KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,  KC.N7,    KC.N8,   KC.N9,    KC.N0,   KC.PMNS,
        KC.TRNS,  KC.NO,    KC.EQL,   KC.MUTE,  KC.NO,    KC.NO,                              KC.NO,  KC.NO,    KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS,
                        KC.UP, KC.DOWN,                                                           KC.LEFT, KC.RIGHT,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,   KC.TRNS,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,  KC.TRNS,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,  KC.TRNS
    ],

    [   # func layer
        KC.NO,    KC.NO,    KC.NO,    KC.NO,     KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.NO,   KC.NO,    KC.NO,   KC.TRNS,
        KC.TRNS,  KC.NO,    KC.NO,    KC.NO,     KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.MPRV, KC.MPLY,  KC.MNXT, KC.BSLS,
        KC.TRNS,  KC.F1,    KC.F2,    KC.F3,     KC.F4,  KC.F5,                              KC.F6,  KC.F7,    KC.F8,   KC.F9,    KC.F10,   KC.PMNS,
        KC.TRNS,  KC.NO,    KC.EQL,   KC.MINUS,  KC.NO,  KC.NO,                              KC.NO,  KC.NO,    KC.TRNS, KC.TRNS,  KC.TRNS, KC.NO,
                        KC.UP, KC.DOWN,                                                           KC.LEFT, KC.RIGHT,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,   KC.TRNS,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,  KC.TRNS,
                                              KC.TRNS,     KC.TRNS,         KC.TRNS,  KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()
