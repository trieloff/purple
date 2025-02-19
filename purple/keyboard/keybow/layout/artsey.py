from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

from purple.action import Action, Lock, MediaPress, MouseMove, MousePress, OneShot, Press, ToLayer
from purple.helpers import key
from purple.layer import Layer

# Keys
#
#  3  7  11  15
#  2  6  10  14
#  1  5  9   13
#  0  4  8   12
#

class Layout:
    name = "ARTSEY (Right)"
    auto_mod = []
    layers = [
        Layer(
            "Base",
            {
                key(1): Action(Press(Keycode.A), ToLayer(2)),
                key(12) + key(0): Action(Press(Keycode.B)),
                key(4) + key(0): Action(Press(Keycode.C)),
                key(9) + key(5) + key(1): Action(Press(Keycode.D)),
                key(0): Action(Press(Keycode.E), ToLayer(3)),
                key(5) + key(1): Action(Press(Keycode.F)),
                key(9) + key(5): Action(Press(Keycode.G)),
                key(8) + key(0): Action(Press(Keycode.H)),
                key(8): Action(Press(Keycode.I)),
                key(13) + key(9): Action(Press(Keycode.J)),
                key(12) + key(4): Action(Press(Keycode.K)),
                key(8) + key(4) + key(0): Action(Press(Keycode.L)),
                key(12) + key(8) + key(4): Action(Press(Keycode.M)),
                key(12) + key(8): Action(Press(Keycode.N)),
                key(12): Action(Press(Keycode.O), ToLayer(4)),
                key(12) + key(8) + key(0): Action(Press(Keycode.P)),
                key(13) + key(9) + key(1): Action(Press(Keycode.Q)),
                key(5): Action(Press(Keycode.R)),
                key(13): Action(Press(Keycode.S), ToLayer(1)),
                key(9): Action(Press(Keycode.T)),
                key(8) + key(4): Action(Press(Keycode.U)),
                key(13) + key(5): Action(Press(Keycode.V)),
                key(13) + key(1): Action(Press(Keycode.W)),
                key(13) + key(9) + key(5): Action(Press(Keycode.X)),
                key(4): Action(Press(Keycode.Y)),
                key(13) + key(9) + key(5) + key(1): Action(Press(Keycode.Z)),

                key(5) + key(1) + key(12): Action(Press(Keycode.ESCAPE)),
                key(1) + key(0): Action(Press(Keycode.ENTER)),
                key(9) + key(5) + key(1) + key(12): Action(Press(Keycode.TAB)),
                key(1) + key(8) + key(4): Action(Press(Keycode.QUOTE)),
                key(13) + key(0): Action(OneShot(Keycode.CONTROL), Press(Keycode.CONTROL, False), hold=True),
                key(1) + key(4): Action(Press(Keycode.PERIOD)),
                key(13) + key(4): Action(OneShot(Keycode.GUI)),
                key(1) + key(8): Action(Press(Keycode.COMMA)),
                key(13) + key(8): Action(OneShot(Keycode.ALT)),
                key(1) + key(12): Action(Press(Keycode.FORWARD_SLASH)),
                key(13) + key(9) + key(5) + key(0): Action(OneShot(Keycode.SHIFT), Press(Keycode.SHIFT, False), hold=True),
                key(9) + key(8): Action(Press(Keycode.SHIFT, Keycode.ONE)), #Exclamation
                key(5) + key(4): Action(Lock(Keycode.SHIFT)),
                key(12) + key(8) + key(4) + key(0): Action(Press(Keycode.SPACE)),
                key(1) + key(12) + key(8) + key(4): Action(Press(Keycode.CAPS_LOCK)),
                key(5) + key(0): Action(Press(Keycode.BACKSPACE), hold=True),
                key(5) + key(8): Action(Press(Keycode.DELETE)),

                key(5) + key(8) + key(0): Action(ToLayer(5)),
                key(9) + key(1) + key(4): Action(ToLayer(6)),
            },
            (0, 0, 0)
        ),
        Layer(
            "Numbers",
            {
                key(13): Action(ToLayer(0)),
                key(1): Action(Press(Keycode.ONE)),
                key(5): Action(Press(Keycode.TWO)),
                key(9): Action(Press(Keycode.THREE)),
                key(0): Action(Press(Keycode.FOUR)),
                key(4): Action(Press(Keycode.FIVE)),
                key(8): Action(Press(Keycode.SIX)),
                key(5) + key(1): Action(Press(Keycode.SEVEN)),
                key(9) + key(5): Action(Press(Keycode.EIGHT)),
                key(4) + key(0): Action(Press(Keycode.NINE)),
                key(8) + key(4): Action(Press(Keycode.ZERO)),
            },
            (0, 64, 64)
        ),
        Layer(
            "Brackets",
            {
                key(1): Action(ToLayer(0)),
                key(13): Action(Press(Keycode.SHIFT, Keycode.RIGHT_BRACKET)),
                key(9): Action(Press(Keycode.SHIFT, Keycode.NINE)),
                key(5): Action(Press(Keycode.SHIFT, Keycode.ZERO)),
                key(12): Action(Press(Keycode.SHIFT, Keycode.LEFT_BRACKET)),
                key(8): Action(Press(Keycode.LEFT_BRACKET)),
                key(4): Action(Press(Keycode.RIGHT_BRACKET)),
            },
            (0, 0, 64)
        ),
        Layer(
            "Symbols",
            {
                key(13): Action(Press(Keycode.GRAVE_ACCENT)),
                key(9): Action(Press(Keycode.SEMICOLON)),
                key(5): Action(Press(Keycode.BACKSLASH)),
                key(1): Action(Press(Keycode.SHIFT, Keycode.ONE)),
                key(12): Action(Press(Keycode.EQUALS)),
                key(8): Action(Press(Keycode.MINUS)),
                key(4): Action(Press(Keycode.SHIFT, Keycode.FORWARD_SLASH)),
                key(0): Action(ToLayer(0)),
            },
            (64, 0, 64)
        ),
        Layer(
            "Extras",
            {
                key(9): Action(MediaPress(ConsumerControlCode.VOLUME_INCREMENT), hold=True),
                key(5): Action(Press(Keycode.INSERT)),
                key(1): Action(MediaPress(ConsumerControlCode.MUTE)),
                key(12): Action(ToLayer(0)),
                key(8): Action(MediaPress(ConsumerControlCode.VOLUME_DECREMENT), hold=True),
                key(4): Action(Press(Keycode.PRINT_SCREEN)),
                key(0): Action(Press(Keycode.RIGHT_SHIFT)),
            },
            (64, 0, 0)
        ),
        Layer(
            "Navigation",
            {
                key(13): Action(Press(Keycode.PAGE_UP)),
                key(9): Action(Press(Keycode.HOME)),
                key(5): Action(Press(Keycode.UP_ARROW), hold=True),
                key(1): Action(Press(Keycode.END)),
                key(12): Action(Press(Keycode.PAGE_DOWN)),
                key(8): Action(Press(Keycode.RIGHT_ARROW), hold=True),
                key(4): Action(Press(Keycode.DOWN_ARROW), hold=True),
                key(0): Action(Press(Keycode.LEFT_ARROW), hold=True),

                key(5) + key(8) + key(0): Action(ToLayer(0)),
            },
            (64, 64, 0)
        ),
        Layer(
            "Mouse",
            {
                key(13): Action(MouseMove(0, 0, -1), hold=True),
                key(9): Action(MousePress(Mouse.RIGHT_BUTTON)),
                key(5): Action(MouseMove(0, -8), hold=True),
                key(1): Action(MousePress(Mouse.LEFT_BUTTON)),
                key(12): Action(MouseMove(0, 0, 1), hold=True),
                key(8): Action(MouseMove(8, 0), hold=True),
                key(4): Action(MouseMove(0, 8), hold=True),
                key(0): Action(MouseMove(-8, 0), hold=True),
                key(9) + key(1) + key(4): Action(ToLayer(0)),
            },
            (0, 64, 0)
        ),
    ]
