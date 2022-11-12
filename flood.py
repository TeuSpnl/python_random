import pyautogui as ptgui
import time

ptgui.hotkey('win', '5')

i = 0

while (i < 67):
    ptgui.write("Mateus Spinola")
    ptgui.press("enter")
    i += 1
    ptgui.write("Daniel Spinola")
    ptgui.press("enter")
    i += 1
    ptgui.write("Tatiana Casas")
    ptgui.press("enter")
    i += 1