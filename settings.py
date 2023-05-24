from debug import *
from sprig import sprig_keys
import time
from input_mapper import keys, input_map
in_change_key = False
key = ''
keyValues = sorted(list(keys))
currentKeyValue = 0

def delay():
    time.sleep(.1)

def open_settings():
    global in_change_key, settingsMapping
    in_change_key = False
    settingsMapping = False

    printSuccess("Settings: ON")
    print("""
    [W]: Change mapping
    [SDJK]: Quit
    """)

def close_settings():
    printSuccess("Settings: OFF")

def change_key():
    global currentKeyValue
    move_key_value(0)
    printStatus(f"Changing [{key}]")
    print("[A] to go left")
    print("[D] to go right")
    print("[W] to accept")
    print("[S] to go back")
    currentKeyValue = 0

def move_key_value(direction):
    global currentKeyValue
    currentKeyValue += direction
    if currentKeyValue >= len(keyValues):
        currentKeyValue = 0
    elif currentKeyValue < 0:
        currentKeyValue = len(keyValues) - 1

    printStatus(f"[{key}] = [{keyValues[currentKeyValue]}]")

def change_key_loop():
    global in_change_key

    if not sprig_keys['buttons']['a'].value:
        move_key_value(-1)
    elif not sprig_keys['buttons']['d'].value:
        move_key_value(1)
    elif not sprig_keys['buttons']['w'].value:
        input_map[key] = keys[keyValues[currentKeyValue]]
        printStatus(f"[{key}] is now [{keyValues[currentKeyValue]}]")
        open_settings()
        delay()
    elif not sprig_keys['buttons']['s'].value:
        open_settings()
        delay()
    delay()


settingsMapping = False

def setting_loop():
    global settingsMapping

    delay()
    global in_change_key, key
    if not sprig_keys['buttons']['w'].value and not in_change_key and not settingsMapping:
        printStatus("SELECT [KEY]")
        printStatus("[KEY] ~= WASDIJKL")
        settingsMapping = True
        delay()
    
    if settingsMapping:
        for button in sprig_keys['buttons']:
            if not sprig_keys['buttons'][button].value and not in_change_key:
                in_change_key = True
                key = button
                change_key()
    
    if in_change_key:
        delay()
        change_key_loop()