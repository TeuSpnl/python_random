import pyautogui as ptgui
import time

ptgui.hotkey('win', '7
             ')

i = 0

while (i < 500):
    ptgui.hotkey("crtl", "v")
    ptgui.press("enter")
    i += 1