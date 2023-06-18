import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_distances

# Загрузка данных
data = pd.read_csv('movie_names.csv')
data_flm = pd.read_csv('flm_final.csv')

# Загрузка предобученной модели
model_path = "text_model"
model = SentenceTransformer(model_path)

# Загрузка предвычисленных эмбеддингов
corpus_embeddings = np.load("embeddings.npy")

# Streamlit приложение
st.title("Рекомендация фильмов")

# Поля ввода
new_text = st.text_input("Введите текст", "")
number = st.number_input("Введите число", value=20)

if st.button("Рекомендовать"):
    # Кодирование нового текста
    new_text_embedding = model.encode([new_text])

    # Вычисление косинусных расстояний
    distances = cosine_distances(new_text_embedding, corpus_embeddings)
    top_indexes = np.argsort(distances.flatten())[:5]

    # Вывод рекомендаций фильмов
    st.header("Рекомендации фильмов:")
    for i in top_indexes:
        st.write(data['movie_name'][i] + " [По настроению]")

    # Вычисление ближайших фильмов по числу
    top_5_closest = data_flm.assign(diff=abs(data_flm['time'] - number)).sort_values('diff').head(5)['name']

    # Вывод ближайших фильмов по числу
    st.header("Ближайшие фильмы по числу:")
    st.write(top_5_closest)
