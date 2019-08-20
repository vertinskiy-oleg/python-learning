import requests as req
from bs4 import BeautifulSoup
from csv import writer

domain = 'https://www.rithmschool.com'
urls = ['/blog']

def crawl(url):
	res = req.get(domain+url)
	soup = BeautifulSoup(res.text, 'html.parser')
	next_url = soup.find(rel='next')
	if next_url == None:
		pass
	else:
		next_url = next_url['href']
	urls.append(next_url)
	
	articles = soup.find_all('article')
	
	with open('articles.csv', 'a') as file:
		csv_writer = writer(file)	
		for article in articles:
			a_tag = article.find('a')
			title = a_tag.get_text()
			url = a_tag['href']
			date = article.find('time')['datetime']
			csv_writer.writerow([title, url, date])

for i in range(9):
	crawl(urls[i])

#print('URLs: ', urls)