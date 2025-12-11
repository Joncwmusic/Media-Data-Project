import streamlit as st
from ingestion.IsThisBandEmo import check_is_emo
from ingestion import geniusIngestion as geniusIn
from ingestion import spotifyIngestion as spotifyIn
from ingestion import tmdbIngestion as tmdbIn
from buildapp import buildMusicArtistData as bmusic
from buildapp import buildMovieActorData as bmovie


if __name__ == '__main__':
    st.title("Media Dashboard: Find data on your favorite artists, actors and movies!")
    tab1, tab2 = st.tabs(["Music", "Movies and TV"])

    # ARTIST SEARCH
    with tab1:
        bmusic.build_music_tab()

    with tab2:
        bmovie.build_movie_tab()

