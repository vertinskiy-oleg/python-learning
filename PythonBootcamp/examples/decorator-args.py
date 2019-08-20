# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
	return "lol"

print(greet("todd")) # HI, I'M TODD.
print(order(side="burger", main="fries")) # HI, I'D LIKE THE FRIES, WITH A SIDE OF BURGER, PLEASE.
print(lol()) # LOL
