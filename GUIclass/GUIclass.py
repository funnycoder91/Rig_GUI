from tkinter import *

class RigGui:
    def __init__(self,master):
        self.myFrame = Frame(master)
        self.myFrame.pack()

        self.reqEnableText = Label(self.myFrame,text='Enable/Disable MCU',fg='Black',bg='White')
        self.reqEnableText.grid(row=0,column=0)

        self.reqEnable = Button(self.myFrame,text='Enable MCU',command=self.clicker)
        self.reqEnable.grid(row=0,column=1,padx=80)

        self.reqDisable = Button(self.myFrame,text='Disable MCU',command=self.clicker)
        self.reqDisable.grid(row=0,column=2,padx=10)


    def clicker(self):
        print("Button clicked!")



