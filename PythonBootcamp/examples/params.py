import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"}, # accept response in a json format
	params={"term": "snow"} # https://icanhazdadjoke.com/search?term=snow
)

status_code = response.status_code
data = response.json() # converting json format to a python dictionary format
print(status_code)  # 200
print(len(data['results'])) # 6
