# we will learn creating new tkinter windows

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("root window")
root.iconbitmap("")

def chichingfak():
    top = Toplevel()
    top.title("new window")
    top.iconbitmap("")

    Label(top, text="hello there!").pack()

    Button(top, text="close window", command=top.quit).pack()

Button(root, text="Open second window", command=chichingfak).pack()


root.mainloop()
