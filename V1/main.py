import multiprocessing.process
from screen import screenShot
from compareImage import ImageComparer
import Vanguards
from time import sleep
import json
import pyautogui
from webhook import editWebhook
import macros.mountainShrineAct3 as mountainShrine3
import threading
import multiprocessing

#tinyTaskSlots = [(1094, 22),(1364, 22),(1638, 22),(1640, 112),(1362, 112),(1098, 112),(1098, 204)]
# Global variables
ran = 0
failed = 0
ended = False
process = None

# Load JSON data
with open(r"src/positions/comparisons.json", "r") as f:
    checks = json.load(f)
with open(r"src/positions/misc.json", "r") as f:
    misc = json.load(f)

def run(event):
    global process, ran, failed  # Declare global variables
    if process is not None:
        process.terminate()
        process.join()
    process = multiprocessing.Process(target=mountainShrine3.run)
    process.start()
    if event == "FailedFull":
        failed += 1
        ran += 1
        editWebhook(None, ran, failed)
    elif event == "VictoryFull":
        ran += 1
        editWebhook(None, ran, failed)
    sleep(10)

def mainloop():
    global process
    while not ended:  # Avoid comparing `== False`
        if process is None:
            print("Created process")
            process = multiprocessing.Process(target=mountainShrine3.run)
            process.start()  # Start the process
            sleep(5)

        for check in checks:
            #print(check, end=": ")
            check_list = checks[check]
            screenShot(check_list[0], f"temp/{check}")
            if ImageComparer(f"Screenshots/temp/{check}.png", check_list[1]) >= 0.75:
                run(check)
        sleep(1)

# To start the mainloop, ensure this is within the proper script entry point
if __name__ == "__main__":
    mainloop()