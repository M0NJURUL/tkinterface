# we will learn making dropdowns now

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("dropdown")

selected = StringVar()
selected.set("Day")

options = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

d = OptionMenu(root, selected, *options)
d.pack()


root.mainloop()