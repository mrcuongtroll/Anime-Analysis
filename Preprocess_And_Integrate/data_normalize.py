'''
This is after the step of splitting the merged data into single-valued and multi-valed.
Convert json file of multi-valued attributes to dummy coding tables, then save that data as csv files.
'''
import json
import pandas as pd

with open('../data/split/single_valued_list.json', 'r') as f:
    single_valued_data = json.load(f)
with open('../data/split/multi_valued_list.json', 'r') as f:
    multi_valued_data = json.load(f)


single_valued_df = pd.DataFrame(single_valued_data)
multi_valued_cols = list(multi_valued_data[0].keys())[1:]
single_valued_df = single_valued_df.drop(multi_valued_cols, 1)
single_valued_df.to_csv('../data/csv/title_single_valued_attrs.csv', index = False)

def atomize_multivalued_attr(data, attr):
    value_list = []

    for anime_raw in data:
        try:
            for item in anime_raw[attr]:
                if item not in value_list:
                    value_list.append(item)
        except:
            pass

    title_attr_relation = []

    for anime_raw in data:
        anime = {}
        anime["title"] = anime_raw["title"]
        for value in value_list:
            anime[value] = 0
        try:
                for value in anime_raw[attr]:
                    anime[value] = 1
        except: pass
        title_attr_relation.append(anime)

    return title_attr_relation


for attr in multi_valued_cols:
    if attr == 'studios':
        title_attr_relation = atomize_multivalued_attr(multi_valued_data, attr)
        title_attr_relation_df = pd.DataFrame(title_attr_relation)
        file_name = '../data/csv/title_'+attr+'.csv'
        title_attr_relation_df.to_csv(file_name, index = False)
        print(file_name)
