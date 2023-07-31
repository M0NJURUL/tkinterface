# we will create checkboxes here

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("checkboxes")

def checkedOrNot():
    Label(root, text=var.get()).pack()

var = StringVar()

checkbox = Checkbutton(root, text="Check me!", variable=var, command=checkedOrNot, onvalue="On", offvalue="Off")
checkbox.deselect()
checkbox.pack()

root.mainloop()
