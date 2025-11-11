import requests
import base64
import dotenv
import os
import urllib.parse

dotenv.load_dotenv()

tmdb_token = os.getenv("TMDB_TOKEN")
tmdb_key = os.getenv("TMDB_API_KEY")

# Note: https://github.com/celiao/tmdbsimple/ is an option

# def get_request_token(tmdb_token):
#     token_url = "https://www.themoviedb.org/3/movie/11"
#     tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
#     resp = requests.get(token_url, headers=tmdb_headers)
#     return resp.text

def get_actor_data(actor_name):
    actor_url = "https://api.themoviedb.org/3/person/person_id?language=en-US"
    tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
    return None

def get_movie_data(movie_name):
    return None

def get_most_popular_movies():
    return None

def get_most_popular_tv_shows():
    return None

def get_most_popular_movie_people():
    return None

def get_most_popular(type = "movie"):
    '''
    :param type: string with options "movie, people, and tv"
    :return: most popular items of that type from TMDB API
    '''
    if type == "movie":
        get_most_popular_movies()
    if type == "people":
        get_most_popular_movie_people()
    if type == "tv":
        get_most_popular_tv_shows()


print(get_request_token(tmdb_token))