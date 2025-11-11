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

def search_actor_name(actor_name):
    actor_name_query = urllib.parse.quote(actor_name)
    api_url = "https://api.themoviedb.org/3/search/person?query={}&include_adult=false&language=en-US&page=1".format(actor_name_query)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()


def get_actor_data(actor_id = None, actor_name = "Morgan Freeman"):
    if actor_id == None:
        json_search_resp = search_actor_name(actor_name)
        actor_id = json_search_resp["results"][0]["id"]
        print(actor_id)
    actor_url = "https://api.themoviedb.org/3/person/{}?language=en-US".format(actor_id)
    tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
    actor_data_resp = requests.get(actor_url, headers= tmdb_headers)
    print(actor_data_resp.text)
    return actor_data_resp.json()

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


print(get_actor_data(actor_id=None, actor_name="Chris Pratt"))