from tkinter import *

class RigGui:
    def __init__(self,master):
        self.myFrame = Frame(master)
        self.myFrame.pack()

        self.CtrlModeText = Label(self.myFrame,text='Enter control mode')
        self.CtrlModeText.grid(row=0,column=0)

        self.TrqControl = Button(self.myFrame,text='Torque control')
        self.TrqControl.grid(row=0,column = 1,padx=80)

        self.SpdControl = Button(self.myFrame,text='Speed control')
        self.SpdControl.grid(row=0,column=2,padx=80)

        self.reqEnableText = Label(self.myFrame,text='Enable/Disable MCU')
        self.reqEnableText.grid(row=1,column=0,pady=20)

        self.reqEnable = Button(self.myFrame,text='Enable MCU',command=self.clicker)
        self.reqEnable.grid(row=1,column=1,padx=80)

        self.reqDisable = Button(self.myFrame,text='Disable MCU',command=self.clicker)
        self.reqDisable.grid(row=1,column=2,padx=10)

    def clicker(self):
        print("Button clicked!")



