from tkinter import *

class FrameMethods:
    def __int__(self):
        pass

    def TrqControlClicker(self):
        self.SpdControl.config(bg='white')
        self.TrqControl.config(bg='red')
    def SpdControlClicker(self):
        self.SpdControl.config(bg='red')
        self.TrqControl.config(bg='white')
    def reqEnableClicker(self):
        self.reqEnable.config(bg='green')
        self.reqDisable.config(bg='white')
    def reqDisableClicker(self):
        self.reqDisable.config(bg='green')
        self.reqEnable.config(bg='white')

class BasicFrame(Frame,FrameMethods):
    def __init__(self,master):
        Frame.__init__(self)
        #FrameMethods.__init__(self)

        self.CtrlModeText = Label(self,text='Enter control mode:')
        self.CtrlModeText.grid(row=0,column=0)

        self.TrqControl = Button(self,text='Torque control',command=self.TrqControlClicker)
        self.TrqControl.grid(row=0,column = 1,padx=20)

        self.SpdControl = Button(self,text='Speed control',command=self.SpdControlClicker)
        self.SpdControl.grid(row=0,column=2,padx=20)

        self.reqEnableText = Label(self,text='Enable/Disable MCU:')
        self.reqEnableText.grid(row=1,column=0,pady=20)

        self.reqEnable = Button(self,text='Enable MCU',command=self.reqEnableClicker)
        self.reqEnable.grid(row=1,column=1,padx=20)

        self.reqDisable = Button(self,text='Disable MCU',command=self.reqDisableClicker)
        self.reqDisable.grid(row=1,column=2,padx=20)







