import scrapy

class BooksSpider(scrapy.Spider):
    name = 'booksspider'
    start_urls = ['http://books.toscrape.com/']
    
    def parse(self, response):
        for book in response.css('.product_pod'):
            yield {
                'title': book.css('h3 > a::attr(title)').get(),
                'price': book.css('.price_color::text').get()
            }
        next = response.css('li.next>a::attr(href)').get()
        if next:
            yield response.follow(next, self.parse)

#Command to run the spider:
# scrapy runspider -o books.csv books_scraper.py
# - books.csv - file in which the results will be saved

#Command to run an interactive shell:
# scrapy shell http://books.toscrape.com/