import requests
import json
import time


def get_anime_batch(access_token: str, limit: int, offset: int):
    base_url = f"https://api.myanimelist.net/v2/anime/ranking?ranking_type=bypopularity&limit={limit}&offset={offset}&fields="
    fields = ["id", "title", "alternative_titles", "mean", "num_list_users", "num_scoring_users",
     "num_favorites", "average_episode_duration", "genres", "start_date", "end_date", "start_season",
     "media_type", "num_episodes", "status", "source", "studios", "related_anime", "rating"]

    url = base_url + ','.join(fields)
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })

    response.raise_for_status()
    batch = response.json()
    response.close()

    return batch


if __name__ == "__main__":
    with open("token.json", "r") as file:
        token = json.load(file)

    for offset in range(0, 19500, 500):
        batch = get_anime_batch(token["access_token"], 500, offset)
        anime_list = [anime["node"] for anime in batch["data"]]
        with open(f"data/data{offset}.json", 'w') as file:
            json.dump(anime_list, file, indent=4)
        print(offset)
