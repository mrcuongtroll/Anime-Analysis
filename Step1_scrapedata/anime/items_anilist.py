# -*- coding: utf-8 -*-

# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AnilistScraperItem(scrapy.Item):

    ranking_score = scrapy.Field()
    ranking_popularity = scrapy.Field()
    user_preferred_title = scrapy.Field()
    format = scrapy.Field()
    episodes = scrapy.Field()
    duration = scrapy.Field()
    status = scrapy.Field()
    season = scrapy.Field()
    avg_score = scrapy.Field()
    mean_score = scrapy.Field()
    popularity = scrapy.Field()
    favorites = scrapy.Field()
    studios = scrapy.Field()
    producers = scrapy.Field()
    source = scrapy.Field()
    genres = scrapy.Field()
    romaji_title = scrapy.Field()
    english_title = scrapy.Field()
    tags = scrapy.Field()
    prequel = scrapy.Field()
    sequel = scrapy.Field()
    voice_actors = scrapy.Field()
    director = scrapy.Field()
    og_creator = scrapy.Field()
    status_completed = scrapy.Field()
    status_planning = scrapy.Field()
    status_current = scrapy.Field()
    status_paused = scrapy.Field()
    status_dropped = scrapy.Field()
    score_distribution = scrapy.Field()
    url = scrapy.Field()
