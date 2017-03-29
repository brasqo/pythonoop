import tkinter as tk
from tkinter import ttk
import webbrowser

def doorbell(event):
	print("DING-DONG!!!")

def doorbell2(event):
	print("Ring-a-Ding-ding-ding!")

def open_cp(event):
	webbrowser.open_new_tab("https://cleverprogrammer.com")

def open_google(event):
	webbrowser.open_new_tab("https://google.com")

#creates and opens a small frame/window
window = tk.Tk()
window.geometry("400x200")
#title of the App
window.title("Tkinter Testing")

#Banana label
alabel = ttk.Label(text="Banana")
alabel.grid(column=0, row=0)

#Apple label
blabel = ttk.Label(text="Apple")
blabel.grid(column=1, row=0)

#CleverProgrammer label
clabel = ttk.Label(text="Clever Prog.")
clabel.grid(column=2, row=0)

#google label
dlabel = ttk.Label(text="Google")
dlabel.grid(column=3, row=0)

#Banana qty button
buttonA = ttk.Button(window, text="Doorbell")
buttonA.grid(column=0, row=1)

#Apple qty button
buttonB = ttk.Button(window, text="RingRing")
buttonB.grid(column=1, row=1)

#Clever Prog button
buttonC = ttk.Button(window, text="CP")
buttonC.grid(column=2, row=1)

#google button
buttonD = ttk.Button(window, text="Google")
buttonD.grid(column=3, row=1)

#Binding the button to the entire window (no good), and assigning left-click to
#start the doorbell function.
#window.bind("<Button-1>", doorbell)

#binding the doorbell function to buttonA, L-click operates
buttonA.bind("<Button-1>", doorbell)
#binding the doorbell2 function to buttonB, L-click operates
buttonB.bind("<Button-1>", doorbell2)
#binding the open_cp function to buttonC, L-click operates
buttonC.bind("<Button-1>", open_cp)

#binding the open_google function to buttonD, L-click operates
buttonD.bind("<Button-1>", open_google)

window.mainloop()


