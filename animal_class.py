class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


pet_qazi = Animal("Qazoo")

print(pet_qazi.name)
print(pet_qazi.talk())


class Dog(Animal): #inherits from Animal class and then doing nothing.
    def talk(self):
		return "woof!"

class Cat(Animal):
	def talk(self):
		return "meow!"


pet = Dog("Dot")
print(pet.name)
print(pet.talk()) #brackets needed - polymorphic part. Works depending what class your working with

pet2 = Cat("Fluffy")
print(pet2.name)
print(pet2.talk())



#pet = Animal("Dot")
#print(pet.name)
