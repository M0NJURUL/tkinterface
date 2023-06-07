# here we will add status bar in the image viewer application
# and make sure that we don't have to grab those images one by one

from tkinter import *

root = Tk()
root.title("PNG Gallery")
root.iconbitmap("images/icons/64x64_project8.ico")

button_quit = Button(root, text="Exit", command=root.quit)

my_png0 = PhotoImage(file="PNG Gallery_project8/underweight.png")
my_png1 = PhotoImage(file="PNG Gallery_project8/normal.png")
my_png2 = PhotoImage(file="PNG Gallery_project8/overweight.png")
my_png3 = PhotoImage(file="PNG Gallery_project8/obese.png")

png_list = [my_png0, my_png1, my_png2, my_png3]

# new label being created here
status = Label(root, text=f"Image {1} of {len(png_list)}", relief="sunken", anchor=E)
# relief and anchor parameter added sunken property to the widget
# try these in relief -> "raised", "sunken", "flat", "ridge", "solid", "groove"
# anchor sets the direction of the label element

imageLabel = Label(image=my_png0)
imageLabel.grid(row=0, column=0, columnspan=3)

def previous(index):
    global imageLabel, previous_button, next_button, status

    imageLabel.destroy()
    previous_button.destroy()
    next_button.destroy()
    status.destroy()

    imageLabel = Label(image=png_list[index])
    imageLabel.grid(row=0, column=0, columnspan=3)

    previous_button = Button(root, text="<< Previous", command=lambda: previous(index - 1))
    next_button = Button(root, text="Next >>", command=lambda: nexxt(index + 1))

    if index == 0:
        previous_button = Button(root, text="<< Previous", command=lambda: previous, state=DISABLED)

    previous_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    # here status label will be updated with the forwarded button, same in the nexxt function
    status = Label(root, text=f"Image {index+1} of {len(png_list)}", relief="sunken", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def nexxt(index):
    global imageLabel, previous_button, next_button, status

    imageLabel.destroy()
    previous_button.destroy()
    next_button.destroy()
    status.destroy()

    imageLabel = Label(image=png_list[index])
    imageLabel.grid(row=0, column=0, columnspan=3)

    previous_button = Button(root, text="<< Previous", command=lambda: previous(index - 1))
    next_button = Button(root, text="Next >>", command=lambda: nexxt(index + 1))

    if index == 3:
        next_button = Button(root, text="Next >>", state=DISABLED)

    previous_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)

    status = Label(root, text=f"Image {index+1} of {len(png_list)}", relief="sunken", anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

previous_button = Button(root, text="<< Previous", command=lambda: previous, state=DISABLED)
quit_button = Button(root, text="Exit", command=root.quit)
next_button = Button(root, text="Next >>", command=lambda: nexxt(1))

previous_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1, pady=10) # given pady to grid move the status bar a little down
next_button.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E) # sticky stretches in directions WEST+EAST

root.mainloop()


