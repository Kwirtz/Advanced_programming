# item.py

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyWikiItem(scrapy.Item):
    # Read the documentation, scrapy.Field() basic item object
    id_ = scrapy.Field()
    href = scrapy.Field()
    text = scrapy.Field()