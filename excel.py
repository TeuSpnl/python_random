from turtle import position
import pyautogui as ptgui
import time

resp = int(input("Qual opção você quer? "))
pos = 70 + (50 * resp)

i = 0
j = 1

ptgui.hotkey('win', '7')

ptgui.PAUSE = .5

# ptgui.moveTo(1085, 81)

while(i < 3):
    ptgui.hotkey("ctrl", "1")
    ptgui.click(1085, 81)
    ptgui.click(1025, pos)
    ptgui.scroll(-100)
    ptgui.click(530, 173)
    ptgui.click(530, 369)
    ptgui.click(1086, 587)

    l = j
    while j < l + 5:
        for t in range(j):
            ptgui.press("down")
        ptgui.press("enter")
        
        ptgui.moveTo(512,250)
        ptgui.scroll(500 * j)
        ptgui.click(512, 280)
        
        j += 1

    ptgui.click(782, 520)
    
    i += 1

# time.sleep(3)
# print(ptgui.position())
# time.sleep(3)
# print(ptgui.position())