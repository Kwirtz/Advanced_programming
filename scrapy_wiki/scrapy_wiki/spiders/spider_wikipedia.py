# spider_wikipedia.py 

import scrapy
from scrapy_wiki.items import ScrapyWikiItem


# A class that inherits from scrapy.Spider. We will see in Chap 2 what inheritance is for the moment just know that we "inherit" modules from the class scrapy.Spider
# This means that you have some function and features already implemented and usable.
 
class SpiderWikipediaSpider(scrapy.Spider):
    # the name we introduce during the creation of the spider
    name = 'spider_wikipedia'
    # If you try to scrap an url outside of allowed_domains it wont work
    allowed_domains = ['wikipedia.org']
    # The first url you will parse
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]
    # create a counter
    n_processed = 0

    # What you do with the first url, response = what we get with a request.get()
    def parse(self, response):

        hrefs = response.xpath("//div[@id='bodyContent']//a[@href[re:test(.,'^(/wiki/)((?!:).)*$')]]/@href").getall()
        # update counter
        self.n_processed += 1
        # create instance of item
        item = ScrapyWikiItem()
        item["href"] = response.url
        item["text"] = response.xpath("//p/text()").getall()
        item["id_"] = self.n_processed
        
        yield item
        # Scrapy works based on scrapy request, the most important argument being callback
        # Basically you get an url and call a function to work on this url (in this case the same as for starting_url: parse())
        for url in hrefs:
            # meta if you want to update item as you go along, in this case not needed
            yield scrapy.Request(url="https://en.wikipedia.org" + url, callback=self.parse,meta={'item': item})