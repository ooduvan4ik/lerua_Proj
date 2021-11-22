# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def proc_f(value):
    try:
        value.replace(" ", "")
        value=int(value)
    except Exception as e :
        print(e)
    finally:
        return value

class Lerua2ParserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    link=scrapy.Field(output_processor=TakeFirst())
    price=scrapy.Field(input_processor=MapCompose(proc_f), output_processor=TakeFirst())
    _id = scrapy.Field()

