import digitalio
import board
from sprig import sprig_init, sprig_keys, sprig_gpio
from debug import *
import displayio
import busio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_st7735r import ST7735R
from input_mapper import input_map

LOOP_SLEEP = .005 # In seconds
in_settings = False
prev_pressed_keys = []

kbd = Keyboard(usb_hid.devices)

def init():
    # Start Init
    sprig_init()
    printStatus("Init Started!")
    sprig_keys['status']['r'].value = True    
    
    # Display
    global display
    displayio.release_displays()
    spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)
    driver = displayio.FourWire(spi_bus=spi, command=board.GP22, chip_select=board.GP20, reset=board.GP26)
    display = ST7735R(driver, width=160, height=128, backlight_pin=board.GP17, rotation=270)
    
    # Init Done
    printStatus("Init Finished!")
    sprig_keys['status']['r'].value = False
    sprig_keys['status']['l'].value = True

def loop():
    global in_settings
    if not sprig_keys['buttons']['a'].value and not sprig_keys['buttons']['w'].value and not sprig_keys['buttons']['i'].value and not sprig_keys['buttons']['l'].value and not in_settings:
            in_settings = True
            printStatus("Settings Opened")
    elif not sprig_keys['buttons']['s'].value and not sprig_keys['buttons']['d'].value and not sprig_keys['buttons']['j'].value and not sprig_keys['buttons']['k'].value and in_settings:
            in_settings = False
            printStatus("Settings Closed")
    elif not in_settings:
          for button in sprig_keys['buttons']:
                if not sprig_keys['buttons'][button].value:
                    #   registerInput(button)
                    kbd.press(input_map[button])
                else:
                    #   deregisterInput(button)
                    kbd.release(input_map[button])
    time.sleep(LOOP_SLEEP)

init()

while True:
    loop()
