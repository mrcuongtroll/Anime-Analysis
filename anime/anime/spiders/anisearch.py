import scrapy
from ..items import AnimeItem

class AnidbSpider(scrapy.Spider):
    name = 'anisearch'
    start_urls = ['https://www.anisearch.com/anime/index']

    def parse(self, response, **kwargs):
        for anime in response.css('ul.covers.gallery > li'):
            anime_link = anime.css('a::attr("href")').get()
            yield response.follow(url=anime_link, callback=self.parse_anime)
        next_page = response.css('ul.pagenav > li > a.pagenav-next::attr("href")').get()
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse)

    def parse_anime(self, response):
        anime = AnimeItem()

        title = response.css('div.title > strong::text').get()
        anime['title'] = title

        atype = response.css('div.type::text').get()
        if atype:
            atype = atype.split(',')
            media_type = atype[0].strip()
            num_episodes = atype[1].strip()
            anime['media_type'] = media_type
            anime['num_episodes'] = num_episodes
        else:
            anime['media_type'] = ''
            anime['num_episodes'] = ''

        duration = response.css('time::text').get()
        if duration:
            duration = duration.replace('\u202f', ' ')
            anime['duration'] = duration
        else:
            anime['duration'] = ''

        status = response.css('div.status::text').get()
        if status:
            anime['status'] = status
        else:
            anime['status'] = ''

        released_date = response.css('div.released::text').get()
        if released_date:
            released_date = released_date.split(u"‑")
            start_date = released_date[0].strip()
            anime['start_date'] = start_date
            if len(released_date) == 2:
                end_date = released_date[1].strip()
            else:
                end_date = ''
            anime['end_date'] = end_date
        else:
            anime['start_date'] = ''
            anime['end_date'] = ''

        studios = []
        for studio in response.css('ul.xlist.row.simple li:nth-child(1) > div.company > a::text'):
            studios.append(studio.get())
        anime['studios'] = studios

        source = response.css('div.adapted::text').get()
        if source:
            anime['source'] = source
        else:
            anime['source'] = ''

        target_group = response.css('div.targets::text').get()
        if target_group:
            target_group = target_group.split(',')
            for i in range(len(target_group)):
                target_group[i] = target_group[i].strip()
            anime['target_group'] = target_group
        else:
            anime['target_group'] = []

        genres = []
        main_genre = response.css('ul.cloud > li > a.gg.showpop::text').get()
        if main_genre:
            genres.append(main_genre)
        for genre in response.css('ul.cloud > li > a.gc.showpop::text'):
            genre = genre.get()
            if genre not in genres:
                genres.append(genre)
        anime['genres'] = genres

        tags = []
        for tag in response.css('ul.cloud > li > a.gt.showpop::text'):
            tags.append(tag.get())
        anime['tags'] = tags

        rating = response.css('#ratingstats tr:nth-child(2) td:nth-child(1) > span::text').get()
        if rating:
            rating = rating.split('=')
            score = str(float(rating[0].strip())*2)
            anime['score'] = score
        else:
            anime['score'] = ''

        rank = response.css('#ratingstats tr:nth-child(2) td:nth-child(2) > span::text').get()
        if rank:
            rank = rank.replace('#', '')
            anime['rank'] = rank
        else:
            anime['rank'] = ''

        yield anime
