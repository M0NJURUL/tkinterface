# here we will learn creating buttons

from tkinter import *

root = Tk()


# creating a function to make the button do something
# first try the button without function and the command parameter in myButton widget
def myClick():
    myLabel = Label(root, text="arigatou gozaimasu")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick)
# try passing these parameters
# state=DISABLED
# fg="blue", bg="red"
# padx=50, pady=50 -> adds padding to button text
# note: calling function with command parameter is a little different by default

myButton.pack()

root.mainloop()
