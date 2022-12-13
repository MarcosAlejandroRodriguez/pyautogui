import pyautogui as p 
import time as t 
msg = str(input("type your msg here "))
for i in range (100):
    p.write(msg)
    p.press('Enter')
    t.sleep(1)

    