from ahk import AHK
ahk = AHK()
from time import sleep

def upgrade():
    ahk.win_activate("Roblox")
    ahk.mouse_move(200,390)
    ahk.click()


def retry():
    ahk.win_activate("Roblox")
    ahk.mouse_move(588,486)
    ahk.click()

def skip():
    ahk.win_activate("Roblox")
    ahk.mouse_move(588,486)
    ahk.click()

def place(ypos,xpos,troop):
    ahk.win_activate("Roblox")
    ahk.mouse_move(ypos,xpos)
    ahk.click()

def start():
    for x in range(10):
        ahk.key_press("o")

def restart():
    ahk.win_activate("Roblox")
    ahk.mouse_move(27,609)
    ahk.click()
    ahk.mouse_move(613,314)
    ahk.click()
    ahk.mouse_move(429,348)
    ahk.click()
    ahk.mouse_move(486,339)
    ahk.click()
    ahk.mouse_move(670,146)
    ahk.click()
    
#retry()
def test():
    ahk.win_activate("Roblox")
    sleep(2)
    print(ahk.get_mouse_position())
#test()