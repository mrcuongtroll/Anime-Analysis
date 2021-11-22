import json
import os
import string


def enumerate_values(data, attr):
    values = []
    if isinstance(data, list):
        for anime in data:
            values.append(anime[attr])
    elif isinstance(data, dict):
        for anime in data:
            values.append(data[anime][attr])
    return set(values)


if __name__ == '__main__':
    with open('../Anime-Analysis/data/merged/merged_anime_data_with_title_as_key.json', 'r') as f:
        merged_data = json.load(f)
    status_map = {'currently_airing': 'ongoing',
                  'current': 'ongoing',
                  'ongoing': 'ongoing',
                  'releasing': 'ongoing',
                  'upcoming': 'upcoming',
                  'aborted': 'cancelled',
                  'cancelled': 'cancelled',
                  'finished_airing': 'finished',
                  'completed': 'finished',
                  'finished': 'finished',
                  'not_yet_aired': 'not yet released',
                  'not yet released': 'not yet released',
                  'tba': 'tba',
                  'on hold': 'on hold'}
    source_map = {'game': 'video game',
                  'video game': 'video game',
                  'other': 'other',
                  'original work': 'original work',
                  'comic': 'comic',
                  'picture book': 'picture book',
                  'digital_manga': 'manga',
                  'web novel': 'web novel',
                  'novel': 'novel',
                  'visual novel': 'visual novel',
                  'light novel': 'light novel',
                  'card_game': 'video game',
                  'manhua': 'manhua',
                  'web_manga': 'manga',
                  'book': 'book',
                  'original': 'original work',
                  'multimedia project': 'multimedia project',
                  '4_koma_manga': '4_koma_manga',
                  'live action': 'live action',
                  'manwha': 'manwha',
                  'light_novel': 'light novel',
                  'radio': 'radio',
                  'visual_novel': 'visual novel',
                  'anime': 'anime',
                  'doujinshi': 'doujinshi',
                  'music': 'music',
                  'picture_book': 'picture book',
                  'manga': 'manga'}
    type_map = {'movie': 'movie',
                'other': 'other',
                'ona': 'ona',
                'special': 'special',
                'tv': 'tv',
                'ova': 'ova',
                'music': 'music',
                'tv short': 'tv short',
                'tv-series': 'tv',
                'bonus': 'bonus',
                'unknown': None,
                'tv-special': 'special',
                'music video': 'music',
                'cm': 'cm',
                'web': 'web'}
    single_valued = []
    multi_valued = []
    single_valued_dict = {}
    multi_valued_dict = {}
    for anime in merged_data:
        m = {'title': anime}
        s = {'title': anime}
        md = {}
        sd = {}
        del merged_data[anime]['id']
        if merged_data[anime]['status']:
            merged_data[anime]['status'] = status_map[merged_data[anime]['status']]
        if merged_data[anime]['source']:
            merged_data[anime]['source'] = source_map[merged_data[anime]['source'].split(',')[0].strip()]
        if merged_data[anime]['media_type']:
            merged_data[anime]['media_type'] = type_map[merged_data[anime]['media_type'].split('\n')[0].strip()]
        if merged_data[anime]['anilist_url']:
            merged_data[anime]['anilist_url'] = merged_data[anime]['anilist_url'][0]
        for key in merged_data[anime].keys():
            if isinstance(merged_data[anime][key], list):
                m[key] = merged_data[anime][key]
                md[key] = merged_data[anime][key]
            else:
                sd[key] = merged_data[anime][key]
                if key != 'title':
                    s[key] = merged_data[anime][key]
        single_valued.append(s)
        multi_valued.append(m)
        single_valued_dict[anime] = sd
        multi_valued_dict[anime] = md
    with open('../Anime-Analysis/data/split/single_valued_list.json', 'w') as f:
        json.dump(single_valued, f, indent=3)
    with open('../Anime-Analysis/data/split/multi_valued_list.json', 'w') as f:
        json.dump(multi_valued, f, indent=3)
    with open('../Anime-Analysis/data/split/single_valued_dict.json', 'w') as f:
        json.dump(single_valued_dict, f, indent=3)
    with open('../Anime-Analysis/data/split/multi_valued_dict.json', 'w') as f:
        json.dump(multi_valued_dict, f, indent=3)
