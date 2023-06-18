from tkinter import *
from PIL import ImageTk, Image

root = Tk()
imageLabel = Label(root)
def showImage():
    global imageLabel, my_image
    my_image = ImageTk.PhotoImage(Image.open("images/obese.png"))
    imageLabel = Label(root, image=my_image)
    imageLabel.pack()

Button(root, text="Show image", command=showImage).pack()

root.mainloop()