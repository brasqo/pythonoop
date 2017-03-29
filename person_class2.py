from PIL import ImageTk, Image
import datetime
import tkinter as tk



root = tk.Tk()
#create frame geometry
root.geometry("400x400")
# title of the App
root.title("Person Age Calculator")

#labels, on far left
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

name_label = tk.Label(text="Name")
name_label.grid(column=0, row=4)

#entries to right of labels
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

name_entry = tk.Entry()
name_entry.grid(column=1, row=4)

#.get retreives what u type in the entry field.
def calculate_age():
	print(year_entry.get())
	print(month_entry.get())
	print(day_entry.get())
	print(name_entry.get())
	person1 = Person(str(name_entry.get()), datetime.date(int(year_entry.get()),
										int(month_entry.get()),
										int(day_entry.get())))
	print(person1.age())
	#creates text box within frame
	text_answer = tk.Text(master=root, height=10, width=30)
	text_answer.grid(column=1, row=5)
	#creates an object 'answer_text' and formats it as a sentence.
	answer_text = "{name} is {age} years old.".format(name=person1.full_name,
													  age=person1.age())
	#inserts text within the textbox in the frame.
	#2nd arg is what value you want to display.
	text_answer.insert(tk.END, answer_text)


#create a button - 'command=' arg binds the function to the button
calc_button = tk.Button(text="Calculate", command=calculate_age)
calc_button.grid(column=1, row=5)

class Person:

	def __init__(self, full_name, birthday):
		self.full_name = full_name
		self.birthday = birthday

	def age(self):
		today = datetime.date.today()
		years_old = today.year - self.birthday.year
		return years_old

#object 'image' point to actual image file
image = Image.open("/home/z3d/Pictures/sample1.jpeg")
#shrinking image to 100x100, and performing antialiasing
image.thumbnail((100,100), Image.ANTIALIAS)
#object 'photo'
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)



#tray = Person("Tray Bali", datetime.date(1980, 1, 2))

#print(tray.full_name)
#print(tray.birthday)
#print(tray.age())

root.mainloop()