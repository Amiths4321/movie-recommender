from src.load_data import load_data
from src.model import build_user_item_matrix, compute_user_similarity, compute_item_similarity
from src.recommend import recommend_movies, recommend_similar_movies


def main():
    data = load_data()
    uim = build_user_item_matrix(data)
    user_sim = compute_user_similarity(uim)
    item_sim = compute_item_similarity(uim)

    print(recommend_movies(1, uim, user_sim))
    print(recommend_similar_movies('Toy Story (1995)', item_sim))


if __name__ == '__main__':
    main()