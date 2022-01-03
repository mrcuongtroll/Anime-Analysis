"""
To scrape data using this scrape, use the command line:
     scrapy crawl anisearch -o file_name.json
in the directory ./anime
"""
import scrapy
from ..items import AnimeItem


class AnisearchSpider(scrapy.Spider):
    name = 'anisearch'
    start_urls = ['https://www.anisearch.com/anime/index']
    page_number = 1

    def parse(self, response, **kwargs):
        for anime in response.css('ul.covers.gallery > li'):
            anime_link = anime.css('a::attr("href")').get()
            anime_link = 'https://www.anisearch.com/' + anime_link
            yield scrapy.Request(url=anime_link, callback=self.parse_anime)
        AnisearchSpider.page_number += 1
        next_page = 'https://www.anisearch.com/anime/index/page-' + str(AnisearchSpider.page_number)
        if AnisearchSpider.page_number <= 404:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_anime(self, response):
        anime = AnimeItem()

        title = response.css('#htitle::text').get()
        anime['title'] = title.lower()
        # romaji_title = response.css('strong+ .grey::text').get()
        # if romaji_title:
        #     anime['romaji_title'] = romaji_title.lower()
        # else:
        #     anime['romaji_title'] = ''
        # english_title = response.css('div.title > strong::text').get()
        # anime['english_title'] = english_title.lower()

        atype = response.css('div.type::text').get()
        if atype:
            atype = atype.split(',')
            media_type = atype[0].strip()
            num_episodes = atype[1].strip()
            anime['media_type'] = media_type.lower().strip()
            anime['episodes'] = num_episodes.lower()
        else:
            anime['media_type'] = ''
            anime['episodes'] = ''

        duration = response.css('time::text').get()
        if duration:
            duration = duration.replace('\u202f', ' ')
            anime['duration'] = duration.lower()
        else:
            anime['duration'] = ''

        status = response.css('div.status::text').get()
        if status:
            anime['status'] = status.lower().strip()
        else:
            anime['status'] = ''

        released_date = response.css('div.released::text').get()
        if released_date:
            released_date = released_date.split(u"‑")
            start_date = released_date[0].strip()
            start_date = start_date.split('.')
            start_date.reverse()
            start_date = '-'.join(start_date)
            anime['start_date'] = start_date.lower()
            if len(released_date) == 2:
                end_date = released_date[1].strip()
                end_date = end_date.split('.')
                end_date.reverse()
                end_date = '-'.join(end_date)
            else:
                end_date = ''
            anime['end_date'] = end_date.lower()
        else:
            anime['start_date'] = ''
            anime['end_date'] = ''

        studios = []
        for studio in response.css('ul.xlist.row.simple li:nth-child(1) > div.company > a::text'):
            studios.append(studio.get().lower())
        anime['studios'] = studios

        source = response.css('div.adapted::text').get()
        if source:
            anime['source'] = source.lower().strip()
        else:
            anime['source'] = ''

        target_group = response.css('div.targets::text').get()
        if target_group:
            target_group = target_group.split(',')
            for i in range(len(target_group)):
                target_group[i] = target_group[i].strip().lower()
            anime['target_group'] = target_group
        else:
            anime['target_group'] = []

        genres = []
        main_genre = response.css('ul.cloud > li > a.gg.showpop::text').get()
        if main_genre:
            genres.append(main_genre.lower())
        for genre in response.css('ul.cloud > li > a.gc.showpop::text'):
            genre = genre.get()
            if genre not in genres:
                genres.append(genre.lower())
        anime['genres'] = genres

        tags = []
        for tag in response.css('ul.cloud > li > a.gt.showpop::text'):
            tags.append(tag.get().lower())
        anime['tags_anisearch'] = tags

        rating = response.css('#ratingstats tr:nth-child(2) td:nth-child(1) > span::text').get()
        if rating:
            rating = rating.split('=')
            mean_score = str(float(rating[0].strip())*2)
            anime['mean_score_anisearch'] = mean_score
        else:
            anime['mean_score_anisearch'] = ''

        rank = response.css('#ratingstats tr:nth-child(2) td:nth-child(2) > span::text').get()
        if rank:
            rank = rank.replace('#', '')
            anime['popularity_anisearch'] = rank
        else:
            anime['popularity_anisearch'] = ''

        favourites = response.css('tr:nth-child(4) span::text').get()
        if favourites:
            anime['favorites_anisearch'] = favourites.replace('.', '').replace(',', '')
        else:
            anime['favorites_anisearch'] = '0'

        status_completed = response.css('.rtype2 span::text').get()
        if status_completed:
            anime['status_completed_anisearch'] = status_completed.replace('.', '').replace(',', '')
        else:
            anime['status_completed_anisearch'] = '0'

        status_planning = response.css('.rtype6 span::text').get()
        if status_planning:
            anime['status_planning_anisearch'] = status_planning.replace('.', '').replace(',', '')
        else:
            anime['status_planning_anisearch'] = '0'

        status_current = response.css('.rtype1 span::text').get()
        if status_current:
            anime['status_current_anisearch'] = status_current.replace('.', '').replace(',', '')
        else:
            anime['status_current_anisearch'] = '0'

        status_paused = response.css('.rtype3 span::text').get()
        if status_paused:
            anime['status_paused_anisearch'] = status_paused.replace('.', '').replace(',', '')
        else:
            anime['status_paused_anisearch'] = '0'

        status_dropped = response.css('.rtype4 span::text').get()
        if status_dropped:
            anime['status_dropped_anisearch'] = status_dropped.replace('.', '').replace(',', '')
        else:
            anime['status_dropped_anisearch'] = '0'

        # Get number of users that rated the anime:
        number_scorer = 0
        for i in range(5):
            star_i = response.css('li:nth-child('+ str(i+1) + ') .value::text').get()
            if star_i:
                number_scorer += int(star_i.replace('.', '').replace(',', ''))
        anime['number_scorer_anisearch'] = str(number_scorer)

        anime['url'] = response.request.url
        # anime['url'] = response.css('meta[property="og:url"]::attr("content")').get()

        yield anime
