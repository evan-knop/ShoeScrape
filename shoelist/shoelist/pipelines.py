import pymongo

from scrapy import settings
from scrapy.exceptions import DropItem
import logging
from shoelist import settings

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings.SETTING.get('MONGODB_SERVER'),
            settings.SETTING.get('MONGODB_PORT')
        )
        db = connection[settings.SETTING.get('MONGODB_DB')]
        self.collection = db[settings.SETTING.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.info("Shoe added to MongoDB database!",
                    spider=spider)
        return item