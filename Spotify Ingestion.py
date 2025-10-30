import requests
import base64
import dotenv
import os

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
### get audio metadata based on song search


print(get_artist_data_raw('0TnOYISbd1XYRBk9myaseg'))

