# here we will print texts using grid

from tkinter import *
root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Everything okay?")
myLabel3 = Label(root, text="Bye World!")

# 2. using grid to show it onto the screen
# grid will help us keep our widgets based on rows and columns
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=3)
# and of course computer starts counting from 0

# and these rows and columns are relative
# so every row and column must have 'something' to visualize the gaps on between
# try changing the column to 10 for myLabel3 to understand more clearly

root.mainloop()
