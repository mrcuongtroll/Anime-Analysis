import json

with open('anilist_data.json','r') as f:
    data = json.load(f)

print(len(data))

preprocessed =[]
problems = []
def duration_preprocess(s):
    duration = 0
    l = s.split(',')
    if len(l) == 2:
        duration += int(l[0].split()[0])*60
        duration += int(l[1].split()[0])
    else:
        if 'hour' in s:
            duration += int(s.split()[0])*60
        else:
            duration += int(s.split()[0])
    return duration

problem_counter =0
for item in data:
    anime = {}
    try:
        title = item['romaji_title'][0].lower() if len(item['romaji_title']) >0 else ''
        anime['romaji_title'] = title
        anime['english_title'] = item['english_title'][0].lower() if len(item['english_title']) >0 else ''

        if title == '':
            title = anime['english_title']
        anime['title'] = title
        anime['mean_score_anilist'] = float(item["mean_score"][0][:-1])/100 if len(item['mean_score']) > 0 else -1
        anime['weighted_score_anilist'] = float(item["avg_score"][0][:-1])/100 if len(item['avg_score']) > 0 else -1
        anime['popularity_anilist'] = int(item['popularity'][0]) if len(item['popularity']) > 0 else -1
        anime['favorites_anilist'] = int(item['favorites'][0]) if len(item['favorites']) > 0 else -1
        anime['duration'] = duration_preprocess(item['duration'][0]) if len(item['duration']) > 0 else -1
        anime['status'] = item['status'][0].lower() if len(item['status']) >0 else ''
        anime['episodes'] =  int(item['episodes'][0]) if len(item['episodes']) > 0 else -1
        anime['source'] =  item['source'][0].lower() if len(item['source']) >0 else ''
        anime['genres'] = [s.lower() for s in item['genres']]
        anime['season_season'] = item['season'][0].split()[0].lower() if len(item['season']) >0 else ''
        anime['season_year'] = int(item['season'][0].split()[1]) if len(item['season']) >0 else -1
        anime['media_type'] = item['format'][0].lower() if len(item['format']) >0 else ''
        anime['anilist_url'] = item['url']
        anime['studios'] = [s.lower() for s in item['studios']]
        anime['producers'] = [s.lower() for s in item['producers']]
        anime['creator'] = item['og_creator'][0].lower() if len(item['og_creator']) >0 else ''
        anime['tags_anilist'] = [s.lower() for s in item['tags']]
        anime['prequel'] = item['prequel'][0].lower() if len(item['prequel']) >0 else ''
        anime['sequel'] = item['sequel'][0].lower() if len(item['sequel']) >0 else ''
        anime['voice_actors'] = [s.lower() for s in item['voice_actors']]
        anime['directors'] = item['director'][0].lower() if len(item['director']) >0 else ''
        anime['status_completed_anilist'] = int(item['status_completed']) if len(item['status_completed']) > 0 else -1
        anime['status_planning_anilist'] = int(item['status_planning']) if len(item['status_planning']) > 0 else -1
        anime['status_current_anilist'] = int(item['status_current']) if len(item['status_current']) > 0 else -1
        anime['status_paused_anilist'] = int(item['status_paused']) if len(item['status_paused']) > 0 else -1
        anime['status_dropped_anilist'] = int(item['status_dropped']) if len(item['status_dropped']) > 0 else -1
        preprocessed.append(anime)
    except:
        anime['status_completed_anilist'] = -1
        anime['status_planning_anilist'] =  -1
        anime['status_current_anilist'] = -1
        anime['status_paused_anilist'] = -1
        anime['status_dropped_anilist'] = -1
        problem = item.copy()
        problems.append(problem)
        problem_counter+=1
print(len(preprocessed),problem_counter)

with open('../data/preprocessed/anilist_data_preprocessed.json', 'w') as outfile:
    json.dump(preprocessed, outfile, indent=2)
