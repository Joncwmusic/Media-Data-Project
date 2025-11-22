import streamlit as st
import pandas as pd
import spotifyIngestion as si


### Looks like streamlit has iframe and html componenets
###



if __name__ == '__main__':
    st.title("Media Dashboard: Find data on your favorite artists, actors and movies!")

    tab1, tab2 = st.tabs(["Music", "Movies and TV"])
    ##### Things to put on the dashbaord
    # Search for artist function

    with tab1:
        st.header("Music")
        st.text("Artist: ")
        artist_search_string = st.text_input("Search for an artist!")

        # Graph stuff over time or one number stats
        # # Number of monthly listeners (over time)
        # # Number of followers (over time) resp_json["followers"]["total"]
        # # Direct artist comparison like google trends (up to 3 artists)
        # # Number of streams (across all tracks or per track)
        # # Number of songs

        # Analytics Visualizations
        # # Patterns of growth for big artists
        # #

        # Search for Track/Album function
        # # Skip Rate and Avg Listening Time
