import json


def preprocess_anisearch(read_path, write_path):
    with open(read_path, 'r') as f:
        data = json.loads(f.read())
    for anime in data:
        if anime['episodes']:
            anime['episodes'] = int(anime['episodes'])
        else:
            anime['episodes'] = None
        try:
            anime['duration'] = int(anime['duration'].replace('min', '').strip())
        except ValueError:
            anime['duration'] = None
        anime['mean_score_anisearch'] = float9=(anime['mean_score_anisearch'])
        if anime['popularity_anisearch']:
            anime['popularity_anisearch'] = int(anime['popularity_anisearch'])
        else:
            anime['popularity_anisearch'] = None
        anime['favorites_anisearch'] = int(anime['favorites_anisearch'])
        anime['status_completed_anisearch'] = int(anime['status_completed_anisearch'])
        anime['status_planning_anisearch'] = int(anime['status_planning_anisearch'])
        anime['status_current_anisearch'] = int(anime['status_current_anisearch'])
        anime['status_paused_anisearch'] = int(anime['status_paused_anisearch'])
        anime['status_dropped_anisearch'] = int(anime['status_dropped_anisearch'])
        anime['number_scorer_anisearch'] = int(anime['number_scorer_anisearch'])
    with open(write_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    read_path = '../Anime-Analysis/data/raw/anisearch.json'
    write_path = '../Anime-Analysis/data/preprocessed/anisearch_preprocessed.json'
    preprocess_anisearch(read_path, write_path)