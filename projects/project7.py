# trying out canvas widget

# import turtle
from tkinter import *
root = Tk()

myCanvas = Canvas(root, height=300, width=300, bg="black")

myCanvas.create_line(50, 100, 100, 100, fill="white")
myCanvas.create_line(50, 100, 50, 150, fill="white")
myCanvas.create_line(50, 150, 100, 150, fill="white")
myCanvas.create_line(100, 100, 100, 150, fill="white")

myCanvas.create_rectangle(150, 100, 200, 150, outline="red")
# myCanvas.create_polygon()

myCanvas.pack()

root.mainloop()



