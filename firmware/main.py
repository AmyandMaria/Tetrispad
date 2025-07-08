import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keyboard import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

macros = Macros()
Encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(Encoder_handler)
keyboard.modules.append(MouseKeys())

Encoder_handler.pins = ((board.D8, board.D9,None))

PINS = [board.D0, board.D1, board.D6, board.D7, board.D10]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E]
]
encoder_handler.map= [
((KC.MW_UP, KC.MW_DN))
]
if name == 'main':
    keyboard.go()
