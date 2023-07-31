# here we will create a calculator using the previously learned topics

from tkinter import *
root = Tk()

# changing the title of the project
root.title("Calculator")

e = Entry(root, width=45, borderwidth=10)
# e.insert(0, "0")

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# columnspan merges 3 column as the buttons under the input field will be in 3 columns

def buttonPressed(number):
    # if e.get() == "0":
    #     e.delete(0, END)
    value = e.get()
    e.delete(0, END)
    e.insert(0, value + str(number))
def clearButton():
    e.delete(0, END)

global first_number, arithmetic_operator
# first_number = 0
# arithmetic_operator = "addition"

def addButton():
    global first_number
    global arithmetic_operator
    arithmetic_operator = "addition"
    first_number = int(e.get())
    e.delete(0, END)
def subtractButton():
    global first_number
    global arithmetic_operator
    arithmetic_operator = "subtraction"
    first_number = int(e.get())
    e.delete(0, END)
def multiplyButton():
    global first_number
    global arithmetic_operator
    arithmetic_operator = "multiplication"
    first_number = int(e.get())
    e.delete(0, END)
def divideButton():
    global first_number
    global arithmetic_operator
    arithmetic_operator = "division"
    first_number = int(e.get())
    e.delete(0, END)
def equalButton():
    second_number = int(e.get())
    e.delete(0, END)
    if arithmetic_operator == "addition":
        e.insert(0, first_number + second_number)
    elif arithmetic_operator == "subtraction":
        e.insert(0, first_number - second_number)
    elif arithmetic_operator == "multiplication":
        e.insert(0, first_number * second_number)
    elif arithmetic_operator == "division":
        try:
            e.insert(0, round(first_number / second_number, 2))
        except ZeroDivisionError:
            e.insert(0, ":O")

# creating buttons -> 0-9, clear, addition, equal
# lambda in tkinter works a little differently
# it helps passing a parameter because normally we can not pass parameter in command
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonPressed(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonPressed(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonPressed(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonPressed(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonPressed(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonPressed(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonPressed(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonPressed(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonPressed(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonPressed(0))

button_clear = Button(root, text="Clear", padx=40, pady=20, command=clearButton, borderwidth=3, width=15)
button_add = Button(root, text="+", padx=40, pady=20, command=addButton, borderwidth=3)
button_equal = Button(root, text="=", padx=40, pady=20, command=equalButton, borderwidth=3, width=15)

button_subtract = Button(root, text="-", padx=40, pady=20, command=subtractButton)
button_multiply = Button(root, text="x", padx=40, pady=20, command=multiplyButton)
button_divide = Button(root, text="/", padx=40, pady=20, command=divideButton)


# using grid to show the buttons onto the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

root.mainloop()
