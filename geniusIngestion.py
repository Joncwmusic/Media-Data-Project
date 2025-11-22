import requests
import base64
import dotenv
import os
import urllib.parse

dotenv.load_dotenv()

genius_id = os.getenv("GENIUS_CLIENTID")
genius_secret = os.getenv("GENIUS_CLIENTSECRET")
genius_access_token = os.getenv("GENIUS_ACCESS_TOKEN")

# Note: https://github.com/celiao/tmdbsimple/ is an option



def get_genius_lyrics(song_id = None, song_name = ""):
    if song_id==None:
        song_id = get_song_id(song_name)
    song_url = "https://api.genius.com/songs/{}".format(song_id)
    genius_header = {'Authorization': 'Bearer ' + genius_access_token}
    resp = requests.get(song_url, headers=genius_header)
    print(resp.text)
    return resp.json()

def get_artist_id_from_search(artist_name):
    return None

def get_song_id(song_name):
    """
    :param song_name: string for the song name
    :return: genius song_id
    """
    song_name_query = urllib.parse.quote(song_name)
    genius_url = "https://api.genius.com/search?q={}".format(song_name_query)
    genius_header = {'Authorization': 'Bearer ' + genius_access_token}
    resp = requests.get(url=genius_url, headers=genius_header).json()
    song_id = resp["response"]["hits"][0]["result"]["id"]
    return song_id

def get_song_analysis(song_id):
    return None


print(get_genius_lyrics(song_name="They Not Like Us Kendrick"))