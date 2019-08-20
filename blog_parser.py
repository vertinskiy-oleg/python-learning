import requests as req
from bs4 import BeautifulSoup 
from csv import writer

url = 'https://www.rithmschool.com/blog'

res = req.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

articles = soup.find_all('article')

with open('articles.csv', 'w') as file:
	csv_writer = writer(file)
	csv_writer.writerow(['title', 'url', 'date'])	
	for article in articles:
		a_tag = article.find('a')
		title = a_tag.get_text()
		url = a_tag['href']
		date = article.find('time')['datetime']
		csv_writer.writerow([title, url, date])