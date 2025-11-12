import requests
import base64
import dotenv
import os
import urllib.parse

dotenv.load_dotenv()

genius_id = os.getenv("GENIUS_CLIENTID")
genius_secret = os.getenv("GENIUS_CLIENTSECRET")

# Note: https://github.com/celiao/tmdbsimple/ is an option

def get_genius_lyrics(song_id):
    return None

def get_artist_id_from_search(artist_name):
    return None

def get_song_id(song_name):
    return None

def get_song_analysis(song_id):
    return None


