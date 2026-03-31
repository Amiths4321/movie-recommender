from fastapi import FastAPI
from src.load_data import load_data
from src.model import build_user_item_matrix, compute_user_similarity, compute_item_similarity
from src.recommend import recommend_movies, recommend_similar_movies

app = FastAPI()

# Load once
_data = load_data()
_uim = build_user_item_matrix(_data)
_user_sim = compute_user_similarity(_uim)
_item_sim = compute_item_similarity(_uim)

@app.get('/')
def home():
    return {'message': 'Movie Recommender API'}

@app.get('/recommend/user/{user_id}')
def recommend_user(user_id: int):
    recs = recommend_movies(user_id, _uim, _user_sim)
    return recs.to_dict()

@app.get('/recommend/movie')
def recommend_movie(title: str):
    recs = recommend_similar_movies(title, _item_sim)
    return recs.to_dict()
