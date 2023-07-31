from tkinter import *

root = Tk()
root.geometry("250x250")
# root.configure(bg="#E6D8D4") #to change background color of the root window using hexadecimal

root.title("Adult Body Mass Index Calculator")

# using image for icon, .ico file is used
root.iconbitmap("images/icons/32x32_project5.ico")

# will be used later to create image label
underweight = PhotoImage(file="images/bmi states/underweight.png")
normal = PhotoImage(file="images/bmi states/normal.png")
overweight = PhotoImage(file="images/bmi states/overweight.png")
obese = PhotoImage(file="images/bmi states/obese.png")

appLabel = Label(root, text="BMI calculator (for age 18 or older)", bg="cyan", borderwidth=10)

weightLabel = Label(root, text="Enter weight (in KG):")
weight = Entry(root)

heightLabel = Label(root, text="Enter height (in FT):")
height = Entry(root)

result = Label(root)

# new label for part 2
imageLabel = Label(root)

def action():
    global result
    global imageLabel
    result.destroy()
    imageLabel.destroy()

    try:
        w = float(weight.get())
        h = float(height.get())
        h = h * 0.3048
        h_square = h ** 2
        BMI = w / h_square
        print(BMI)
        if BMI >= 30:
            state = "obese"
            imageLabel = Label(root, image=obese)
        elif BMI >= 25:
            state = "overweight"
            imageLabel = Label(root, image=overweight)
        elif BMI <= 18.5:
            state = "underweight"
            imageLabel = Label(root, image=underweight)
        else:
            state = "normal"
            imageLabel = Label(root, image=normal)
        result = Label(root, text="You are " + state)

    except ValueError:
        result = Label(root, text="Are you?")

    result.grid(row=4, column=0)
    # new label grid
    imageLabel.grid(row=4, column=1)


button = Button(root, text="Am I?", command=action)

appLabel.grid(row=0, column=0, columnspan=2)

weightLabel.grid(row=1, column=0)
weight.grid(row=1, column=1)

heightLabel.grid(row=2, column=0)
height.grid(row=2, column=1)

button.grid(row=3, column=0, columnspan=2)

root.mainloop()
