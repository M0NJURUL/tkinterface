# here we will learn creating input fields

from tkinter import *

root = Tk()

# Input widget are created with Entry(parameters)
e = Entry(root, width=30, fg="red")
e.pack()

e.insert(0, "Senpai") # default text for the input box
e.insert(3, "x") # default text for the input box

def myClick():
    myLabel = Label(root, text="Arigatou gozaimasu, " + e.get())
    # e.get() fetches the input message and python concatenates it with a string
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()

root.mainloop()


