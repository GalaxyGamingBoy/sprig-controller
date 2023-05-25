from adafruit_hid.keycode import Keycode

input_map = {
    'w': Keycode.W,
    'a': Keycode.A,
    's': Keycode.S,
    'd': Keycode.D,
    'i': Keycode.I,
    'j': Keycode.J,
    'k': Keycode.K,
    'l': Keycode.L
}

keys = {
    'q': Keycode.Q,
    'w': Keycode.W,
    'e': Keycode.E,
    'r': Keycode.R,
    't': Keycode.T,
    'y': Keycode.Y,
    'u': Keycode.U,
    'i': Keycode.I,
    'o': Keycode.O,
    'p': Keycode.P,
    'a': Keycode.A,
    's': Keycode.S,
    'd': Keycode.D,
    'f': Keycode.F,
    'g': Keycode.G,
    'h': Keycode.H,
    'j': Keycode.J,
    'k': Keycode.K,
    'l': Keycode.L,
    'z': Keycode.Z,
    'x': Keycode.X,
    'c': Keycode.C,
    'v': Keycode.V,
    'b': Keycode.B,
    'n': Keycode.N,
    'm': Keycode.M,
    'UP': Keycode.UP_ARROW,
    'DOWN': Keycode.DOWN_ARROW,
    'LEFT': Keycode.LEFT_ARROW,
    'RIGHT': Keycode.RIGHT_ARROW,
    'ENTER': Keycode.ENTER,
    'ESC': Keycode.ESCAPE
}

# TEMPLATES!
templates = {
    'DEFAULT': {
        'w': keys['w'],
        'a': keys['a'],
        's': keys['s'],
        'd': keys['d'],
        'i': keys['i'],
        'j': keys['j'],
        'k': keys['k'],
        'l': keys['l']
    },
    'UNDERTALE': {
        'w': keys['UP'],
        'a': keys['LEFT'],
        's': keys['DOWN'],
        'd': keys['RIGHT'],
        'i': keys['c'],
        'j': keys['ESC'],
        'k': keys['x'],
        'l': keys['ENTER']
    }
}
