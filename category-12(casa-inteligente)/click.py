import pyautogui
import time
from time import sleep

def Move(x, y):
    pyautogui.moveTo(x, y)
    sleep(5)

def Click(x, y):
    pyautogui.moveTo(x, y)
    sleep(1)
    pyautogui.doubleClick()
    sleep(2)
    pyautogui.leftClick()
    sleep(2)

while True:
    Click(500, 400)
    Move(100, 200)
    Move(600, 800)
    Move(1100, 300)
    Move(400, 200)
    Move(600, 700)
    