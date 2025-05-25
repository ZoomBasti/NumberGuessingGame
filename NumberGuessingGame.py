import random
import tkinter as tk
from random import randint
from tkinter import ttk, Widget
from turtledemo.nim import computerzug

from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")


name = ""       # Save her the name from the user


# Create a Welcome Screen
def welcomescreen():
    global name
    global random
    global entry
    random = randint(0, 100)
    if name == "" and nameinput.winfo_exists():     #Save the Name
        name = nameinput.get()

    for widget in root.winfo_children():    #Clear the Welcome Screen
        widget.destroy()

    Welcomefont = ttk.Label(root, text="Welcome " + name + " to the Number Guessing Game")
    Welcomefont.pack(pady=10)

    #Main-programm

    label = ttk.Label(root, text="The number generation was sucessfull!",foreground="Green")
    label.pack()
    entry = ttk.Entry(root)
    entry.pack(pady=10)
    entry.bind("<Return>", guess)





    #Quit Button
    quit = ttk.Button(root, text="QUIT", command=root.destroy)
    quit.pack(pady=20, side="bottom")


def guess(event = None):

# Durchgang der Überprüfung
    try:
        guess = int(entry.get())
    except ValueError:
        label = ttk.Label(root, text="Please enter a valid number.")
        return

    if guess < random:
        larger = ttk.Label(root, text="Please enter a larger number.")
        larger.pack()
    elif guess > random:
        smaller = ttk.Label(root, text="Please enter a smaller number.")
        smaller.pack()
    else:
        correct = ttk.Label(root, text="The number was correct!")
        correct.pack()
        entry.config(state=tk.DISABLED)
        again = ttk.Button(root, text="Try again", command=welcomescreen)
        again.pack()



#Welcome-Screen Layout
label = ttk.Label(root, text="Welcome to the Number Guessing Game enter your name: ", compound="left", )
label.pack(pady=100, side="top")
nameinput = ttk.Entry(root, width=50, justify='center')
nameinput.pack()
welcomescreen_button = ttk.Button(root, text="Start", command=welcomescreen)
welcomescreen_button.pack()




root.mainloop()