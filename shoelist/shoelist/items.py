# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class ShoelistItem(scrapy.Item):

    #Company = Field()
    ShoeName = Field()
    #Terrain = Field()
    Price = Field()
    #BestUse = Field()
    #Discontinued = Field()
    Date_Modified = Field()
