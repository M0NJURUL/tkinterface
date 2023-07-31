from tkinter import *
from PIL import ImageTk, Image

# root = Tk()
# root.geometry("500x500")
#
# # imageLabel = Label(root)
# # def showImage():
# #     global imageLabel, my_image
# #     my_image = ImageTk.PhotoImage(Image.open("images/obese.png"))
# #     imageLabel = Label(root, image=my_image)
# #     imageLabel.pack()
# #
# # Button(root, text="Show image", command=showImage).pack()
#
# def test():
#     new_label = Label(root, text="Thank you for clicking me, " + entry_widget.get())
#     new_label.pack()
#
# def clear():
#     x = entry_widget.get()
#     entry_widget.delete(0, 5)
#
# entry_widget = Entry(root, relief=SOLID, bd=2, width=50)
# entry_widget.pack()
#
# click_button = Button(root, text="Click me!", command=test)
# click_button.pack()
#
# clear_button = Button(root, text="Clear", command=clear)
# clear_button.pack()
#
# root.mainloop()

my_list = [1, 2, 3,4]
my_list.remove(1)
print(my_list)