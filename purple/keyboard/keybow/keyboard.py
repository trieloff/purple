import board
from digitalio import DigitalInOut

from purple.key import Key

# Keys
#
#  3  7  11  15
#  2  6  10  14
#  1  5  9   13
#  0  4  8   12
#

class Keyboard:
  name = "Pimoroni Keybow 2040"
  def __init__(self, keybow):
    self._keybow = keybow
    self._keys = keybow.keys
    keys = [
      Key(keybow.keys[0].switch),
      Key(keybow.keys[1].switch),
      Key(keybow.keys[2].switch),
      Key(keybow.keys[3].switch),
      Key(keybow.keys[4].switch),
      Key(keybow.keys[5].switch),
      Key(keybow.keys[6].switch),
      Key(keybow.keys[7].switch),
      Key(keybow.keys[8].switch),
      Key(keybow.keys[9].switch),
      Key(keybow.keys[10].switch),
      Key(keybow.keys[11].switch),
      Key(keybow.keys[12].switch),
      Key(keybow.keys[13].switch),
      Key(keybow.keys[14].switch),
      Key(keybow.keys[15].switch)
    ]