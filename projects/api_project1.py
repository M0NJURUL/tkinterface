from tkinter import *
from tkinter import ttk
import requests

# joke = "joke"

root = Tk()
root.title("You Need To Laugh!")

# joke frame
frame1 = LabelFrame(root, height=100, width=500)
frame1.grid(padx=5, pady=5)
# frame1.pack_propagate(FALSE)

# review frame
frame2 = LabelFrame(root, height=1000, width=500)
frame2.grid(padx=5, pady=5)
frame2.grid_propagate(FALSE)

# progress frame
frame3 = LabelFrame(root, height=50, width=500)
frame3.grid(padx=5, pady=5)
# frame3.pack_propagate(FALSE)

joke_label = Label(frame1)

# Joke generating function
def generate():
    button1["state"] = NORMAL
    button2["state"] = NORMAL
    button3["state"] = NORMAL
    global joke_label
    joke_label.destroy()
    # random jokes
    category = "any"
    req = requests.get(f"https://v2.jokeapi.dev/joke/{category}")
    data = req.json()
    # generate_button.destroy()
    # joke inside frame1
    if data["type"] == "single":
        joke = data["joke"]
    else:
        joke = data["setup"] + "\n" + data["delivery"]
    joke_label = Label(frame1, text=joke)
    joke_label.pack()

def progress(num):
    progress_bar["value"] += num
    if progress_bar["value"] > 99:
        button1["state"] = DISABLED
        button2["state"] = DISABLED
        button3["state"] = DISABLED
        generate_button["state"] = DISABLED
    else:
        generate()

# progress bar
progress_bar = ttk.Progressbar(frame3, length=500)
progress_bar.pack()

# generate & rating buttons
generate_button = Button(frame1, text="Generate", command=generate)
button1 = Button(frame2, state=DISABLED, text="DIDN'T LAUGH", command=lambda: progress(-10))
button2 = Button(frame2, state=DISABLED, text="FUNNY", command=lambda: progress(20))
button3 = Button(frame2, state=DISABLED, text="LMFAO", command=lambda: progress(33.33))

# showing the buttons
generate_button.pack()
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button1.pack(anchor=E)
button2.pack(anchor=E)
button3.pack(anchor=E)

root.mainloop()
