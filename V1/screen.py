from PIL import ImageGrab
from time import sleep
import mouse as mouse


def screenShot(bbox=None,name="Screenshot"):
    # Capture the entire screen
    screenshot = ImageGrab.grab(bbox)

    # Save the screenshot to a file
    screenshot.save(f"Screenshots/{name}.png")

    # Close the screenshot
    screenshot.close()

def newScreenshot(name):

    sleep(3)

    mouse1 = mouse.getMousePos()
    print(mouse1)

    sleep(1.5)

    mouse2 = mouse.getMousePos()
    print(mouse2)

    screenShot((mouse1[0],mouse1[1],mouse2[0],mouse2[1]),name)

newScreenshot("VictoryFull")

# sleep(2)
#screenShot((557, 222,815, 275))