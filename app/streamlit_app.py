import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.load_data import load_data
from src.model import build_user_item_matrix, compute_user_similarity, compute_item_similarity
from src.recommend import recommend_movies, recommend_similar_movies

st.set_page_config(page_title='Movie Recommender', layout='wide')


# 🔐 Simple Login Simulation
# -----------------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title('🔐 Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username == 'admin' and password == 'admin':
            st.session_state.logged_in = True
            st.success('Login successful')
        else:
            st.error('Invalid credentials')
    st.stop()

# -----------------------------
# 📊 Load Data (Cached)
# -----------------------------
@st.cache_data
def load_all():
    data = load_data()
    uim = build_user_item_matrix(data)
    user_sim = compute_user_similarity(uim)
    item_sim = compute_item_similarity(uim)
    return data, uim, user_sim, item_sim


data, uim, user_sim, item_sim = load_all()

st.title('🎬 Movie Recommender System')

# -----------------------------
# 🔥 Top Trending Movies
# -----------------------------
st.subheader('🔥 Top Trending Movies')
trending = data.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
st.write(trending)

st.divider()

# -----------------------------
# 🎯 Mode Selection
# -----------------------------
mode = st.radio('Choose Mode', ['User-Based', 'Movie-Based'])

# -----------------------------
# 👤 User-Based
# -----------------------------
if mode == 'User-Based':
    user_id = st.number_input('Enter User ID', min_value=1, step=1)

    if st.button('Recommend for User'):
        recs = recommend_movies(user_id, uim, user_sim)
        st.write(recs)

# -----------------------------
# 🎬 Movie-Based (Dropdown Search)
# -----------------------------
else:
    movie_list = uim.columns.tolist()
    selected_movie = st.selectbox('Select Movie', movie_list)

    if st.button('Find Similar Movies'):
        recs = recommend_similar_movies(selected_movie, item_sim)
        st.write(recs)
