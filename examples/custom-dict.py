class CustomDict(dict):
	# Creating a new CustomDict class from a parent dict class
	def __repr__(self):
		print("Showing the dictionary") # Custom code
		return super().__repr__() # Calling the standart dict __repr__ method

	def __getitem__(self, key):
		# Get a value for the specified key
		print(f"Getting a value for the {key} key") # Custom code
		return super().__getitem__(key) # Calling the standart dict __getitem__ method

	def __setitem__(self, key, value):
		# Add a new key-value pair to the dictionary
		print(f"Setting a {value} value with a {key} key") # Custom code
		super().__setitem__(key, value) # Calling the standart dict __setitem__ method

d = CustomDict({'a':1, 'b':2, 'c':3})
print(d) # Showing the dictionary {'a': 1, 'b': 2, 'c': 3}
d['a'] = 5 # Setting a 5 value with a a key
print(d) # Showing the dictionary {'a': 5, 'b': 2, 'c': 3}
print(d['b']) # Getting a value for the b key 2



























class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"THAT THING YOU WANT ISN'T IN HERE")

	def __setitem__(self, key, value):
		print("Why do you always have to change things?")
		print(f"Ugh fine, setting {key} to {value}")
		super().__setitem__(key, value)