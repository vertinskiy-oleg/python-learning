import requests as req
from random import choice

url = 'https://icanhazdadjoke.com/search'

print('DAD JOKE 3000')
user_term = input('Let me tell you a joke! Give me a topic: ')

res = req.get(
    url,
    headers = {'Accept': 'application/json'},
    params = {'term': user_term}
 ).json()

results = res['results']
num_jokes = len(results)

if num_jokes == 0:
    print(f"Sorry, I don't have any jokes about {user_term}. Please, try again")
elif num_jokes == 1:
    print(f"I've got one joke about {user_term}. Here it is:")
    print(results[0]['joke'])
else:
    print(f"I've got {num_jokes} jokes about {user_term}. Here is one:")
    print(choice(results)['joke'])
