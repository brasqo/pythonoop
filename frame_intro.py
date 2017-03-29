import tkinter as tk
from tkinter import ttk

#creates and opens a small frame
window = tk.Tk()
window.geometry("300x200")


#Banana label
alabel = ttk.Label(text="Banana")
alabel.grid(column=0, row=0)

#Apple label
blabel = ttk.Label(text="Apple")
blabel.grid(column=1, row=0)

#Banana qty button
buttona = ttk.Button(text="5")
buttona.grid(column=0, row=1)

#Apple qty button
buttonb = ttk.Button(text="12")
buttonb.grid(column=1, row=1)

window.mainloop()


