from app import grate_movies
from unittest import mock
import pytest

APIKEY = "*****"
API = "https://api.themoviedb.org/3/movie"
NOW_PLAYING_URL = f"{API}/now_playing?api_key={APIKEY}&language=en-US&page=1"

TMDB_GET_NOW_PLAYING_RESPONSE = {
    "results": [
        {
            "id": 443791,
            "popularity": 232.985,
            "release_date": "2020-01-08",
            "title": "Underwater",
        },
        {
            "id": 454626,
            "popularity": 207.585,
            "release_date": "2020-02-12",
            "title": "Sonic the Hedgehog",
        },
    ]
}


def test_give_get_now_playing():
    with mock.patch("app.requests") as mock_requests:
        mock_requests.get.return_value.json.return_value = TMDB_GET_NOW_PLAYING_RESPONSE
        assert grate_movies() == {
            443791: {"directors": [], "title": "Underwater"},
            454626: {"directors": [], "title": "Sonic the Hedgehog"},
        }
        assert mock_requests.get.call_args == mock.call(NOW_PLAYING_URL)
