import json



#
# for anime in merged_data:
#     for tag in tags:
#         if 'tags' in anime.keys():
#             if anime['tags']:
#                 if tag in anime['tags']:
#                     anime[f'tag_{tag}'] = True
#         anime[f'tag_{tag}'] = False
#     del anime['tags']
#     for genre in genres:
#         if 'genres' in anime.keys():
#             if anime['genres']:
#                 if genre in anime['genres']:
#                     anime[f'genre_{genre}'] = True
#         anime[f'genre_{genre}'] = False
#     del anime['genres']
#
#
#
#
#
# for anime in merged_data_with_title_as_key:
#     for tag in tags:
#         if merged_data_with_title_as_key[anime]['tags']:
#             if tag in merged_data_with_title_as_key[anime]['tags']:
#                 merged_data_with_title_as_key[anime][f'tag_{tag}'] = True
#         merged_data_with_title_as_key[anime][f'tag_{tag}'] = False
#     del merged_data_with_title_as_key[anime]['tags']
#     for genre in genres:
#         if merged_data_with_title_as_key[anime]['genres']:
#             if genre in merged_data_with_title_as_key[anime]['genres']:
#                 merged_data_with_title_as_key[anime][f'genre_{genre}'] = True
#         merged_data_with_title_as_key[anime][f'genre_{genre}'] = False
#     del merged_data_with_title_as_key[anime]['genres']
#

if __name__ == '__main__':
    with open('../data/preprocessed/kitsu_data.json', 'r', encoding='ISO-8859-1') as f:
        data = json.loads(f.read())
        print(data[0])
