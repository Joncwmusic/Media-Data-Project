import requests
import base64
import dotenv
import os
import urllib.parse


dotenv.load_dotenv()

lastfm_api_key = os.getenv("LASTFM_API_KEY")

def get_artist_info(artist_name, api_key):
    response = requests.get(
        "http://ws.audioscrobbler.com/2.0/",
        params={
            "method": "artist.getinfo",
            "artist": artist_name,
            "api_key": api_key,
            "format": "json"
        }
    )
    print(response.json())
    return response.json()

get_artist_info("Origami Angel", lastfm_api_key)