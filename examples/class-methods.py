
class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def full_name(self):
		print(f"{self.first} {self.last}")

john = User("John", "Smith", 35) # creating instance with class User(). 
                                 # Directly from __init__
john.full_name() # John Smith
tom = User.from_string("Tom,Jones,89") # creating instance with class method User.from_string(). 
                                       # First from_string method, than __init__
tom.full_name() # Tom Jones
print(User.display_active_users()) # 2














