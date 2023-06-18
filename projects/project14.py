# we will learn opening/selecting files with dialog box

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("root window")
root.iconbitmap("")

def choose():
    global my_image
    global imageLabel
    imageLabel.destroy()
    # this will return the file location
    filename = filedialog.askopenfilename(initialdir="/images", title="Choose Choose Choose", filetypes=(("PNG FILES", "*.png"), ("JPG FILES", "*.jpg")))

    # using the location to open file in root window
    my_image = ImageTk.PhotoImage(Image.open(filename))
    imageLabel = Label(root, image=my_image)
    imageLabel.pack()

imageLabel = Label(root)
my_image = 0
Button(root, text="Choose image to view", command=choose, padx=10, pady=10).pack(padx=10, pady=10)

root.mainloop()