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
  keys = [
    Key(DigitalInOut(board.KEY0)),  # 0
    Key(DigitalInOut(board.KEY1)),  # 1
    Key(DigitalInOut(board.KEY2)),  # 2
    Key(DigitalInOut(board.KEY3)),  # 3
    Key(DigitalInOut(board.KEY4)),  # 4
    Key(DigitalInOut(board.KEY5)),  # 5
    Key(DigitalInOut(board.KEY6)),  # 6
    Key(DigitalInOut(board.KEY7)),  # 7
    Key(DigitalInOut(board.KEY8)),  # 8
    Key(DigitalInOut(board.KEY9)),  # 9
    Key(DigitalInOut(board.KEY10)),  # 10
    Key(DigitalInOut(board.KEY11)),  # 11
    Key(DigitalInOut(board.KEY12)),  # 12
    Key(DigitalInOut(board.KEY13)),  # 13
    Key(DigitalInOut(board.KEY14)),  # 14
    Key(DigitalInOut(board.KEY15)),  # 15
  ]