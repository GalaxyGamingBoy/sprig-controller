# Sprig Controller

This is a basic controller that uses the [Hackclub Sprig](https://sprig.hackclub.com) as a Gamepad.

## Features

-   Basic Gamepad
-   Modifiable Controls
-   Settings Menu
-   Mouse Mode\*

## Adding a Template

To add your template on a game, feel free to open an issue with the keymaps.  
The keymaps look like:

```python
'TEMPLATE': {
        'w': keys['w'],
        'a': keys['a'],
        's': keys['s'],
        'd': keys['d'],
        'i': keys['i'],
        'j': keys['j'],
        'k': keys['k'],
        'l': keys['l']
    },
```

You will need to change `TEMPLATE` to the games name and `'key'` to the key in the key list.  
A key list is:

```python
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
```

## COMMON ERRORS

-   `[ERROR] SETTING NOT FOUND, IGNORING`: This error commonly appears if a setting is not present. Common settings that trigger this error:

    -   `template_in_use` is `None` or `''`. In this case you can safely ignore the error if you don't want to use a template.

-   `[ERROR] [TEMPLATE] NOT FOUND`: This error is trigerred if a template is not found. Common triggers are mispellings.
