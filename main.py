#Main script

from GUIclass.GUIclass import RigGui
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title('Rig GUI')
    root.geometry('700x350')
    R1 = RigGui(root)
    root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
