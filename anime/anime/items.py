# -*- coding: utf-8 -*-

# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):

    title = scrapy.Field()          # str
    romaji_title = scrapy.Field()   # str
    english_title = scrapy.Field()  # str
    mean_score = scrapy.Field()     # float. range = [0, 10]
    popularity = scrapy.Field()     # int (number of users)
    num_scorers = scrapy.Field()    # int
    favourites = scrapy.Field()     # int
    duration = scrapy.Field()       # int (minutes)
    status = scrapy.Field()         # str
    episodes = scrapy.Field()       # int
    source = scrapy.Field()         # str
    age = scrapy.Field()            # str
    target_group = scrapy.Field()   # list[str]
    genres = scrapy.Field()         # list[str]
    start_date = scrapy.Field()     # str (yyyy-mm-dd)
    end_date = scrapy.Field()       # str (yyyy-mm-dd)
    season_season = scrapy.Field()  # str (spring, summer, fall, winter)
    season_year = scrapy.Field()    # int
    media_type = scrapy.Field()     # str (format)
    url = scrapy.Field()            # str
    studios = scrapy.Field()        # list[str]
    producers = scrapy.Field()      # list[str]
    tag = scrapy.Field()            # list[str]
    prequel = scrapy.Field()        # str
    sequel = scrapy.Field()         # str
    voice_actors = scrapy.Field()   # list[str]
    creator = scrapy.Field()        # str (author)
    directors = scrapy.Field()      # list[str]
    status_completed = scrapy.Field()   # int
    status_planning = scrapy.Field()    # int
    status_current = scrapy.Field()     # int
    status_paused = scrapy.Field()      # int
    status_dropped = scrapy.Field()     # int
