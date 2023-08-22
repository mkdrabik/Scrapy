# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_w_tax = scrapy.Field()
    tax = scrapy.Field()
    ava = scrapy.Field()
    num = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    des = scrapy.Field()
    price = scrapy.Field()
    