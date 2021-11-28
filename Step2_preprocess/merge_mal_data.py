import json


data = []

for num in range(0, 19500, 500):
    with open(f"data/data{num}.json", "r") as f:
        anime_list = json.load(f)
        data.extend(anime_list)

with open("data/data.json", "w") as f:
    json.dump(data, f, indent=4)
