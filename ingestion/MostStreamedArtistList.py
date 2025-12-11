from bs4 import BeautifulSoup
import requests

top_artist_url = "https://kworb.net/spotify/artists.html"

# for each artist call the spotify search endpoint
# get the top result for an ID
# Use that to call the endpoint (use multiple artist api call)
# compile the data as follows:
# artist_id, artist_name, followers, listeners, album array, genre array, popularity score
# , image url, first_tracked and last_updated, is_active