# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    media_type = scrapy.Field()
    num_episodes = scrapy.Field()
    duration = scrapy.Field()
    status = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    source = scrapy.Field()
    studios = scrapy.Field()
    target_group = scrapy.Field()
    genres = scrapy.Field()
    tags = scrapy.Field()
    score = scrapy.Field()
    rank = scrapy.Field()
    pass
