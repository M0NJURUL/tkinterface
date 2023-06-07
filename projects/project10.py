# here we will learn about frame widget

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning frame widget")
root.iconbitmap("")

frame = LabelFrame(root, text="This is my new frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

# instead of root we will put the button in the frame
b = Button(frame, text="Don't Click Me")
b2 = Button(frame, text="Don't Click Me")
b3 = Button(frame, text="Don't Click Me")

# b.pack() # here we can also do grid inside a packed frame which is new and awesome :D
# lets try it
b.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=1)

root.mainloop()
