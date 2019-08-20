from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self): 
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		# len() function will return age of an object
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"

j = Human("John", "Smith", 35)
k = Human("Kate", "Adams", 30)

print(j) # Human named John Smith aged 35
print(k) # Human named Kate Adams aged 30
print(len(j)) # 35
print(len(k)) # 30
print(j + k) # Human named Newborn Smith aged 0
print(j * 3) # [Human named John Smith aged 35, Human named John Smith aged 35, Human named John Smith aged 35]