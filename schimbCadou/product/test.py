class Animal:
	def __init__(self, name):
		self.name = name

		def speak(self):
			raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):

	def speak(self):
		return "Meow!"

animals = [Dog("Buddy"), Cat("hera")]
for animal in animals:
	print(f'{animal.name} says {animal.speak()}')