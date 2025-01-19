import typer
from utils.api import API
from models.movie import json_to_movie

api = API()

cli_tmdb = typer.Typer()

@cli_tmdb.command()
def movies(
    type: str = typer.Option(None, help="Type of movies to show. You can choose between 'popular', 'playing', 'top', 'upcoming'"),
    lan: str = typer.Option("en-US", help="Language for the movies, default is 'en-US'"),
    page: int = typer.Option(1, help="Page number for the movies, default is 1")
    ):

    if type == "popular":
        movies = json_to_movie(api.get_popular_movies(page, lan))

    if type == "playing":
        movies = json_to_movie(api.get_now_playing_movies(page, lan))
    
    if type == "top":
        movies = json_to_movie(api.get_top_rated_movies(page, lan))

    if type == "upcoming":
        movies = json_to_movie(api.get_upcoming_movies(page, lan))

    if not type:
        movies = json_to_movie(api.get_movies(page, lan))    

    for movie in movies:
        print(f"-> {movie}")
