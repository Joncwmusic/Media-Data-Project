import streamlit as st
from ingestion.IsThisBandEmo import check_is_emo
from ingestion import geniusIngestion as geniusIn
from ingestion import spotifyIngestion as spotifyIn


def build_music_tab():
    st.header("Music")
    st.text("Artist: ")
    artist_search_string = st.text_input("Search for an artist!")

    # RETRIEVE SPOTIFY ARTIST DATA FROM SEARCH
    if artist_search_string:
        spotify_token = spotifyIn.get_spotify_token()
        artist_json = spotifyIn.search_for_artist(artist_search_string, token=spotify_token)

        artist_dict = {}

        # Artist metrics from spotify API
        for item in artist_json["artists"]["items"]:
            try:
                artist_id = item["id"]
                total_followers = item["followers"]["total"]
                genre_list = item["genres"]
                try:
                    artist_image_url = item["images"][0]["url"]
                except:
                    artist_image_url = None
                try:
                    artist_thumbnail_url = item["images"][1]["url"]
                except:
                    artist_thumbnail_url = None
                artist_name = item["name"]
                artist_popularity_score = item["popularity"]
                artist_list = [artist_id, total_followers, genre_list, artist_name, artist_image_url,
                               artist_thumbnail_url, artist_popularity_score]
                artist_dict[artist_name] = artist_list
            except:
                st.text("Error Collecting Artist Data")
                st.text(item["name"])
                st.json(item)

        # st.dataframe(artist_dict)

        st.header("Artist Search Results")

        header_c = st.container()
        col1, col2, col3, col4, col5, col6 = header_c.columns(6)
        col1.markdown("**Artist**")
        col2.markdown("**Profile Photo**")
        col3.markdown("**Followers**")
        col4.markdown("**Popularity Score**")
        col5.markdown("**Genres**")

        for item in artist_dict:

            arc = st.container()
            col1, col2, col3, col4, col5, col6 = arc.columns(6)

            col1.text(artist_dict[item][3])
            try:
                col2.image(artist_dict[item][4])
            except:
                col2.write("no image available")

            col3.text(artist_dict[item][1])

            col4.text(artist_dict[item][6])

            for genre in artist_dict[item][2]:
                col5.write(genre)

            # col6.button(label= "More data", key = artist_dict[item][0] + "morebutton")
            if col6.button(label="More Data", key=artist_dict[item][0] + "morebutton"):
                col6.write("The data you're looking for is in another castle!")
                col6.write(check_is_emo(artist_dict[item][3]))

    # SONG SEARCH
    st.text("Song: ")
    song_search_string = st.text_input("Search for a song")
    song_spotify_json = spotifyIn.search_for_song(song_search_string)
    song_genius_json = geniusIn.get_genius_lyrics(song_search_string)


# TESTING
