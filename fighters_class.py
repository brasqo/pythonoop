class Fighters:


	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10


	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage
		print("{} attacks {}".format(self.name, other_guy.name))
		print("{} lost {} health points!".format(other_guy.name, self.damage))
		print("{} now has {} health remaining.".format(other_guy.name, other_guy.health))

#string formatting - essentially overwriting the print func.
	def __str__(self):
		return "{}: {}".format(self.name, self.health)


qazi = Fighters('Qazi')
you = Fighters('Billy')

print(qazi)  # Qazi: 100 due to string formatting
print(you)  # Billy: 100

print(qazi.name)
print(you.name)

you.attack(qazi)

print(qazi)

class Boxer(Fighters):
	def heal(self):
		self.health += 10


boxer_qazi = Boxer("Boxer Qazi")
print(boxer_qazi)
print(boxer_qazi.damage)
print(boxer_qazi.health)

boxer_qazi.heal()

print(boxer_qazi)





