import requests
import json
import time

url_anime = 'https://kitsu.io/api/edge/anime/'
url_genres = 'https://kitsu.io/api/edge/genres/'

preprocess_data = []

for i in range(4000, 10000):
    # if i % 10 == 0:
    #     time.sleep(3)

    x_1 = requests.get(url_anime + str(i))
    x_2 = requests.get(url_genres + str(i))

    d_1 = x_1.text
    d_2 = x_2.text

    j = json.loads(d_1)
    jk = json.loads(d_2)

    if "errors" in jk.keys():
        pass
    if "errors" in j.keys():
        pass

    anime = {}

    try:
        if "errors" not in j.keys():
            anime['id'] = i
        else:
            pass

    except:
        pass

    try:
        anime['title'] = j['data']['attributes']['canonicalTitle'].lower().strip()
    except:
        pass

    try:
        anime['romaji_title'] = j['data']['attributes']['titles']['en_jp'].lower().strip()
    except:
        pass

    try:
        anime['english_title'] = j['data']['attributes']['titles']['en'].lower().strip()
    except:
        pass

    try:
        anime['status'] = j['data']['attributes']['status'].lower().strip()
    except:
        pass

    try:
        anime['episodes'] = j['data']['attributes']['episodeCount']
    except:
        pass

    try:
        anime['media_type'] = j['data']['attributes']['showType'].lower().strip()
    except:
        pass

    try:
        anime['duration'] = j['data']['attributes']['episodeLength']
    except:
        pass

    try:
        anime['start_date'] = j['data']['attributes']['startDate']
    except:
        pass

    try:
        anime['end_date'] = j['data']['attributes']['endDate']
    except:
        pass

    try:
        anime['age'] = j['data']['attributes']['ageRating'].lower().strip()
    except:
        pass

    try:
        anime['mean_score_kitsu'] = round((float((j['data']['attributes']['averageRating'].strip())) / 10), 2)
    except:
        pass

    try:
        anime['popularity_rank_kitsu'] = j['data']['attributes']['popopularityRank']
    except:
        pass

    try:
        anime['favorite_count_kitsu'] = j['data']['attributes']['favoritesCount']
    except:
        pass

    try:
        anime['rating_rank_kitsu'] = j['data']['attributes']['ratingRank']
    except:
        pass

    try:
        anime['user_count_kitsu'] = j['data']['attributes']['userCount']
    except:
        pass

    try:
        genres = []
        main_genre = jk['data']['attributes']['name']
        if main_genre:
            genres.append(main_genre)
            anime['genres'] = genres
        else:
            anime['genres'] = ''
    except:
        pass

    preprocess_data.append(anime)

with open('anime.json', 'w') as f:
    json.dump(preprocess_data, f)
# print(preprocess_data)
