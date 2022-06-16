import pyautogui as ptgui
import time

ptgui.hotkey('win', '5')

i = 0

time.pause = 5

while (i < 500):
    ptgui.hotkey("ctrl", "v")
    ptgui.press("enter")
    i += 1