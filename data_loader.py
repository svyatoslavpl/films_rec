import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def filter_films_by_time(films_data, max_time):
    return films_data[films_data['time'] <= max_time]

def filter_films_by_english_level(films_data, english_level):
    return films_data[films_data['english level'] == english_level]
