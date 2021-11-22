from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lerua2_parser.spiders.lerua import LeruaSpider
from lerua2_parser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    my_query = input('Введите товар: ')
    process.crawl(LeruaSpider, query=my_query)
    process.start()