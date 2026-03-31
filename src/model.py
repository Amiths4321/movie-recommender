import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def build_user_item_matrix(data):
    return data.pivot_table(index='userId', columns='title', values='rating')


def compute_user_similarity(matrix):
    filled = matrix.fillna(0)
    sim = cosine_similarity(filled)
    return pd.DataFrame(sim, index=matrix.index, columns=matrix.index)


def compute_item_similarity(matrix):
    filled = matrix.fillna(0)
    sim = cosine_similarity(filled.T)
    return pd.DataFrame(sim, index=matrix.columns, columns=matrix.columns)