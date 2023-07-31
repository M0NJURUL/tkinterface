# we will work with sliders

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("slider")

def resize():
    # Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=500) # default orient VERTICAL
vertical.pack()

horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)
horizontal.pack()

Button(root, text="click me to resize window", command=resize).pack()




root.mainloop()