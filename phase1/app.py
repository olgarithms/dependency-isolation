APIKEY = "*****"
API = "https://api.themoviedb.org/3/movie"
NOW_PLAYING_URL = f"{API}/now_playing?api_key={APIKEY}&language=en-US&page=1"

from pprint import pprint
import requests


def get_now_playing_movies():

    movies_dict = {}
    try:
        data = requests.get(NOW_PLAYING_URL).json()
    except requests.exceptions.RequestException as ex:
        print(f"Error: {ex}")
    for movie in data["results"]:
        movies_dict[movie["id"]] = {"title": movie["title"], "directors": []}
    return movies_dict


def grate_movies():

    movies_dict = get_now_playing_movies()
    return movies_dict


movies_dict = grate_movies()
pprint(movies_dict)
pprint(directors_dict)
