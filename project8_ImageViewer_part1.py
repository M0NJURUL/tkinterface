# here we will build our own image viewer application

from tkinter import *

root = Tk()
root.title("PNG Gallery")
root.iconbitmap("images/icons/64x64_project8.ico")

# testing_image = PhotoImage(file="PNG Gallery_project8/overweight.png")

# jpg and some other formats of image are not supported in tkinter PhotoImage
# for that we have to use pillow.
# that would look something like this:
# from PIL import ImageTk, Image
# testing_image = ImageTk.PhotoImage(Image.open("images_for_image_viewer_app_project8/file_name.jpg"))

# imageLabel = Label(image=testing_image)
# imageLabel.pack()

# creating our own exit button for the image viewer
button_quit = Button(root, text="Exit", command=root.quit)

# button_quit.pack()

my_png0 = PhotoImage(file="PNG Gallery_project8/underweight.png")
my_png1 = PhotoImage(file="PNG Gallery_project8/normal.png")
my_png2 = PhotoImage(file="PNG Gallery_project8/overweight.png")
my_png3 = PhotoImage(file="PNG Gallery_project8/obese.png")

png_list = [my_png0, my_png1, my_png2, my_png3]

imageLabel = Label(image=my_png0)
imageLabel.grid(row=0, column=0, columnspan=3)

def previous(index):
    global imageLabel
    global previous_button
    global next_button

    imageLabel.destroy()
    previous_button.destroy()
    next_button.destroy()

    imageLabel = Label(image=png_list[index])
    imageLabel.grid(row=0, column=0, columnspan=3)

    previous_button = Button(root, text="<< Previous", command=lambda: previous(index - 1))
    next_button = Button(root, text="Next >>", command=lambda: nexxt(index + 1))

    if index == 0:
        previous_button = Button(root, text="<< Previous", command=lambda: previous, state=DISABLED)

    previous_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

def nexxt(index):
    global imageLabel
    global previous_button
    global next_button

    imageLabel.destroy()
    previous_button.destroy()
    next_button.destroy()

    imageLabel = Label(image=png_list[index])
    imageLabel.grid(row=0, column=0, columnspan=3)

    previous_button = Button(root, text="<< Previous", command=lambda: previous(index - 1))
    next_button = Button(root, text="Next >>", command=lambda: nexxt(index + 1))

    if index == 3:
        next_button = Button(root, text="Next >>", state=DISABLED)

    previous_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

previous_button = Button(root, text="<< Previous", command=lambda: previous, state=DISABLED)
quit_button = Button(root, text="Exit", command=root.quit)
next_button = Button(root, text="Next >>", command=lambda: nexxt(1))

previous_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
next_button.grid(row=1, column=2)

root.mainloop()
# i can edit yee


