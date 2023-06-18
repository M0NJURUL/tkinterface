from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("")

pizza = StringVar()

MODES = [
    ("Cheese", "Cheese"),
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]
pizza.set(MODES[2][0])

def buttonClicked(mode):
    myLabel = Label(root, text=mode)
    myLabel.pack()

for text, value in MODES:
    Radiobutton(root, text=text, variable=pizza, value=value).pack(anchor=W)

myButton = Button(root, text="Order", command=lambda: buttonClicked(pizza.get()))
myButton.pack()

root.mainloop()
