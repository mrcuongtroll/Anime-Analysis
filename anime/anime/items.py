# -*- coding: utf-8 -*-

# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):

    title = scrapy.Field()          # str
    romaji_title = scrapy.Field()   # str
    english_title = scrapy.Field()  # str

    mean_score_anilist = scrapy.Field()     # float. range = [0, 10]
    mean_score_myanimelist = scrapy.Field()  # float. range = [0, 10]
    mean_score_anisearch = scrapy.Field()  # float. range = [0, 10]
    mean_score_kitsu = scrapy.Field()  # float. range = [0, 10]
    popularity_anilist = scrapy.Field()     # int (ranking)
    popularity_myanimelist = scrapy.Field()  # int (ranking)
    popularity_anisearch = scrapy.Field()  # int (ranking)
    popularity_kitsu = scrapy.Field()  # int (ranking)
    number_scorer_anilist = scrapy.Field()    # int
    number_scorer_myanimelist = scrapy.Field()  # int
    number_scorer_anisearch = scrapy.Field()  # int
    number_scorer_kitsu = scrapy.Field()  # int
    favorites_anilist = scrapy.Field()     # int
    favorites_myanimelist = scrapy.Field()  # int
    favorites_anisearch = scrapy.Field()  # int
    favorites_kitsu = scrapy.Field()  # int

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

    tags_anilist = scrapy.Field()            # list[str]
    tags_myanimelist = scrapy.Field()  # list[str]
    tags_anisearch = scrapy.Field()  # list[str]
    tags_kitsu = scrapy.Field()  # list[str]

    prequel = scrapy.Field()        # str
    sequel = scrapy.Field()         # str
    voice_actors = scrapy.Field()   # list[str]
    creator = scrapy.Field()        # str (author)
    directors = scrapy.Field()      # list[str]

    status_completed_anilist = scrapy.Field()   # int
    status_completed_myanimelist = scrapy.Field()  # int
    status_completed_anisearch = scrapy.Field()  # int
    status_completed_kitsu = scrapy.Field()  # int
    status_planning_anilist = scrapy.Field()    # int
    status_planning_myanimelist = scrapy.Field()  # int
    status_planning_anisearch = scrapy.Field()  # int
    status_planning_kitsu = scrapy.Field()  # int
    status_current_anilist = scrapy.Field()     # int
    status_current_myanimelist = scrapy.Field()  # int
    status_current_anisearch = scrapy.Field()  # int
    status_current_kitsu = scrapy.Field()  # int
    status_paused_anilist = scrapy.Field()      # int
    status_paused_myanimelist = scrapy.Field()  # int
    status_paused_anisearch = scrapy.Field()  # int
    status_paused_kitsu = scrapy.Field()  # int
    status_dropped_anilist = scrapy.Field()     # int
    status_dropped_myanimelist = scrapy.Field()  # int
    status_dropped_anisearch = scrapy.Field()  # int
    status_dropped_kitsu = scrapy.Field()  # int
