import streamlit as st
import requests

st.title("Movie Recommender")

option = st.selectbox("Choose recommendation type", ["By User ID", "By Movie Title", "Trending"])

if option == "By User ID":
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    if st.button("Recommend"):
        res = requests.get(f"http://127.0.0.1:8000/recommend/user/{int(user_id)}")
        st.json(res.json())

elif option == "By Movie Title":
    title = st.text_input("Enter Movie Title")
    if st.button("Recommend"):
        res = requests.get(f"http://127.0.0.1:8000/recommend/movie", params={"title": title})
        st.json(res.json())

elif option == "Trending":
    if st.button("Show Trending"):
        res = requests.get("http://127.0.0.1:8000/trending")
        st.json(res.json())