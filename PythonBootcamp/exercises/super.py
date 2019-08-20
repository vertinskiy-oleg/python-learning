class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old"


class Manager(User):
    def __init__(self, first_name, last_name, age, salary, department):
        super().__init__(first_name, last_name, age) # name and age inherits from User class
        self.salary = salary
        self.department = department

    def __repr__(self):
        return f"{super().__repr__()} from {self.department} department" # calls User.__repr__ method

usr1 = User("John", "Smith", 35)
mng1 = Manager("John", "Smith", 35, 2000, "Marketing")
print(usr1) # John Smith, 35 years old
print(mng1) # John Smith, 35 years old from Marketing department
help(Manager)




