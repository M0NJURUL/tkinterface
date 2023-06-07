# here we will create an "Adult BMI Calculator" using the previously learned topics

from tkinter import *

root = Tk()
root.geometry("250x125")  # to set the initial size of the box window

# changing the title of the project
root.title("Adult Body Mass Index Calculator")

# creating widgets (Label, Input)
appLabel = Label(root, text="BMI calculator (for age 18 or older)")

weightLabel = Label(root, text="Enter weight (in KG):")
weight = Entry(root)

heightLabel = Label(root, text="Enter height (in FT):")
height = Entry(root)

result = Label(root)
# creating this empty Label for result is important
# to overwrite previous result and use destroy
# try your code without it to better understand

def action():
    global result # used a variable from outside function
    result.destroy()

    try:
        w = int(weight.get())
        h = int(height.get())
        h = h * 0.3048  # converting to meter
        h_square = h ** 2
        BMI = w / h_square
        if BMI >= 30:
            state = "obese"
        elif BMI >= 25:
            state = "overweight"
        elif BMI <= 18.5:
            state = "underweight"
        else:
            state = "normal"
        result = Label(root, text="You are " + state)

    except ValueError:
        result = Label(root, text="Are you?")

    result.grid(row=4, column=0)


button = Button(root, text="Am I?", command=action)

# using grid to
appLabel.grid(row=0, column=0, columnspan=2)

weightLabel.grid(row=1, column=0)
weight.grid(row=1, column=1)

heightLabel.grid(row=2, column=0)
height.grid(row=2, column=1)

button.grid(row=3, column=0, columnspan=2)

root.mainloop()
