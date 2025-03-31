import customtkinter as ctk
import macro

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Vanguards Macros")
        self.geometry("700x500")
        self.resizable(False,False)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)

        self.sideBarFrame = ctk.CTkFrame(master=self,width=150,corner_radius=0)
        self.sideBarFrame.grid(sticky="nesw",column=0,row=0)
        self.mainFrame = ctk.CTkFrame(master=self,width=500,corner_radius=0,fg_color=("gray75", "gray25"))
        self.mainFrame.grid(sticky="news",column=1,row=0)
        self.macroMaker = None

        #---------Frames----------#
        self.macroFrame = macroFrame(self)
        self.webhookFrame = webhookFrame(self)
        self.creatorFrame = creatorFrame(self)
        self.settingFrame = settingFrame(self)
        self.infoFrame = infoFrame(self)



        #------------ SideBar -------------#
        self.sideBarFrame.rowconfigure(6, weight=1)


        self.sideBarLabel = ctk.CTkLabel(master=self.sideBarFrame,text="Sidebar",font=ctk.CTkFont(size=30))
        self.sideBarLabel.grid(row=0,column=0, padx=20, pady=10)
        self.macroButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Macro", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("macro"),font=ctk.CTkFont(size=25))
        self.macroButton.grid(row=1,column=0, sticky="ew")
        self.webhookButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Webhook", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("webhook"),font=ctk.CTkFont(size=25))
        self.webhookButton.grid(row=2,column=0, sticky="ew")
        self.creatorButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Creator", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("creator"),font=ctk.CTkFont(size=25))
        self.creatorButton.grid(row=3,column=0, sticky="ew")
        self.settingsButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Settings", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("setting"),font=ctk.CTkFont(size=25))
        self.settingsButton.grid(row=4,column=0, sticky="ew")
        self.infoButton = ctk.CTkButton(master=self.sideBarFrame, corner_radius=0, text="Info", border_spacing=10, height=40,
                                        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=lambda : self.select_frame_by_name("info"),font=ctk.CTkFont(size=25))
        self.infoButton.grid(row=5,column=0, sticky="ew")
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sideBarFrame, values=["System", "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        self.select_frame_by_name("macro")
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.macroButton.configure(fg_color=("gray75", "gray25") if name == "macro" else "transparent")
        self.webhookButton.configure(fg_color=("gray75", "gray25") if name == "webhook" else "transparent")
        self.creatorButton.configure(fg_color=("gray75", "gray25") if name == "creator" else "transparent")
        self.settingsButton.configure(fg_color=("gray75", "gray25") if name == "setting" else "transparent")
        self.infoButton.configure(fg_color=("gray75", "gray25") if name == "info" else "transparent")

        # show selected frame
        if name == "macro":
            self.macroFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.macroFrame.grid_forget()
        if name == "webhook":
            self.webhookFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.webhookFrame.grid_forget()
        if name == "creator":
            self.creatorFrame.grid(row=0, column=1, sticky="nesw")
        else:
            self.creatorFrame.grid_forget()
        if name == "setting":
            self.settingFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settingFrame.grid_forget()
        if name == "info":
            self.infoFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.infoFrame.grid_forget()
        
    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        

class macroFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.configure(width=500, height=500)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="MACROFRAME")
        self.label.grid(row=0,column=0,sticky="nesw")
    
class webhookFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.configure(width=500, height=500)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="WEBHOOK")
        self.label.grid(row=0,column=0,sticky="nesw")

class creatorFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.configure(width=500, height=500)
        self.rowconfigure((0,1,2,3,4),weight=1)
        self.columnconfigure((0,1,2,3,4),weight=1)
        self.grid_propagate(False)

        self.nameBox = ctk.CTkTextbox(master=self,activate_scrollbars=False,height=30,width=300)
        self.nameBox.grid(row=0,columnspan=3,column=0,pady=0)
        self.nameBox.insert(text="Macro name",index="0.0")
        self.startButton = ctk.CTkButton(master=self,text="Start recording",command=self.startBtnCallback,height=30)
        self.startButton.grid(row=0,column=4)
        self.actionFrame = ctk.CTkScrollableFrame(master=self,height=300)
        self.actionFrame.grid(row=1,sticky="ew",columnspan=5,padx=20)
        self.slotDropDownLabel = ctk.CTkLabel(master=self,text="Slot")
        self.slotDropDownLabel.grid(row=2,column=0)
        self.slotDropDown = ctk.CTkOptionMenu(master=self,values=["1","2","3","4","5","6"],width=100,command=self.slotDropDownCallBack)
        self.slotDropDown.grid(row=3,column=0,pady=(0,35))
        self.typeLabel = ctk.CTkLabel(master=self,text="Action type")
        self.typeLabel.grid(row=2,column=1)
        self.typeDropDown = ctk.CTkOptionMenu(master=self,values=["Place","Upgrade","Ability","Delete","Skip wave"],width=100)
        self.typeDropDown.grid(row=3,column=1,pady=(0,35))
        self.indexlabel = ctk.CTkLabel(master=self,text="Index")
        self.indexlabel.grid(row=2,column=2)
        self.indexDropDown = ctk.CTkOptionMenu(master=self,values=["N/A"],width=100)
        self.indexDropDown.grid(row=3,column=2,pady=(0,35))
        self.addActionBtn = ctk.CTkButton(master=self,text="Add action",height=50,command=self.actionBtnCallBack)
        self.addActionBtn.grid(row=2,rowspan=2,column=4,padx=(0,20),pady=(0,20))
    
    def startBtnCallback(self):
        if self.master.macroMaker != None:
            print("Stopping macro")
            self.master.macroMaker.stopMacro()
            self.master.macroMaker = None
            self.startButton.configure(text="Start recording")
            return
        self.master.macroMaker = macro.macroMaker(self.nameBox.get("0.0",None))
        self.startButton.configure(text="Stop Recording")

    def slotDropDownCallBack(self,value):
        if self.master.macroMaker == None:
            print("Stopped")
            return
        index = 1
        indexs = []
        length = self.master.macroMaker.getCharIndex(value)
        if length == 0:
            self.indexDropDown.configure(values=["N/A"])
            return
        for x in range(length):
            indexs.append(str(index))
            index += 1
        self.indexDropDown.configure(values=indexs)
        return

    def actionBtnCallBack(self):
        self.master.macroMaker.addAction(self.slotDropDown.get(),self.indexDropDown.get(),self.typeDropDown.get())
        self.actionFrame = ctk.CTkFrame(master=self.actionFrame,corner_radius=0,bg_color="transparent")
        self.actionFrame.grid_columnconfigure((0,1,2,3),weight=1)
        print(self.actionFrame)
        self.actionTypeLabel = ctk.CTkLabel(master=self.actionFrame,text=self.typeDropDown.get())


class settingFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.configure(width=500, height=500)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="Settings")
        self.label.grid(row=0,column=0,sticky="nesw")

class infoFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._corner_radius = 0
        self._fg_color = "transparent"
        self.configure(width=500, height=500)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.label = ctk.CTkLabel(master=self,text="Developed independently by @atratochoana")
        self.label.grid(row=0,column=0,sticky="nesw")

app = App()
app.mainloop()

