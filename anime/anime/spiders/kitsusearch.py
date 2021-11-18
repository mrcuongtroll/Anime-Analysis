import scrapy
import requests
import json
from ..items import AnimeItem

class KitsusearchSpider(scrapy.Spider):
    name = "kitsusearch"
    url = 'https://kitsu.io/api/edge/anime/'
    start_urls = []

    for i in range(20001):
        start_urls.append(url + str(i))

    def parse(self, response):
        item = AnimeItem()

        d = response.text
        j = json.loads(d)

        item['title'] = j['data']['attributes']['canonicalTitle'].lower().strip()
        item['romaji_title'] = j['data']['attributes']['titles']['en_jp'].lower().strip()
        item['english_title'] = j['data']['attributes']['titles']['en'].lower().strip()
        item['status'] = j['data']['attributes']['status'].lower().strip()
        item['episodes'] = str(j['data']['attributes']['episodeCount']).strip()
        item['media_type'] = j['data']['attributes']['showType'].lower().strip()
        item['duration'] = (str(j['data']['attributes']['episodeLength']) +' min')
        #item['season']
        item['start_date'] = j['data']['attributes']['startDate']
        item['end_date'] = j['data']['attributes']['endDate']
        #item['genres'] = j[]

        yield item


