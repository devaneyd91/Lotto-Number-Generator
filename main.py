import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from unittest import result
from lotto import irish_lotto, euromillions
import math

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
        label = tk.Label(newWindow, text="The cost of your ticket will be: €" + costirish(), width=50, height=5, padx=20)
        label.pack()

    elif value == 3:
        label = tk.Label(newWindow, text="Your first line is: " + irish_lotto(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + irish_lotto(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="Your third line is: " + irish_lotto(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="The cost of your ticket will be: €" + costirish(), width=50, height=5, padx=20)
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
        label = tk.Label(newWindow, text="The cost of your ticket will be: €" + costeuro(), width=50, height=5, padx=20)
        label.pack()
    elif value == 2:
        label = tk.Label(newWindow, text="Your first line is: " + euromillions(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="The cost of your ticket will be: €" + costeuro(), width=50, height=5, padx=20)
        label.pack()
    elif value == 3:
        label = tk.Label(newWindow, text="Your first line is: " + euromillions(), width=50, height=5)
        label.pack()
        label = tk.Label(newWindow, text="Your second line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="Your third line is: " + euromillions(), width=50, height=5, padx=20)
        label.pack()
        label = tk.Label(newWindow, text="The cost of your ticket will be: €" + costeuro(), width=50, height=5, padx=20)
        label.pack()

def costirish():

    value = v.get()
    if value == 1:
        cost = 2
    elif value == 2:
        cost = 4
    elif value == 3:
        cost = 6

    value2 = v2.get()
    if value2 == 1:
        if cost == 2:
            plus = 1
        elif cost == 4: 
            plus = 2
        elif cost == 6:
            plus = 3
    irish_cost = cost + plus
    print (irish_cost)
    return str(irish_cost)
    
def costeuro():

    value = v.get()
    if value == 1:
        cost = 2.5
    elif value == 2:
        cost = 5
    elif value == 3:
        cost = 7.5

    value2 = v2.get()
    plus = 0
    if value2 == 1:
        if cost == 2.50:
            plus = 1
        elif cost == 5:
            plus = 2
        elif cost == 7.50:
            plus = 3
    euro_cost = (cost + plus)
    print (euro_cost)
    return str(euro_cost)

window = tk.Tk()
window.title("Lotto Number Generator")
v = tk.IntVar()
v2 = tk.IntVar()

label = tk.Label(text="Lotto Number Generator", width=50, height=5)
label.pack()

label = tk.Label(text="How many lines would you like to play?", width=50, height=5, padx = 20)
label.pack(anchor=tk.W)

one = tk.Radiobutton(window, text="1 Line", padx = 20, variable=v, value=1, command=optionselected).pack(anchor=tk.NW)
two = tk.Radiobutton(window, text="2 Lines", padx = 20, variable=v, value=2, command=optionselected).pack(anchor=tk.NW)
three = tk.Radiobutton(window, text="3 Lines", padx = 20, variable=v, value=3, command=optionselected).pack(anchor=tk.NW)

plus = tk.Checkbutton(window, text='Add Plus?',variable=v2, onvalue=1, offvalue=0)
plus.pack(anchor=tk.N)

button = tk.Button(text="Irish Lotto", width=50, height=5, bg="blue", fg="yellow", command=OpenNewWindowIrish)
button.pack(padx=5, pady=15, side=tk.LEFT)

button2 = tk.Button(text="EuroMillions", width=50, height=5, bg="blue", fg="yellow", command=OpenNewWindowEuro)
button2.pack(padx=5, pady=20, side=tk.LEFT)

window.mainloop()