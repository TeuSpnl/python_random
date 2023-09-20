import pyautogui as ptgui
from time import sleep

ptgui.hotkey('win', '0')

i = 0

# sleep(.5)
# ptgui.click(1060, 700)
# sleep(1)
# ptgui.click(985, 260)
# sleep(1)

while (i < 300):
    # sleep(.15)
    # ptgui.click(855, 325)
    ptgui.hotkey('ctrl', 'v')
    sleep(.25)
    ptgui.press("enter")

    
    i += 1