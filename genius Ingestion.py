import requests
import base64
import dotenv
import os
import urllib.parse

dotenv.load_dotenv()

genius_id = os.getenv("GENIUS_CLIENTID")
genius_secret = os.getenv("GENIUS_CLIENTSECRET")

# Note: https://github.com/celiao/tmdbsimple/ is an option

# def get_request_token(tmdb_token):
#     token_url = "https://www.themoviedb.org/3/movie/11"
#     tmdb_headers = {'Authorization': 'Bearer ' + tmdb_token}
#     resp = requests.get(token_url, headers=tmdb_headers)
#     return resp.text

def get_genius_lyrics(song_id):
    return None


def get_song_analysis(song_id)
    return None


