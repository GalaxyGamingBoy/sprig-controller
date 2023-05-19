import board
import digitalio

sprig_gpio = {
    'buttons': {
        'w': board.GP5,
        'a': board.GP6,
        's': board.GP7,
        'd': board.GP8,
        'i': board.GP12,
        'j': board.GP13,
        'k': board.GP14,
        'l': board.GP15
    },
    'status': {
        'l': board.GP28,
        'r': board.GP4
    },
    'display': {
        'lite': board.GP17,
        'miso': board.GP16,
        'sck': board.GP18,
        'mosi': board.GP19,
        'tft_cs': board.GP20,
        'card_cs': board.GP21,
        'dc': board.GP22,
        'reset': board.GP26
    }
}

sprig_keys = {}

def sprig_init():
    for boardSection in sprig_gpio:
        sprig_keys[boardSection] = {}
        for key in sprig_gpio[boardSection]:
            if boardSection != 'display':
                sprig_keys[boardSection][key] = digitalio.DigitalInOut(sprig_gpio[boardSection][key])
                if boardSection == 'buttons':
                    sprig_keys[boardSection][key].direction = digitalio.Direction.INPUT
                    sprig_keys[boardSection][key].pull = digitalio.Pull.UP
                else:
                    sprig_keys[boardSection][key].direction = digitalio.Direction.OUTPUT
