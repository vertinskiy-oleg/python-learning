# age = input('How old are you? : ')
# if age:
#     age = int(age)
#     if age >= 21:
#         print('You can come in and drink')
#     elif age >= 18:
#         print('You can come in but need a wristband')
#     else:
#         print('You are too young')
# else:
#     print('Please, enter your age.')

# def find_short(s):
#     s_list = s.split()
#     s_len = []
#     for sl in s_list:
#        s_len.append(len(sl))
#     print(s_len)
#     return min(s_len)


# print(find_short("bitcoin take over the world maybe who knows perhaps"))


# num = input("How many times do I have to tell you? ")
# num = int(num)

# for i in range(num):
#     print(f"time {i+1}: Clean UP!")


# for num in range(1, 21):
#     if num == 4 or num == 13:
#         state = "Unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")


# emoji = "\U0001f600"
# num = 1

# while num < 10:
#     print(emoji * num)
#     num += 1

# for n in range(10):
#     print(emoji * n)


# print("Hey how's it going?")
# user_input = input()

# while user_input != "stop copying me":
#     print(user_input)
#     user_input = input()
# print("Ok, you win")


# from random import randint  # use randint(a, b) to generate a random number between a and b

# number = 0 # store random number in here, each time through
# i = 0  # i should be incremented by one each iteration

# while number != 5:
#     number = randint(1, 10)
#     i += 1

# print(i)


# import random

# random_number = random.randint(1,10)

# while True:
#     user_number = int(input("Guess a number between 1 and 10: "))
#     if user_number == random_number:
#         print("You guessed it!")
#         cont = input("Do you want to keep playing? (y/n) ")
#         if cont == "y":
#             random_number = random.randint(1,10)
#             continue
#         else:
#             print("Thanks for playing! Bye.")
#             break
#     elif user_number > random_number:
#         print("Too high, try again")
#     else:
#         print("Too low, try again")


# '''
# calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
# '''


# def calculate(**kwargs):
#     first = kwargs.get('first', 0)
#     second = kwargs.get('second', 0)
#     operation = kwargs.get('operation', 'add')
#     make_float = kwargs.get('make_float', False)
#     result = 0

#     operation_lookup = {
#         "add": first + second,
#         "subtract": first - second,
#         "multiply": first * second,
#         "divide": first / second
#     }

#     if make_float:
#         result = float(operation_lookup[operation])
#     else:
#         result = int(operation_lookup[operation])

#     return "{} {}".format(kwargs.get('message', "The result is"), result)

# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
# print(calculate(make_float=True, operation='divide', first=3.5, second=5))


# first = 5
# second = 2

# operation_lookup = {
#         "add": first + second,
#         "subtract": first - second,
#         "multiply": first * second,
#         "divide": first / second
#     }

# operation_lookup['add'] # 7
# operation_lookup['subtract'] # 3
# operation_lookup['multiply'] # 10
# operation_lookup['divide'] # 2.5


# def div(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError as err:
#         print("It's a ZeroDivisionError")
#         print(err)
#     except TypeError as err:
#         print("It's a ValueError")
#         print(err)
#     else:
#         print(result)
#     finally:
#         print("End of a function")

# div(1, 2)
# div(1, 0)
# div(1, 'a')


# def debug_func(a,b,c):
#     first = a
#     import pdb; pdb.set_trace()
#     second = b
#     third = c
#     result = first + second + third
#     return result

# debug_func(1,2,3)

# def divide(num1, num2):
#     try:
#         result = num1/num2
#     except TypeError as err:
#         return "Please provide two integers or floats"
#     except ZeroDivisionError as err:
#         return "Please do not divide by zero"
#     else:
#         return result


# divide(4, 2)
# divide([], "1")
# divide(1, 0)


# for num in range(1,5):
#     print(num)
# else:
#     print(f"{num + 1} is too high")


# from functools import wraps

# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('Here are the args: {}'.format(args))
#         print('Here are the kwargs: {}'.format(kwargs))
#         fn(*args, **kwargs)
#     return wrapper

# @show_args
# def do_nothing(*args, **kwargs):
#     pass

# do_nothing(1, 2, 3, a="hi", b="bye")


# from functools import wraps

# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return [result, result]
#     return wrapper

# @double_return 
# def add(x, y):
#     return x + y

# @double_return
# def greet(name):
#     return "Hi, I'm " + name

# print(add(2,3))
# print(greet("Colt"))


# from functools import wraps

# def ensure_fewer_than_three_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if len(args) >= 3:
#             return "Too many arguments!"
#         return fn(*args, **kwargs)
#     return wrapper

# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# print(add_all()) # 0
# print(add_all(1)) # 1
# print(add_all(1,2)) # 3
# print(add_all(1,2,3)) # "Too many arguments!"
# print(add_all(1,2,3,4,5,6)) # "Too many arguments!"


# from functools import wraps

# def only_ints(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         int_check = all(type(arg) == int for arg in args)
#         if not int_check:
#             return "Please only invoke with integers."
#         return fn(*args, **kwargs)
#     return wrapper

# @only_ints 
# def add(x, y):
#     return x + y
    
# print(add(1, 2)) # 3
# print(add("1", "2")) # "Please only invoke with integers.


def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y

print(add_positive_numbers(1,5)) # 6
print(add_positive_numbers(1,-5)) # AssertionError: Both numbers must be positive


