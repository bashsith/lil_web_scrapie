import scrapy


class JobsItem(scrapy.Item):
    url = scrapy.Field()
    recrtr_name = scrapy.Field()
    recrtr_email = scrapy.Field()
