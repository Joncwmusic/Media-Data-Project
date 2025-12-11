import streamlit as st
from ingestion import tmdbIngestion as tmdbIn


def build_movie_tab():
    st.header("Movies and TV")
    st.text("Actor:")
    actor_search_string = st.text_input("Search for an Actor")
    # Do tmdb

    if actor_search_string:
        actor_json = tmdbIn.search_actor_name(actor_search_string)

        actor_dict = {}

    # for item in actor_json["artists"]["items"]:
    #     try:
    #         artist_id = item["id"]
    #         total_followers = item["followers"]["total"]
    #         genre_list = item["genres"]
    #         try:
    #             artist_image_url = item["images"][0]["url"]
    #             artist_thumbnail_url = item["images"][1]["url"]
    #         except:
    #             artist_image_url = None
    #             artist_thumbnail_url = None
    #         artist_name = item["name"]
    #         artist_popularity_score = item["popularity"]
    #         artist_list = [artist_id, total_followers, genre_list, artist_name, artist_image_url,
    #                        artist_thumbnail_url, artist_popularity_score]
    #         actor_dict[artist_name] = artist_list
    #     except:
    #         st.text("Error Collecting Artist Data")
    #         st.text(item["name"])
    #         st.json(item)

        st.header("Actor Search Results")

    header_c = st.container()
    col1, col2, col3, col4, col5, col6 = header_c.columns(6)
    col1.markdown("**Actor**")
    col2.markdown("**Profile Photo**")
    # col3.markdown("**Followers**")
    # col4.markdown("**Popularity Score**")
    # col5.markdown("**Genres**")


    st.header("Movies and TV")
    st.text("Movie or TV Series:")
    actor_search_string = st.text_input("Search for an Actor")


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