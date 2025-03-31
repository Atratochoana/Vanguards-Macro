from pyautogui import position,moveTo, click
from time import sleep

def getMousePos():
    currentMouseX, currentMouseY = position()

    return (currentMouseX, currentMouseY)

def moveMousePos(pos):
    moveTo(pos)
    click()


# sleep(5)
# print(getMousePos())
