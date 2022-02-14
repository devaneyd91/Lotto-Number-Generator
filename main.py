import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from unittest import result
from lotto import irish_lotto, euromillions
from functools import partial


def optionselected():
   v.get()

def OpenNewWindowIrish():
    value = v.get()
    newWindow = Toplevel(window)
    newWindow.title("Your Numbers")
    newWindow.geometry("400x400")
    Label(newWindow, text ="These are your lucky numbers!").pack()
    if value == 1:
        label = tk.Label(newWindow, text=irish_lotto(), width=50, height=5)
        label.pack()
    elif value == 2:
        label = tk.Label(newWindow, text="Your first line is: " + irish_lotto(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + irish_lotto(), width=50, height=5, padx=20)
        label.pack()
    elif value == 3:
        label = tk.Label(newWindow, text="Your first line is: " + irish_lotto(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + irish_lotto(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="Your third line is: " + irish_lotto(), width=50, height=5, padx=20)
        label.pack()
    
def OpenNewWindowEuro():
    value = v.get()
    newWindow = Toplevel(window)
    newWindow.title("Your Numbers")
    newWindow.geometry("400x400")
    Label(newWindow, text ="These are your lucky EuroMillions numbers!").pack()
    if value == 1:
        label = tk.Label(newWindow, text=euromillions(), width=50, height=5)
        label.pack()
    elif value == 2:
        label = tk.Label(newWindow, text="Your first line is: " + euromillions(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()
    elif value == 3:
        label = tk.Label(newWindow, text="Your first line is: " + euromillions(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="Your third line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()


window = tk.Tk()
window.title("Lotto Number Generator")
v = tk.IntVar()

label = tk.Label(text="Lotto Number Generator", width=50, height=5)
label.pack()

label = tk.Label(text="How many lines would you like to play?", width=50, height=5, padx = 20)
label.pack(anchor=tk.W)

one = tk.Radiobutton(window, text="1 Line", padx = 20, variable=v, value=1, command=optionselected).pack(anchor=tk.NW)


two = tk.Radiobutton(window, text="2 Lines", padx = 20, variable=v, value=2, command=optionselected).pack(anchor=tk.NW)

three = tk.Radiobutton(window, text="3 Lines", padx = 20, variable=v, value=3, command=optionselected).pack(anchor=tk.NW)


button = tk.Button(text="Irish Lotto", width=50, height=5, bg="blue", fg="yellow", command=OpenNewWindowIrish)
button.pack(padx=5, pady=15, side=tk.LEFT)

button2 = tk.Button(text="EuroMillions", width=50, height=5, bg="blue", fg="yellow", command=OpenNewWindowEuro)
button2.pack(padx=5, pady=20, side=tk.LEFT)

window.mainloop()