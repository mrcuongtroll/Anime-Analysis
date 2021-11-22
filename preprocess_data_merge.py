import json
import os
import string


def process_merged_data(temp_path, temp_with_key, write_path, file_name):
    with open(temp_path, 'r') as f:
        merged_data = json.load(f)
    with open(temp_with_key, 'r') as f:
        merged_data_with_title_as_key = json.load(f)
    # Give each anime all available attributes
    keys_list = []
    for anime in merged_data:
        for key in anime.keys():
            if key not in keys_list:
                keys_list.append(key)
    genres = []
    tags = []

    # For merged_data:
    for anime in merged_data:
        for key in keys_list:
            if key in anime.keys():
                if isinstance(anime[key], str):
                    anime[key] = anime[key].lower()
                    if anime[key] == '' or anime[key] == '?':
                        anime[key] = None
                elif isinstance(anime[key], list):
                    for i in range(len(anime[key])):
                        if isinstance(anime[key][i], str):
                            anime[key][i] = anime[key][i].lower()
                elif isinstance(anime[key], int):
                    if anime[key] == -1:
                        anime[key] = None
            else:
                anime[key] = None
            if key == 'genres' and anime['genres']:
                for genre in anime['genres']:
                    if genre not in genres:
                        genres.append(genre)
            if key == 'tags' and anime['tags']:
                for tag in anime['tags']:
                    if tag not in tags:
                        tags.append(tag)

    # For merged_data_with_title_as_key:
    for anime in merged_data_with_title_as_key:
        for key in keys_list:
            if key in merged_data_with_title_as_key[anime].keys():
                if isinstance(merged_data_with_title_as_key[anime][key], str):
                    merged_data_with_title_as_key[anime][key] = merged_data_with_title_as_key[anime][key].lower()
                    if merged_data_with_title_as_key[anime][key] == '' or merged_data_with_title_as_key[anime][key] == '?':
                        merged_data_with_title_as_key[anime][key] = None
                elif isinstance(merged_data_with_title_as_key[anime][key], list):
                    for i in range(len(merged_data_with_title_as_key[anime][key])):
                        if isinstance(merged_data_with_title_as_key[anime][key][i], str):
                            merged_data_with_title_as_key[anime][key][i] = merged_data_with_title_as_key[anime][key][i].lower()
                elif isinstance(merged_data_with_title_as_key[anime][key], int):
                    if merged_data_with_title_as_key[anime][key] == -1:
                        merged_data_with_title_as_key[anime][key] = None
            else:
                merged_data_with_title_as_key[anime][key] = None
            if key == 'genres' and merged_data_with_title_as_key[anime]['genres']:
                for genre in merged_data_with_title_as_key[anime]['genres']:
                    if genre not in genres:
                        genres.append(genre)
            if key == 'tags' and merged_data_with_title_as_key[anime]['tags']:
                for tag in merged_data_with_title_as_key[anime]['tags']:
                    if tag not in tags:
                        tags.append(tag)

    # Save merged data (in json format)
    with open(os.path.join(write_path, file_name + '.json'), 'w') as f:
        json.dump(merged_data, f, indent=3)
    with open(os.path.join(write_path, file_name + '_with_title_as_key.json'), 'w') as f:
        json.dump(merged_data_with_title_as_key, f, indent=3)

    with open(os.path.join(os.path.split(temp_path)[0], 'genres.json'), 'w') as f:
        json.dump(genres, f, indent=3)
    with open(os.path.join(os.path.split(temp_path)[0], 'tags.json'), 'w') as f:
        json.dump(tags, f, indent=3)
    return


def merge1(read_path, temp_path, ref_path, ref_name, file_name, keywords_path):
    merged_data = []
    merged_data_with_title_as_key = {}
    with open(ref_path, 'r') as f:
        ref = json.load(f)
    with open(keywords_path, 'r') as f:
        keywords = json.load(f)

    # Merge data from files into the ref dict
    for file in os.listdir(read_path):
        if file == ref_name:
            continue
        with open(os.path.join(read_path, file), 'r', encoding='ISO-8859-1') as f:
            data = json.load(f)
            for anime in data:
                title = anime['title'].lower()
                if ':' in title:
                    keyword = title.split(':')[0]
                    if keyword not in keywords:
                        keywords.append(keyword)
                for punc in string.punctuation:
                    title = title.replace(punc, '')
                title = title.replace('  ', ' ')
                if title in ref.keys():
                    merge_anime(ref[title], anime)
                else:
                    tags = []
                    keys = list(anime.keys())
                    for key in keys:
                        if 'tags_' in key:
                            tags += anime[key]
                            del anime[key]
                    anime['tags'] = tags
                    ref[title] = anime

    with open(ref_path, 'w') as f:
        json.dump(ref, f, indent=3)
    with open(os.path.join(temp_path, file_name + '.json'), 'w') as f:
        json.dump(merged_data, f, indent=3)
    with open(os.path.join(temp_path, file_name + '_with_title_as_key.json'), 'w') as f:
        json.dump(merged_data_with_title_as_key, f, indent=3)
    with open(keywords_path, 'w') as f:
        json.dump(keywords, f, indent=2)
    return


def merge2(ref_data, ref_file, temp_file, temp_with_key):
    # Merge animes with multiple titles in the ref dict and put into the merged data list/dict
    merged_data = []
    merged_data_with_title_as_key = {}
    with open(ref_file, 'r') as f:
        ref = json.load(f)
    titles = list(ref.keys())
    with open(ref_data, 'r') as f:
        ref_data = json.load(f)
        for anime in ref_data:
            if anime['english_title'] != '':
                english_title = anime['english_title'].lower()
                for punc in string.punctuation:
                    english_title = english_title.replace(punc, '')
                english_title = english_title.replace('  ', ' ')
                try:
                    titles.remove(english_title)
                except ValueError:
                    pass
                if anime['romaji_title'] != '':
                    romaji_title = anime['romaji_title'].lower()
                    for punc in string.punctuation:
                        romaji_title = romaji_title.replace(punc, '')
                    romaji_title = romaji_title.replace('  ', ' ')
                    try:
                        titles.remove(romaji_title)
                    except ValueError:
                        pass
                    merge_anime(ref[english_title], ref[romaji_title])
                if anime['title'] != '':
                    title = anime['title'].lower()
                    for punc in string.punctuation:
                        title = title.replace(punc, '')
                    title = title.replace('  ', ' ')
                    try:
                        titles.remove(title)
                    except ValueError:
                        pass
                    merge_anime(ref[english_title], ref[title])
                merged_data_with_title_as_key[english_title] = ref[english_title]
                merged_data.append(ref[english_title])
            elif anime['title'] != '':
                title = anime['title'].lower()
                for punc in string.punctuation:
                    title = title.replace(punc, '')
                title = title.replace('  ', ' ')
                try:
                    titles.remove(title)
                except ValueError:
                    pass
                if anime['romaji_title'] != '':
                    romaji_title = anime['romaji_title'].lower()
                    for punc in string.punctuation:
                        romaji_title = romaji_title.replace(punc, '')
                    romaji_title = romaji_title.replace('  ', ' ')
                    try:
                        titles.remove(romaji_title)
                    except ValueError:
                        pass
                    merge_anime(ref[title], ref[romaji_title])
                merged_data_with_title_as_key[title] = ref[title]
                merged_data.append(ref[title])
    for title in titles:
        merged_data.append(ref[title])
        merged_data_with_title_as_key[title] = ref[title]
    with open(temp_file, 'w') as f:
        json.dump(merged_data, f, indent=3)
    with open(temp_with_key, 'w') as f:
        json.dump(merged_data_with_title_as_key, f, indent=3)
    return


def title_as_key(filepath, savepath, keywords_path):
    """
    :param filepath: path to the reference data file (json file)
    :param savepath: path to save preprocessed data
    :return: None
    """
    data = {}
    keywords = []
    with open(filepath, 'r') as f:
        ref_data = json.load(f)
    for anime in ref_data:
        if 'english_title' in anime.keys() and anime['english_title'] != '':
            english_title = anime['english_title'].lower()
            if ':' in english_title:
                keyword = english_title.split(':')[0]
                if keyword not in keywords:
                    keywords.append(keyword)
            for punc in string.punctuation:
                english_title = english_title.replace(punc, '')
            english_title = english_title.replace('  ', ' ')
            data[english_title] = anime
        if 'romaji_title' in anime.keys() and anime['romaji_title'] != '':
            romaji_title = anime['romaji_title'].lower()
            if ':' in romaji_title:
                keyword = romaji_title.split(':')[0]
                if keyword not in keywords:
                    keywords.append(keyword)
            for punc in string.punctuation:
                romaji_title = romaji_title.replace(punc, '')
            romaji_title = romaji_title.replace('  ', ' ')
            data[romaji_title] = anime
        if 'title' in anime.keys() and anime['title'] != '':
            title = anime['title'].lower()
            if ':' in title:
                keyword = title.split(':')[0]
                if keyword not in keywords:
                    keywords.append(keyword)
            for punc in string.punctuation:
                title = title.replace(punc, '')
            title = title.replace('  ', ' ')
            data[title] = anime
    with open(savepath, 'w') as f:
        json.dump(data, f, indent=2)
    with open(keywords_path, 'w') as f:
        json.dump(keywords, f, indent=2)
    return


def merge_anime(target, source):
    source_keys = list(source.keys())
    for new_key in source_keys:
        if new_key not in target.keys() and 'tags' not in new_key:
            target[new_key] = source[new_key]
        if new_key == 'genres':
            if source['genres']:
                for genre in source['genres']:
                    if genre.lower() not in target['genres']:
                        target['genres'].append(genre.lower())
        if 'tags' in new_key:
            tags = []
            if source[new_key]:
                for tag in source[new_key]:
                    tags.append(tag.lower())
            target['tags'] = tags
        if 'tags_' in new_key:
            del source[new_key]
    target_keys = list(target.keys())
    for key in target_keys:
        if 'tags' in key:
            if target[key]:
                for tag in target[key]:
                    if 'tags' not in target.keys():
                        target['tags'] = []
                    if tag.lower() not in target['tags']:
                        target['tags'].append(tag.lower())
            if '_' in key:
                del target[key]
    return


if __name__ == '__main__':
    title_as_key(filepath='../Anime-Analysis/data/preprocessed/anilist_data_preprocessed.json',
                 savepath='../Anime-Analysis/data/reference/anilist_data_ref.json',
                 keywords_path='../Anime-Analysis/data/keywords.json')

    merge1(read_path='../Anime-Analysis/data/preprocessed',
           temp_path='../Anime-Analysis/data/temporary',
           ref_path='../Anime-Analysis/data/reference/anilist_data_ref.json',
           ref_name='anilist_data_preprocessed.json',
           file_name='merged_anime_data',
           keywords_path='../Anime-Analysis/data/keywords.json')

    merge2(ref_data='../Anime-Analysis/data/preprocessed/anilist_data_preprocessed.json',
           ref_file='../Anime-Analysis/data/reference/anilist_data_ref.json',
           temp_file='../Anime-Analysis/data/temporary/merged_anime_data.json',
           temp_with_key='../Anime-Analysis/data/temporary/merged_anime_data_with_title_as_key.json')

    process_merged_data(temp_path='../Anime-Analysis/data/temporary/merged_anime_data.json',
                        temp_with_key='../Anime-Analysis/data/temporary/merged_anime_data_with_title_as_key.json',
                        write_path='../Anime-Analysis/data/merged',
                        file_name='merged_anime_data')
