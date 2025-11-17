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
    '''
    :param actor_name: actor name to query in api search
    :return: json response with search results
    '''
    actor_name_query = urllib.parse.quote(actor_name)
    api_url = "https://api.themoviedb.org/3/search/person?query={}&include_adult=false&language=en-US&page=1".format(actor_name_query)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()


def get_actor_data(actor_id = None, actor_name = "Morgan Freeman"):
    '''
    :param actor_id: actor_id from tmdb supplied or otherwise searched for with actor_name query
    :param actor_name: actor_name to invoke search_actor_name function if actor_id is not provided
    :return: json response of actor data
    '''
    if actor_id == None:
        json_search_resp = search_actor_name(actor_name)
        actor_id = json_search_resp["results"][0]["id"]
        print(actor_id)
    actor_url = "https://api.themoviedb.org/3/person/{}?language=en-US".format(actor_id)
    tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
    actor_data_resp = requests.get(actor_url, headers= tmdb_headers)
    print(actor_data_resp.text)
    return actor_data_resp.json()


def search_movie_name(movie_name):
    '''
    :param movie_name: movie name query string
    :return: json results from movie search
    '''
    movie_name_query = urllib.parse.quote(movie_name)
    api_url = "https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&language=en-US&page=1".format(movie_name_query)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()


def get_movie_data(movie_id = None, movie_name = "The Shawshank redemption"):
    if movie_id == None:
        json_search_resp = search_actor_name(movie_name)
        print(json_search_resp.text)
        #movie_id = json_search_resp["results"][0]["id"]
    actor_url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
    actor_data_resp = requests.get(actor_url, headers= tmdb_headers)
    return actor_data_resp.json()

def get_trending_movies(week = True):
    if week:
        time_window = "week"
    else:
        time_window = "day"
    api_url = "https://api.themoviedb.org/3/trending/movie/{}}?language=en-US".format(time_window)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()


def get_trending_tv_shows(week=True):
    if week:
        time_window = "week"
    else:
        time_window = "day"
    api_url = "https://api.themoviedb.org/3/trending/movie/{}}?language=en-US".format(time_window)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()


def get_trending_movie_people(week=True):
    if week:
        time_window = "week"
    else:
        time_window = "day"
    api_url = "https://api.themoviedb.org/3/trending/movie/{}}?language=en-US".format(time_window)
    tmdb_header = {'Authorization': 'Bearer ' + tmdb_token}
    resp = requests.get(api_url, headers=tmdb_header)
    return resp.json()

def get_most_popular(type = "movie"):
    '''
    :param type: string with options "movie, people, and tv"
    :return: most popular items of that type from TMDB API
    '''
    if type == "movie":
        get_trending_movies()
    if type == "people":
        get_trending_movie_people()
    if type == "tv":
        get_trending_tv_shows()