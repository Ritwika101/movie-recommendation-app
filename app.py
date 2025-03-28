import streamlit as st 
import pickle
import time
import requests
import ssl
import certifi

AUTHOR_DETAILS = """
Hi! I am Ritwika. I like to spend time exploring ML models. This is my LinkedIn
"""

ssl_context = ssl.create_default_context(cafile=certifi.where())

movies_data = pickle.load(open('movies_data.pkl', 'rb'))
movies_list = movies_data['title'].values

recommendations_list = pickle.load(open('recommendations.pkl', 'rb'))

def fetch_poster(tmdbId, apiKey):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(tmdbId, apiKey), verify=certifi.where())
    json_data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + json_data['poster_path']

def recommend(title, apiKey):
    movie_index = movies_data[movies_data['title'] == title].index[0]
    list_of_recommendations = recommendations_list[movie_index]
    titles = []
    posters = []
    for index in list_of_recommendations[1:6]:
        titles.append(movies_data.iloc[index]['title'])
        posters.append(fetch_poster(movies_data.iloc[index]['tmdbId'], apiKey))
    return titles, posters

def stream_data():
    for word in AUTHOR_DETAILS.split(" "):
        yield word + " "
        time.sleep(0.05)
    st.link_button("Linkedin", "https://www.linkedin.com/in/ritwika-pal-198b48199/")
    

st.title('Movie Recommendation Application')

apiKey = st.text_input("TMDB api key", "")

chosen_movie = st.selectbox('Choose a movie', movies_list)

if st.button("Recommend"):
    titles, posters = recommend(chosen_movie, apiKey)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(titles[0])
        st.image(posters[0])
    with col2:
        st.text(titles[1])
        st.image(posters[1])
    with col3:
        st.text(titles[2])
        st.image(posters[2])
    with col4:
        st.text(titles[3])
        st.image(posters[3])
    with col5:
        st.text(titles[4])
        st.image(posters[4])


if st.button("About Developer"):
    st.write_stream(stream_data)
