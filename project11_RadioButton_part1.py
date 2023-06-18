# we will work with radio button here
# radio button works similarly to the old radio buttons
# when one is pressed all other buttons would pop out

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap("")

# tkinter variable is a little different from normal different

anything = IntVar() # calling IntVar() function because the value the variable will get is an integer
# anything.set(2) # this is to set the default options

# creating a function to check if my radio buttons are working fine
def buttonClicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=anything, value=1, command=lambda: buttonClicked(anything.get())).pack()
Radiobutton(root, text="Option 2", variable=anything, value=2, command=lambda: buttonClicked(anything.get())).pack()
# value=1, value=2 determines what value the variable will receive, this can be any value

# now creating a label to confirm the changes happening with radio buttons
# myLabel = Label(root, text=anything.get()) # anything.get() will receive the value for the variable whenever a radio button is clicked
# myLabel.pack()
# moved this set of code to function

myButton = Button(root, text="Click here", command=lambda: buttonClicked(anything.get()))
myButton.pack()

root.mainloop()
