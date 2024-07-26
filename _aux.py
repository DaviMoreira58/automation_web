''' Its purpose is to identify the position of the mouse on the display screen so that we can pass the coordinates into the program. '''

import pyautogui
import time


time.sleep(5)
print(pyautogui.position())