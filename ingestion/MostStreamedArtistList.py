from bs4 import BeautifulSoup
import requests
from ingestion import spotifyIngestion

top_artist_url = "https://kworb.net/spotify/artists.html"


def get_artist_id(artist_name):
    artist_json = spotifyIngestion.search_for_artist(artist_name)
    return artist_json["artists"]["items"][0]["id"]
# for each artist call the spotify search endpoint
# get the top result for an ID

def create_pandas_record(artist_id):
    token = spotifyIngestion.get_spotify_token()
    artist_headers = {'Authorization': 'Bearer ' + token}
    artist_response = requests.get('https://api.spotify.com/v1/artists/{}'.format(artist_id),
                                   headers=artist_headers)
    artist_json_resp = artist_response.json()
    ## extract json components in a dict
    return artist_response.json()

def create_pandas_record_mult(artist_id_list):
    token = spotifyIngestion.get_spotify_token()
    artist_headers = {'Authorization': 'Bearer ' + token}
    artist_id_mult_string = artist_id_list.join("&")
    artist_response = requests.get('https://api.spotify.com/v1/artists/{}'.format(artist_id_mult_string),
                                   headers=artist_headers)
    ## extract json components in a dict
    artist_json_resp = artist_response.json()
# Use that to call the endpoint (use multiple artist api call)


# compile the data as follows:
# artist_id, artist_name, followers, listeners, album array, genre array, popularity score
# , image url, first_tracked and last_updated, is_active