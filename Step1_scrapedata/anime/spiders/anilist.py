'''
To scrape data using this scrape, use the command line:
     scrapy crawl anilist -o file_name.json
in the directory ./anime
'''

import scrapy
from anime.items_anilist import AnilistScraperItem
from datetime import datetime
import re

import requests
import json
import time


class AnilistScraper(scrapy.Spider):
    '''
    We can get anime urls through ranking page. However, the ranking page itself
    is not static, and uses POST method, which makes it harder for the bot in
    scrapy to load more contents.
    To avoid this hassle, we use the API to get anime ids, which can be used to
    generate individual anime info page urls.
    The anime info pages are static, so we can get the data conveniently.

    The fastest way to get all the data is by using only API. This is for the
    purpose of practice scraping using Scrapy.
    '''

    name = "anilist"


    #Getting anime ids, then create anime urls.
    page = 1
    # Here we define our query
    query = '''
    query($page:Int){
      Page (page: $page, perPage:50){
        pageInfo {
          hasNextPage
        }
        media(sort: POPULARITY_DESC, type: ANIME){
            id
        }
      }
    }
    '''

    variables = {
        'page': page
    }

    url = 'https://graphql.anilist.co'
    start_urls = []
    hasNextPage = True

    while hasNextPage:
        try:
            time.sleep(1)
            print("Getting anime ids on popularity pagination #", page)
            variables['page'] = page
            response = requests.post(url, json={'query': query, 'variables': variables})
            batch = response.json()
            start_urls += ['https://anilist.co/anime/'+ str(media['id']) for media in batch['data']['Page']['media']]
            hasNextPage = batch['data']['Page']['pageInfo']['hasNextPage']

        except:
            print('Problem getting pagination #', page)
            if i== 1e4:
                break
            pass

        page+=1

    print('Finished scraping anime ids from Anilist. There are',len(start_urls),'animes total.')

    #parse through each anime info page to get data
    def parse(self, response, **kwargs):
        item = AnilistScraperItem()

        item['format'] = [s.strip() for s in response.xpath("//div[text() = 'Format']/following-sibling::div/descendant::text()").extract()]
        item['episodes'] = [s.strip() for s in response.xpath("//div[text() = 'Episodes']/following-sibling::div/descendant::text()").extract()]
        item['duration'] = [s.strip() for s in response.xpath("//div[text() = '\nDuration\n']/following-sibling::div/descendant::text()").extract()]
        item['status'] = [s.strip() for s in response.xpath("//div[text() = 'Status']/following-sibling::div/descendant::text()").extract()]
        item['season'] = [s.strip() for s in response.xpath("//div[text() = 'Season']/following-sibling::a/descendant::text()").extract()]
        item['avg_score'] = [s.strip() for s in response.xpath("//div[text() = 'Average Score']/following-sibling::div/descendant::text()").extract()]
        item['mean_score'] = [s.strip() for s in response.xpath("//div[text() = 'Mean Score']/following-sibling::div/descendant::text()").extract()]
        item['popularity'] = [s.strip() for s in response.xpath("//div[text() = 'Popularity']/following-sibling::div/descendant::text()").extract()]
        item['favorites'] = [s.strip() for s in response.xpath("//div[text() = 'Favorites']/following-sibling::div/descendant::text()").extract()]
        item['studios'] = [s.strip() for s in response.xpath("//div[text() = 'Studios']/following-sibling::div/span/a/descendant::text()").extract()]
        item['producers'] = [s.strip() for s in response.xpath("//div[text() = 'Producers']/following-sibling::div/span/a/descendant::text()").extract()]
        item['source'] = [s.strip() for s in response.xpath("//div[text() = 'Source']/following-sibling::div/descendant::text()").extract()]
        item['genres'] = [s.strip() for s in response.xpath("//div[text() = 'Genres']/following-sibling::div/span/a/descendant::text()[1]").extract()]
        item['romaji_title'] = [s.strip() for s in response.xpath("//div[text() = 'Romaji']/following-sibling::div/descendant::text()").extract()]
        item['english_title'] = [s.strip() for s in response.xpath("//div[text() = 'English']/following-sibling::div/descendant::text()").extract()]
        item['tags'] = [s.strip() for s in response.xpath("//div[contains(@class,'tag')]/a/descendant::text()").extract()]
        item['prequel'] = [s.strip() for s in response.xpath("//div[text() = 'Prequel']/parent::div/following-sibling::a/descendant::text()").extract()]
        item['sequel'] = [s.strip() for s in response.xpath("//div[text() = 'Sequel']//parent::div/following-sibling::a/descendant::text()").extract()]
        item['voice_actors'] = [s.strip() for s in response.xpath("//div[contains(@class,'characters')]/div/div/div[contains(@class,'staff')]/a[contains(@class,'content')]/div[contains(@class, 'name')]/descendant::text()").extract()]
        item['director'] = [s.strip() for s in response.xpath("//div[text() = '\nOriginal Creator\n']/preceding-sibling::div/descendant::text()").extract()]
        item['og_creator'] = [s.strip() for s in response.xpath("//div[text() = '\nDirector\n']/preceding-sibling::div/descendant::text()").extract()]
        status_distribution = [s.strip() for s in response.xpath("//div[contains(@class,'statuses')]/div[contains(@class,'status')]/div[contains(@class,'amount')]/descendant::text()").extract()]
        try:
            item['status_completed'], item['status_planning'], item['status_current'], item['status_paused'], item['status_dropped'] = status_distribution[0], status_distribution[2], status_distribution[4], status_distribution[6], status_distribution[8]
        except: pass
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

        yield item
