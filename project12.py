# we will learn showing messagebox

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("message box")
root.iconbitmap("")

def popup():
    # messagebox methods -> showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    # messagebox.showinfo("Popup Title", "Hello!")
    # messagebox.askquestion("Popup Title", "Are you okay?")
    # messagebox.askokcancel("Popup Title", "You agree with our terms and conditions, right? ..right?")
    # messagebox.askyesno("Popup Title", "Did you cancel?")
    # messagebox.showwarning("Popup Title", "Careful of the errors!")
    # messagebox.showerror("Popup Title", "I warned you!")

    # response = messagebox.askyesno("Popup Title", "Hello!")
    # Label(root, text=response).pack()

    response = messagebox.askyesno("Propose", "Will you marry me?")
    if response == 1:
        Label(root, text="You are a lucky man!").pack()
    else:
        Label(root, text="I feel bad for you.").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()
