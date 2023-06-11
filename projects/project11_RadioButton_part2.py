from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("")

anything = IntVar()

def buttonClicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=anything, value=1, command=lambda: buttonClicked(anything.get())).pack()
Radiobutton(root, text="Option 2", variable=anything, value=2, command=lambda: buttonClicked(anything.get())).pack()


myButton = Button(root, text="Click here", command=lambda: buttonClicked(anything.get()))
myButton.pack()

root.mainloop()
