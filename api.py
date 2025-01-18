import requests
from decouple import config


class MissingAPIKeyError(Exception):
    """Raised when the API key is missing."""
    pass

API_KEY = config('TMDB_API_KEY', default=None)
if not API_KEY:
    raise MissingAPIKeyError(
        "Not found API key, please set the TMDB_API_KEY environment variable."
    )

class API():
    def __init__(self):
        self.url = "https://api.themoviedb.org/3"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }


    def get_movies(self, page, lan) -> dict:
        url = f"{self.url}/trending/movie/day?language={lan}&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_popular_movies(self, page, lan) -> dict:
        url = f"{self.url}/movie/popular?language={lan}&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_now_playing_movies(self, page, lan) -> dict:
        url = f"{self.url}/movie/now_playing?language={lan}&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_top_rated_movies(self, page, lan) -> dict:
        url = f"{self.url}/movie/top_rated?language={lan}&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_upcoming_movies(self, page, lan) -> dict:
        url = f"{self.url}/movie/upcoming?language={lan}&page={page}"
        response = requests.get(url, headers=self.headers)
        return response.json()

