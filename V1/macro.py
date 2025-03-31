from ahk import AHK
from time import sleep
#Idea for this is to decompile a txt file into a macro through having it have information based on then action, specific for vanguards

#example input [1-6 for slot][Index of that slot][Action][Sleep time from previous task];
# [Slot] if 0 will mean the action is not character related otherwise is self explainitory
# [Index] this is also self explanatory, if the slot is 0 it doesnt matter
# [Action] this will be one letter such as "u" for upgrade or "r" for restart
# [Sleep] this will just a time from between the last task and this one
# [End] will end in a ; to indicate the difference between the sleep time and slot
# end product could look something like this ;30u15 this means, slot 3 index 0 upgrade after sleeping 15 seconds
# character locations will be at the start and be based on this format: [{slot}:{x coords}:{1 coords}&]=
# example for character location is &2:500:500:&2:600:600:

ahk = AHK()

def find(string, char):
    return [i for i, ltr in enumerate(string) if ltr == char]

def find_indices(string, chars):
    return [[i for i, ltr in enumerate(string) if ltr == char] for char in chars]

def decompile(filePath: str):
    """Takes a macro filepath (custom .txt) and then will execute the macro, will not stop unless manually done or through ending task or something"""

    with open(filePath,"r") as f:
        string = f.read()
    
    actions = []
    chars = []
    characters = [[],[],[],[],[],[]]

    indices = find_indices(string,[":",";"])
    for x in range(int(len(indices[0])/4)):
        chars.append(string[indices[0][int(4*(x))]:indices[0][(int(4*(x))+3)]+1])

    for x in range(int(len(indices[1])/2)):
        actions.append(string[indices[1][int(2*(x))]:indices[1][(int(2*(x))+1)]+1])

    for c in chars:
        colonIndex = find(c,":")
        characters[int(c[1])].append([int(c[colonIndex[1]+1:colonIndex[2]]),int(c[colonIndex[2]+1:len(c)-1])])

    for action in actions:
        ahk.find_window(title="Roblox").activate()
        if int(action[4]) != 0:
            sleep(int(action[4:int(len(action))-1]))
            print("Finished sleeping")
        if int(action[1]) >= 1:
            ahk.click(characters[int(action[1])][int(action[2])][0],characters[int(action[1])][int(action[2])][1])
            print("Clicked on char")
        if action[3] == "u": #U is for upgrade, and assumes that click has happened already
            ahk.key_press("t")
            print("Upgraded")
        if action[3] == "r": #retry for fullscreen, slot should be 0, althought doesnt matter
            for x in range(10):
                ahk.click(x=1175, y=816)
            print("Retried")
        if action[3] == "s": #skip for fullscreen
            ahk.click(x=899, y=192)
        if action[3] == "q": #resets character to spawn
            ahk.click(x=40, y=1004)
            ahk.click(x=1194, y=363)
            ahk.click(x=1287, y=224)
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
            ahk.click(button="wheeldown")
        

class macroMaker():
    def __init__(self,name):
        self.characters = [[],[],[],[],[],[]]
        self.actions = []
        print(f"Created {name}.macro")

    def addAction(self,slot,index,type):
        print(f"{slot},{index},{type}")
        #"Place","Upgrade","Ability","Delete","Skip wave"
        slot = int(slot)-1
        if type == "Place":
            sleep(2)
            mousePos = ahk.get_mouse_position()
            self.characters[slot].append([mousePos[0],mousePos[1]])
            #print(f"&{slot}:{mousePos[0]}:{mousePos[1]}:")
        elif type == "Upgrade":
            print("Upgraded")
            ahk.click(x=self.characters[slot][int(index)-1][0],y=(self.characters[slot][int(index)-1][1]-10))
            ahk.key_press("t")
        elif type == "Ability":
            ahk.click(x=self.characters[slot][int(index)-1][0],y=(self.characters[slot][int(index)-1][1]-10))
            ahk.click(x=3066, y=807)
        elif type == "Delete":
            ahk.click(x=self.characters[slot][int(index)-1][0],y=(self.characters[slot][int(index)-1][1]-10))
            ahk.key_press("x")
        elif type == "Skip wave":
            pass

    def getCharIndex(self,char):
        """Char is the index of the character you want
        Returns len(char)"""
        return len(self.characters[int(char)-1])
    
    def stopMacro(self):
        return


#decompile("src\macros/test.txt")