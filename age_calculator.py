import tkinter as tk
import datetime
#from tkinter import ttk

tray = datetime.date(1980, 10, 20)
ageDays = datetime.date.today() - tray
ageYears = datetime.date.today().year - tray.year

def bday(event):
	print("Tray's birthday is: " + str(tray))

def age_in_days(event):
	print("Tray is " + str(ageDays) + " days old.")

def age_in_years(event):
	print("Tray is " + str(ageYears) + " years old.")

window = tk.Tk()
window.geometry("400x200")
# title of the App
window.title("Age Calculator")

#labels
alabel = tk.Label(text=datetime.date.today())
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Birthday")
blabel.grid(column=0, row=1)

clabel = tk.Label(text="Age in Days")
clabel.grid(column=1, row=1)

dlabel = tk.Label(text="Age in Years")
dlabel.grid(column=2, row=1)

#buttons for labels
buttonB = tk.Button(window, text="Push for Bday")
buttonB.grid(column=0, row=2)

buttonC = tk.Button(window, text="Push for Age in Days")
buttonC.grid(column=1, row=2)

buttonD = tk.Button(window, text="Push for Age in Years")
buttonD.grid(column=2, row=2)

#binding buttons
buttonB.bind("<Button-1>", bday)
buttonC.bind("<Button-1>", age_in_days)
buttonD.bind("<Button-1>", age_in_years)

#print(now.year)

#prints the date
#print("Today's date is: " + str(datetime.date.today()))

#print("Tray's birthday is: " + str(tray))
#print("Tray is " + str(ageDays) + " days old.")
#print("Tray is " + str(ageYears) + " years old.")

window.mainloop()