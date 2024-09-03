import scrapy

from jobs.items import JobsItem


class JobSpider(scrapy.Spider):
    name = "job"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ["https://www.linkedin.com/"]

    def parse(self, response):
        for job in recruiters.css(""):
            item = JobsItem()
            item['url'] = 
            yield item
