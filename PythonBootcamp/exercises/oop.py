# # Define Bank Account Below:
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, num):
#         self.balance += num
#         return self.balance
        
#     def withdraw(self, num):
#         self.balance -= num
#         return self.balance

# acc1 = BankAccount('Oleg', 10)
# print(acc1.owner)
# print(acc1.balance)
# acc1.deposit(10)
# print(acc1.balance)
# acc1.withdraw(5)
# print(acc1.balance)

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        print(f"{self.first} {self.last}")

    def likes(self, thing):
        print(f"{self.first} likes {thing}")


user1 = User("John", "Smith", 30)
user1.full_name()
user1.likes("fruits")

