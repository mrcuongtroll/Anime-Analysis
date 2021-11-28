import json
import logging


def preprocess_anime(anime):
    anime_preprocessed = {}

    anime_preprocessed["id"] = anime.get("id")
    anime_preprocessed["title"] = anime.get("title")

    anime_preprocessed["mean_score_mal"] = anime.get("mean")
    anime_preprocessed["popularity_mal"] = anime.get("num_list_users")
    anime_preprocessed["number_scorer_mal"] = anime.get("num_scoring_users")
    anime_preprocessed["favorites_mal"] = anime.get("num_favorites")

    anime_preprocessed["duration"] = int(round(int(anime.get("average_episode_duration") / 60)))
    anime_preprocessed["status"] = anime.get("status")
    anime_preprocessed["episodes"] = anime.get("num_episodes")
    anime_preprocessed["source"] = anime.get("source")
    anime_preprocessed["age"] = anime.get("rating")
    anime_preprocessed["media_type"] = anime.get("media_type")

    genres = anime.get("genres")
    if genres != None:
        anime_preprocessed["genres"] = [genre["name"] for genre in genres]
    else:
        anime_preprocessed["genres"] = None

    anime_preprocessed["start_date"] = anime.get("start_date")
    anime_preprocessed["end_date"] = anime.get("end_date")
    season = anime.get("start_season")
    if season != None:
        anime_preprocessed["season_season"] = season["season"]
        anime_preprocessed["season_year"] = season["year"]
    else:
        anime_preprocessed["season_season"] = None
        anime_preprocessed["season_year"] = None

    studios = anime.get("studios")
    if studios != None:
        anime_preprocessed["studios"] = [studio["name"] for studio in studios]
    else:
        anime_preprocessed["studios"] = None

    return anime_preprocessed


if __name__ == "__main__":
    with open("data/data.json", "r") as file:
        anime_list = json.load(file)
    new_anime_list = []
    for anime in anime_list:
        new_anime_list.append(preprocess_anime(anime))

    with open("data/data_preprocessed.json", "w") as write_file:
        json.dump(new_anime_list, write_file, indent=4)
