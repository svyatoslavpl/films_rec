from sklearn.metrics.pairwise import cosine_distances
from sentence_transformers import SentenceTransformer

def perform_movie_recommendation(phrase, time_available, study_english, movie_data, english_films_data, time_films_data):




    new_text_embedding = model.encode([phrase])
    corpus_embeddings = np.load("data/embeddings.npy")
    distances = cosine_distances(new_text_embedding, corpus_embeddings)
    top_indexes = np.argsort(distances.flatten())[:10]
    top_movies = movie_data.loc[top_indexes, 'movie_name'].values


    if study_english == 'Да':
        english_level = st.selectbox("Выберите уровень английского:", ('Начинающий', 'Средний', 'Продвинутый'))
        english_films_data = filter_films_by_english_level(english_films_data, english_level)
        time_films_data = filter_films_by_time(time_films_data, time_available)
        recommended_films = pd.merge(english_films_data, time_films_data, on='movie_id')['movie_name'].values
    else:
        recommended_films = top_movies

    return recommended_films
