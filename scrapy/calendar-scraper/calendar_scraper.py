import scrapy

class CalendarSpider(scrapy.Spider):
    name = 'calendarspider'
    start_urls = ['http://www.calendarium.com.ua/dekabr']
    domain = 'http://www.calendarium.com.ua/'
    
    def parse(self, response):
        for date in response.css('.p1_'):
            yield {
                'day': date.css('.p1_ > .a16::text').get(),
                'event_type': date.css('.p1_ #norm > a::text').get(),
                'event_name': date.css('.p1_ .x33::text').get(),
                'event_url': CalendarSpider.domain + date.css('.p1_ .x33::attr(href)').get(), 
            }