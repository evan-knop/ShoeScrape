import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shoelist.items import ShoelistItem


class ShoelistCrawlerSpider(CrawlSpider):
    name = 'shoelist_crawler'
    allowed_domains = ['runrepeat.com']
    start_urls = ['https://runrepeat.com/catalog/running-shoes']

    rules = (
        Rule(LinkExtractor(allow=r'running-shoes\?page=[0-67]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        shoes = response.xpath('//*[@id="rankings-list"]/li')

        for shoe in shoes:
            item = ShoelistItem()

            item['ShoeName'] = shoe.xpath(
                'div[5]/div[1]/a/span/text()').extract()[0]

            item['Price'] = shoe.xpath(
                'div[5]/div[4]/div[2]/div[1]/span[1]/text()').extract()[0]

            yield item

