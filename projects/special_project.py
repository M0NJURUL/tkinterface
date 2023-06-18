# a special project
import os
import pygame
import random
import time
from tkinter import *

pygame.mixer.init()

root = Tk()
root.title("DO NOT PUSH THE DOOR")
root.iconbitmap("images/icons/64x64_special_project.ico")
# root.geometry("200x250")

sounds = os.listdir("sounds")
def play_sound():
    random_index = random.randint(0, len(sounds)-1)
    pygame.mixer.music.load("sounds/"+sounds[random_index])
    pygame.mixer.music.play()

clock = Label(root)

frame = LabelFrame(root, padx=70, pady=70)
frame.pack(padx=10, pady=10)

doorFrame = LabelFrame(frame, pady=80, bd=5)
doorFrame.pack()

doorButton = Button(doorFrame, text="Push", command=play_sound, padx=20, pady=20)
doorButton.pack(side=LEFT)
emptyLabel = Label(doorFrame, text="                 ")
emptyLabel.pack()

root.mainloop()




