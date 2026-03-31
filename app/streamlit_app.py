import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.load_data import load_data
from src.model import build_user_item_matrix, compute_user_similarity, compute_item_similarity
from src.recommend import recommend_movies, recommend_similar_movies

st.title('🎬 Movie Recommender System')

@st.cache_data
def load_all():
    data = load_data()
    uim = build_user_item_matrix(data)
    user_sim = compute_user_similarity(uim)
    item_sim = compute_item_similarity(uim)
    return uim, user_sim, item_sim

uim, user_sim, item_sim = load_all()

mode = st.selectbox('Choose Mode', ['User-Based', 'Movie-Based'])

if mode == 'User-Based':
    user_id = st.number_input('Enter User ID', min_value=1, step=1)
    if st.button('Recommend'):
        recs = recommend_movies(user_id, uim, user_sim)
        st.write(recs)

else:
    movie = st.text_input('Enter Movie Name', 'Toy Story (1995)')
    if st.button('Find Similar'):
        recs = recommend_similar_movies(movie, item_sim)
        st.write(recs)