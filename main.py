#Main script

from GUIclass.GUIclass import RigGui
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title('Rig GUI')
    root.geometry('700x700')
    R1 = RigGui(root)
    R1.grid(row=0,column=0)
    root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
