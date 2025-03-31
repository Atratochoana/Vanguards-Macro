import mouse as mouse
import screen as screen
from time import sleep

def newScreenshot(name):

    sleep(3)

    mouse1 = mouse.getMousePos()
    print(mouse1)

    sleep(1.5)

    mouse2 = mouse.getMousePos()
    print(mouse2)

    screen.screenShot((mouse1[0],mouse1[1],mouse2[0],mouse2[1]),name)

newScreenshot("VictoryFull")





