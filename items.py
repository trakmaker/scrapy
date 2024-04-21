import scrapy

class IpoItem(scrapy.Item):
    company = scrapy.Field()
    symbol = scrapy.Field()
    industry = scrapy.Field()
    offer_date = scrapy.Field()
    shares_millions = scrapy.Field()
    offer_price = scrapy.Field()
    first_day_close = scrapy.Field()
    current_price = scrapy.Field()
    return_percentage = scrapy.Field()
    scoop_rating = scrapy.Field()