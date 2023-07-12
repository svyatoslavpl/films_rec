import streamlit as st
from data_loader import load_data, filter_films_by_time, filter_films_by_english_level
from recommendation import perform_movie_recommendation
from display import display_recommendations

def main():
    st.title("Фильмы по вашему настроению")


    movie_data = load_data('data/movie_names.csv')
    english_films_data = load_data('data/english_films.csv')
    time_films_data = load_data('data/films_time.csv')

    with st.container():
        phrase = st.text_input("Введите фразу по вашему настроению:")
        time_available = st.number_input("Введите количество свободного времени (в минутах):")
        study_english = st.radio("Хотите ли вы изучать английский сегодня?", ('Да', 'Нет'))

    with st.container():

        recommended_films = perform_movie_recommendation(phrase, time_available, study_english, movie_data, english_films_data, time_films_data)

    with st.container():

        display_recommendations(recommended_films)

if __name__ == '__main__':
    main()
