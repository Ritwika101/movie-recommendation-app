import streamlit as st 
import requests
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())

st.image('https://image.tmdb.org/t/p/original/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg')

response = requests.get('https://api.themoviedb.org/3/movie/11?api_key=d8a4f8c33f590d8cb1dad133e6566b7c', verify=False)
st.write(response.json())