#Main script

from GUIclass.GUIclass import BasicFrame
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title('GUI')
    root.geometry('700x700')
    R1 = BasicFrame(root)
    R1.grid(row=0,column=0)
    root.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
