import scrapy

from profiles.items import ProfilesItem


class ProfileSpider(scrapy.Spider):
    name = "profile"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ["https://www.linkedin.com/"]

    def parse(self, response):
        for profile in response.css("xxx"): # config HTML item here!
            item = ProfilesItem()
            item["url"] = profile.css("h3 > a::attr(href)").get() # config this as well
            item["name"] = profile.css().get() # You know the drill
            item["headline"] = profile.css().get() # You know the drill
            yield item
