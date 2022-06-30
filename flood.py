import pyautogui as ptgui
import time

ptgui.hotkey('win', '3')

i = 0

time.pause = 5

while (i < 150):
    ptgui.press("f2")
    ptgui.press("end")
    ptgui.press("backspace")
    ptgui.press("v")
    ptgui.press("enter")
    ptgui.press("enter")
    ptgui.press("down")
    i += 1