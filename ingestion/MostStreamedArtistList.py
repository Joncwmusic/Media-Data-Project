from bs4 import BeautifulSoup
import requests
import pandas as pd
from ingestion import spotifyIngestion
import datetime as dt

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
    artist_id_mult_string = ",".join(artist_id_list)
    artist_response = requests.get('https://api.spotify.com/v1/artists/?ids={}'.format(artist_id_mult_string),
                                   headers=artist_headers)
    ## extract json components in a dict
    artist_json = artist_response.json()
    print(artist_json)
    artist_dict = {"id":[], "Name":[], "Followers":[], "Popularity":[], "Genres":[], "Image_url":[], "Timestamp":[]}

    for artist in artist_json["artists"]:
        print(artist)
        artist_dict["id"].append(artist["id"])
        artist_dict["Followers"].append(artist["followers"]["total"])
        artist_dict["Genres"].append(artist["genres"])
        try:
            artist_dict["Image_url"].append(artist["images"][0]["url"])
        except:
            artist_dict["Image_url"].append(None)
        artist_dict["Name"].append(artist["name"])
        artist_dict["Popularity"].append(artist["popularity"])
        artist_dict["Timestamp"].append(dt.datetime.now())

        print(artist_dict)

    return pd.DataFrame(artist_dict)
        #compile data into dictionary to convert to pandas df

# Use that to call the endpoint (use multiple artist api call)


# compile the data as follows:
# artist_id, artist_name, followers, listeners, album array, genre array, popularity score
# , image url, first_tracked and last_updated, is_active



######## Testing
skrillex_id = get_artist_id("skrillex")
origami_angel_id = get_artist_id("Origami Angel")
print([skrillex_id, origami_angel_id])
print(create_pandas_record_mult([skrillex_id, origami_angel_id]))