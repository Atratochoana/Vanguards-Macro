from ahk import AHK
from webhook import editWebhook
from time import sleep

ahk = AHK()
#This is a macro for mountain shrine act 3, (Raid stages), when game is fullscreen

#webhook = None

characters = {
    "1": [[989,496],[885,494],[820,493]], #speedwagon
    "2": [[1584,594]], #toji
    "3": [[1412,515],[1366,510],[1748, 952]], #vegita
    "4": [],
    "5": [[1525,568]], #gojo
    "6": []
}

def spawn():
    ahk.find_window(title="Roblox").activate()
    ahk.click(x=40, y=1004)
    ahk.click(x=1194, y=363)
    ahk.click(x=1287, y=224)
    ahk.click(button="wheeldown")
    ahk.click(button="wheeldown")
    ahk.click(button="wheeldown")
    ahk.click(button="wheeldown")
    ahk.click(button="wheeldown")
    ahk.click(button="wheeldown")

def upgrade(slot,index):
    ahk.click(x=characters[slot][index][0],y=(characters[slot][index][1]-10))
    ahk.key_press("t")

def place(slot,index):
    ahk.key_press(slot)
    ahk.click(x=characters[slot][index][0],y=characters[slot][index][1])

def retry():
    for x in range(10):
        ahk.click(x=1175, y=816)

def skip():
    ahk.click(x=899, y=192)

def ability(slot,index):
    ahk.click(x=characters[slot][index][0],y=(characters[slot][index][1]-10))
    ahk.click(x=3066, y=807)
    
def run():
    task = 0
    global contin
    contin = True
    print("Started")
    while contin:
        if task == 0: #starts by retrying and going to spawn, then places first speedwagon
            print(task)
            retry()
            spawn()
            sleep(3)
            skip()
            sleep(0.5)
            place("1",0)
            task += 1
            sleep(20)
        elif task == 1: #places second speed wagon
            print(task)
            place("1",1)
            task += 1
            sleep(5)
        elif task == 2: #places third speed wagon
            print(task)
            place("1",2)
            task += 1
            sleep(14)
        elif task == 3: #upgrades first speed wagon to lvl 1
            print(task)
            upgrade("1",0)
            task += 1
            sleep(9)
        elif task == 4: #places first vegita
            print(task)
            place("3",0)
            task += 1
            sleep(11)
        elif task == 5: #upgrades second speedwagon to lvl 1
            print(task)
            upgrade("1",1)
            task += 1
            sleep(5)
        elif task == 6: #upgrades third speedwagon to lvl 1 and places second vegita
            print(task)
            upgrade("1",2)
            place("3",1)
            task += 1
            sleep(18)
        elif task == 7: #upgrades first speed wagon to lvl 2
            print(task)
            upgrade("1",0)
            task += 1
            sleep(4)
        elif task == 8: #upgrades second speedwagon to lvl 3
            print(task)
            upgrade("1",1)
            upgrade("1",1)
            task += 1
            sleep(12)
        elif task == 9: #upgrades third speedwagon to lvl 2
            print(task)
            upgrade("1",2)
            task += 1
            sleep(6)
        elif task == 10: #upgrades first speedwagon to lvl max
            print(task)
            upgrade("1",0)
            task += 1
            sleep(3)
        elif task == 11: #upgrades second speedwagon to max
            print(task)
            upgrade("1",1)
            task += 1
            sleep(16)
        elif task == 12: #upgrades third speedwagon to 3
            print(task)
            upgrade("1",2)
            upgrade("1",1)
            task += 1
            sleep(15)
        elif task == 13: #upgrades first speedwagon to max
            print(task)
            upgrade("1",0)
            sleep(3)
            place("5",0)
            task += 1
            sleep(2)
        elif task == 14: #places first gojo
            print(task)
            upgrade("1",2)
            upgrade("5",0)
            task += 1
            sleep(14)
        elif task == 15: #upgrades 
            print(task)
            upgrade("5",0)
            place("2",0)
            task += 1
            sleep(4)
        elif task == 16: #upgrades 
            print(task)
            upgrade("2",0)
            upgrade("2",0)
            upgrade("2",0)
            task += 1
            sleep(16)
        elif task == 17: #upgrades 
            print(task)
            place("3",2)
            upgrade("3",2)
            task += 1
            sleep(5)
        elif task == 18: #upgrades 
            print(task)
            upgrade("3",2)
            upgrade("3",2)
            task += 1
            sleep(5)
        elif task == 19: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(15)
        elif task == 20: #upgrades 
            print(task)
            upgrade("5",0)
            upgrade("5",0)
            task += 1
            sleep(15)
        elif task == 21: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(5)
        elif task == 22: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(20)
        elif task == 23: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(20)
        elif task == 24: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(20)
        elif task == 25: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(30)
        elif task == 26: #upgrades 
            print(task)
            upgrade("5",0)
            task += 1
            sleep(10)
        elif task == 27: #upgrades 
            print(task)
            upgrade("2",0)
            upgrade("2",0)
            task += 1
            sleep(20)
        elif task == 28: #upgrades 
            print(task)
            upgrade("2",0)
            upgrade("2",0)
            task += 1
            sleep(20)
        elif task == 29: #upgrades 
            print(task)
            upgrade("2",0)
            task += 1
            sleep(20)
        elif task == 30: #upgrades 
            print(task)
            upgrade("2",0)
            upgrade("2",0)
            task += 1
            sleep(60)
        elif task == 31:
            print(task)
            ability("5",0)
            print("Done")
            task += 1
            #webhook = editWebhook(webhook)
        elif task == 32:
            sleep(1)
            ahk.click()
            #end()
            print("ended")


def end():
    global contin
    contin = False
    print("Force stopped")

def getCoords():
    print(ahk.mouse_position)


# contin = True
# ahk.add_hotkey("r",run)
# ahk.add_hotkey("e",end)
# ahk.add_hotkey("q",getCoords)
# ahk.start_hotkeys()
# ahk.block_forever()

