import scrapy
from ipo_scrapy.items import IpoItem

class IpoSpider(scrapy.Spider):
    name = 'ipo_data'
    #allowed_domains = ['example.com']
    start_urls = ['https://www.iposcoop.com/current-year-pricings/']

    def parse(self, response):
        tables = response.xpath('//table[contains(@class, "ipolist")]')
        for table in tables:
            rows = table.xpath('.//tr')[1:]  # Skipping the header row
            for row in rows:
                item = IpoItem()
                item['company'] = row.xpath('td[1]/text()').get()
                item['symbol'] = row.xpath('td[2]/text()').get()
                item['industry'] = row.xpath('td[3]/text()').get()
                item['offer_date'] = row.xpath('td[4]/text()').get()
                item['shares_millions'] = row.xpath('td[5]/text()').get()
                item['offer_price'] = row.xpath('td[6]/text()').get()
                item['first_day_close'] = row.xpath('td[7]/text()').get()
                item['current_price'] = row.xpath('td[8]/text()').get()
                item['return_percentage'] = row.xpath('td[9]/text()').get()
                item['scoop_rating'] = row.xpath('td[10]/text()').get()
                yield item
