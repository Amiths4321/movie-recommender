import pandas as pd


def recommend_movies(user_id, user_item_matrix, user_similarity_df, top_n=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    weighted = pd.Series(dtype=float)

    for other_user, score in similar_users.items():
        ratings = user_item_matrix.loc[other_user]
        weighted = weighted.add(ratings * score, fill_value=0)

    watched = user_item_matrix.loc[user_id].dropna().index
    recs = weighted.drop(watched)
    return recs.sort_values(ascending=False).head(top_n)


def recommend_similar_movies(movie_title, item_similarity_df, top_n=5):
    return item_similarity_df[movie_title].sort_values(ascending=False)[1:].head(top_n)