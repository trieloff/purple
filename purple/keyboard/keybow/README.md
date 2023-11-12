# Keyboard Layout

![Alt text](https://cdn.mos.cms.futurecdn.net/Zx8ZqmAfvKMU4vMxW2dx4g-1200-80.jpg.webp)

# Usage

Use this `code.py`

```python
# This is a simple example code.py file, you will want to
# customize it for your own keyboard.

from purple.core import Core

# Import the keyboard and layout you are using here.
from purple.keyboard.keybow.keyboard import Keyboard
from purple.keyboard.keybow.layout.artsey import Layout

# Import any extras you would like to use here.
from purple.extras.hardware.led import LED
from purple.extras.performance_counter import PerformanceCounter

# Create a new Core object with your keyboard, layout, and any
# extras, and then call run()
Core(Keyboard, Layout, LED(), PerformanceCounter()).run()
```