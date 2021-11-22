import json


def json_formatter(filepath, savepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    with open(savepath, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    path = '../Anime-Analysis/data/preprocessed/anilist_data_preprocessed.json'
    json_formatter(path, path)