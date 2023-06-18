# here we will print simple text using pack

# importing everything inside tkinter library
# from tkinter import *
import tkinter

# everything in tkinter is a widget
# for example: button widget, text widget, frame widget

# in tkinter we always have 2 steps
# 1. create/define something - widget
# 2. making it ready to show it onto the screen
#       packing is one of the ways to make it ready

# this is root widget
root = tkinter.Tk()
# -> it creates the initial box window for graphical interface

# 1. creating a label widget
myLabel = tkinter.Label(root, text="Hello World!")
# -> more parameter we can pass (height=100, width=100)

# 2. packing to show it onto the screen
myLabel.pack()

# now we have to create a loop to track things happening on the screen
# and finally this will also bring up the screen
root.mainloop()
