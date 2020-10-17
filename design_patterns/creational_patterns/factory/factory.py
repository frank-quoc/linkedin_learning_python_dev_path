class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

class Cat:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet='dog'):
	"""Factory method"""
	pets = dict(dog=Dog('Spot'), cat=Cat('Scatchy'))

	return pets[pet]

d = get_pet('dog')
c = get_pet('cat')

print(d.speak(), c.speak(), sep='\n')
