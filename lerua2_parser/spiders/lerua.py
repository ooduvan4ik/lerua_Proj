import scrapy
from scrapy.http import HtmlResponse
from lerua2_parser.items import Lerua2ParserItem
from scrapy.loader import ItemLoader
from lerua2_parser.items import Lerua2ParserItem

class LeruaSpider(scrapy.Spider):
    name = 'lerua'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://leroymerlin.ru/search/?q={query}']


    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[contains('Следующая', @aria-label)]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        goods = response.xpath("//a[@data-qa = 'product-image']")


        for i in goods:
            yield response.follow(i, callback=self.goods_parse)

    def goods_parse(self, response:HtmlResponse):

        lerua_loader=ItemLoader(item=Lerua2ParserItem(), response=response)
        lerua_loader.add_xpath('name', "//h1/text()")
        lerua_loader.add_value('link', response.url)
        lerua_loader.add_xpath('price', "//span[@slot='price']/text()")
        lerua_loader.add_xpath('photos', "//img[@itemprop='image']/@data-origin")
        yield lerua_loader.load_item()

        #name = response.xpath("//h1/text()").get()
        #link = response.url
        #price = response.xpath("//span[@slot='price']/text()").get()
        #photos = response.xpath("//img[@itemprop='image']/@data-origin").getall()
        #yield Lerua2ParserItem(name=name, link=link, price=price, photos=photos )




