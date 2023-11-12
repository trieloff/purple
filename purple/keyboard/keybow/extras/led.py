import board
from adafruit_hid.keycode import Keycode

import board
from keybow2040 import Keybow2040

class LED:
    _MODIFIER_BLINK = 500
    _MODIFIER_BLINK_ON = 100
    _LOCK_FADE = 800
    _LOCK_FADE_MIN = 0.1
    _LOCK_FADE_NO_COLOR = (32, 32, 32)
    _MOD_COLORS = {
        Keycode.LEFT_SHIFT: (255, 255, 0),
        Keycode.RIGHT_SHIFT: (255, 255, 0),
        Keycode.LEFT_CONTROL: (255, 0, 0),
        Keycode.RIGHT_CONTROL: (255, 0, 0),
        Keycode.LEFT_ALT: (0, 0, 255),
        Keycode.RIGHT_ALT: (0, 0, 255),
        Keycode.LEFT_GUI: (255, 0, 255),
        Keycode.RIGHT_GUI: (255, 0, 255),
    }

    def __init__(self, keybow):
        # Set up Keybow
        self._keybow = keybow
        self._keys = keybow.keys

    def update(self, status):
        # always remember to call keybow.update()!
        self._keybow.update()
        if (
            status.one_shot_key_buffer
            and (status.time % LED._MODIFIER_BLINK) < LED._MODIFIER_BLINK_ON
        ):
            index = (status.time % (len(status.one_shot_key_buffer) * LED._MODIFIER_BLINK)) // LED._MODIFIER_BLINK
            key = status.one_shot_key_buffer[index]
            if key in LED._MOD_COLORS:
                color = LED._MOD_COLORS[key]
        else:
            color = status.layer.color
        
        lock_mult = 1
        if status.lock_key_buffer:
            lock_mult = (
                abs(status.time % (LED._LOCK_FADE * 2) - LED._LOCK_FADE) / LED._LOCK_FADE
            ) * (1 - LED._LOCK_FADE_MIN) + LED._LOCK_FADE_MIN
            if color == (0, 0, 0):
                color = LED._LOCK_FADE_NO_COLOR

        for key in self._keys:
            # set the color
            key.rgb = tuple(lock_mult*i for i in color)
