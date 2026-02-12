# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros() 
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D5, board.D6, board.D7, board.D8, board.D9, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
RIGHT_CLICK = KC.Macro(
    Press(KC.LSHIFT),
    Tap(KC.F10),
    Release(KC.LSHIFT)
)
# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [RIGHT_CLICK, KC.LEFT, KC.UP, KC.DOWN, KC.ENTER, KC.RIGHT]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()