from tkinter import *

class RigGui:
    def __init__(self,master,side):
        self.myFrame = Frame(master)
        self.myFrame.pack(side=side)

        self.CtrlModeText = Label(self.myFrame,text='Enter control mode:')
        self.CtrlModeText.grid(row=0,column=0)

        self.TrqControl = Button(self.myFrame,text='Torque control',command=self.TrqControlClicker)
        self.TrqControl.grid(row=0,column = 1,padx=20)

        self.SpdControl = Button(self.myFrame,text='Speed control',command=self.SpdControlClicker)
        self.SpdControl.grid(row=0,column=2,padx=20)

        self.reqEnableText = Label(self.myFrame,text='Enable/Disable MCU:')
        self.reqEnableText.grid(row=1,column=0,pady=20)

        self.reqEnable = Button(self.myFrame,text='Enable MCU',command=self.reqEnableClicker)
        self.reqEnable.grid(row=1,column=1,padx=20)

        self.reqDisable = Button(self.myFrame,text='Disable MCU',command=self.reqDisableClicker)
        self.reqDisable.grid(row=1,column=2,padx=20)

    def TrqControlClicker(self):
        self.TrqControl.config(bg='red')
        self.SpdControl.config(bg='white')

    def SpdControlClicker(self):
        self.SpdControl.config(bg='red')
        self.TrqControl.config(bg='white')

    def reqEnableClicker(self):
        self.reqEnable.config(bg='green')
        self.reqDisable.config(bg='white')

    def reqDisableClicker(self):
        self.reqDisable.config(bg='green')
        self.reqEnable.config(bg='white')





