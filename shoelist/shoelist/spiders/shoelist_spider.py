from scrapy import Spider
from scrapy.selector import Selector

from shoelist.items import ShoelistItem


class ShoelistSpider(Spider):
    name = "shoelist"
    allowed_domains = ["runrepeat.com"]
    start_urls = [
        "https://runrepeat.com/catalog/running-shoes",
    ]

    def parse(self, response):
        shoes = Selector(response).xpath('//*[@id="rankings-list"]/li')

        print("SHOEEEEES: ")
        print(shoes)

        for shoe in shoes:
            item = ShoelistItem()

            item['ShoeName'] = shoe.xpath(
                'div[5]/div[1]/a/span/text()').extract()[0]

            item['Price'] = shoe.xpath(
                'div[5]/div[4]/div[2]/div[1]/span[1]').extract()[0]

            yield item
