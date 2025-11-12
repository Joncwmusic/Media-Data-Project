import requests
import base64
import dotenv
import os
import urllib.parse

dotenv.load_dotenv()

spotify_client_id = os.getenv("SPOTIFY_CLIENTID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENTSECRET")

def get_spotify_token():
    # Encode client_id and client_secret for Authorization header
    auth_string = f"{spotify_client_id}:{spotify_client_secret}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(token_url, headers=headers, data=data)
    token = response.json().get("access_token")
    print("Access token:", token)
    return token

def get_top_artist_data_curated():
    return None

### get top tracks from the big playlist
def get_top_song_data_curated():
    return None

### get artist specific metrics based on artist search
def get_artist_data_raw(artist_string, token = None):
    current_token = token
    if artist_string is None:
        raise ValueError("artist_string is null. Please input artist string")
    if current_token is None:
        token = get_spotify_token()
    artist_headers = {'Authorization': 'Bearer ' + token}
    artist_response = requests.get('https://api.spotify.com/v1/artists/{}'.format(artist_string), headers= artist_headers)
    return artist_response.json()


### get song specific metrics based on song search

def get_song_data_raw(track_string, token = None):
    current_token = token
    if track_string is None:
        raise ValueError("artist_string is null. Please input artist string")
    if current_token is None:
        token = get_spotify_token()
    track_headers = {'Authorization': 'Bearer ' + token}
    track_response = requests.get('https://api.spotify.com/v1/tracks/{}'.format(track_string), headers= track_headers)
    return track_response.json()


def get_audio_data_raw(track_string, token = None):
    current_token = token
    if track_string is None:
        raise ValueError("artist_string is null. Please input artist string")
    if current_token is None:
        token = get_spotify_token()
    track_headers = {'Authorization': 'Bearer ' + token}
    track_response = requests.get('https://api.spotify.com/v1/audio-analysis/{}'.format(track_string), headers= track_headers)
    return track_response.json()


def search_for_artist(artist_search_string, token = None):
    current_token = token
    if artist_search_string is None:
        raise ValueError("artist_search_string is null. Please input artist string")
    if current_token is None:
        token = get_spotify_token()
    query_string = urllib.parse.quote(artist_search_string)
    print(query_string)
    type = "artist"
    limit = "20"
    artist_headers = {'Authorization': 'Bearer ' + token}
    result = requests.get('https://api.spotify.com/v1/search?q={}&type={}&market=US&limit={}'.format(query_string, type, limit), headers= artist_headers)
    return result.json()

def search_for_song(song_search_string, token = None):
    current_token = token
    if song_search_string is None:
        raise ValueError("artist_search_string is null. Please input artist string")
    if current_token is None:
        token = get_spotify_token()
    query_string = urllib.parse.quote(song_search_string)
    print(query_string)
    type = "track"
    limit = "20"
    artist_headers = {'Authorization': 'Bearer ' + token}
    result = requests.get(
        'https://api.spotify.com/v1/search?q={}&type={}&market=US&limit={}'.format(query_string, type, limit),
        headers=artist_headers)
    return result.json()

#print(get_artist_data_raw('0TnOYISbd1XYRBk9myaseg', token = "BQBeZg-yY3ofEQFl8BHhE_FD3CrOfqFtQ7RnXEAflje7U_njiul1c6tFUyo3_b5Wezwbcb288nEilVEIW2PFzQ-9BSy0hVpZwgCdSpLbc74MoABNdWq8Kcu82N1otQ86J87SbWCC6Jo"))
#print(get_song_data_raw('11dFghVXANMlKmJXsNCbNl', token = "BQBeZg-yY3ofEQFl8BHhE_FD3CrOfqFtQ7RnXEAflje7U_njiul1c6tFUyo3_b5Wezwbcb288nEilVEIW2PFzQ-9BSy0hVpZwgCdSpLbc74MoABNdWq8Kcu82N1otQ86J87SbWCC6Jo"))
token = get_spotify_token()
print(search_for_song("Sequoia Throne", token = token))