import streamlit as st
import pandas as pd

# Load the movie data from CSV or JSON file
def load_movie_data(file_path):
    return pd.read_csv(file_path)  # If using CSV, use pd.read_json(file_path) for JSON
    
def main():
    
    st.write("Let me suggest you some movies!")

    def show_df():
        print(st.session_state['genres'])
        if st.session_state['genres'] == []:
            st.write("Please select a genre")
        else:
            df = movie_data.loc[(movie_data['genres'].isin(st.session_state['genres']))].sample(n=5, replace=True)
            df = df[df.columns[[1,4,5,6]]].drop_duplicates()
            st.dataframe(df, hide_index=True, column_config={"title": "Movie", "genres": "Genre", "year_of_release": st.column_config.NumberColumn(label="Year", format="%d")}, use_container_width=True)
    
    
    file_path = 'archive/1950-1989/bollywood_meta_1950-1989.csv'
    
    # Load the movie data
    movie_data = load_movie_data(file_path)
    
    all_genres = tuple(set(movie_data['genres'].to_list()))
    genres = st.multiselect("Genres", all_genres, default=all_genres[0], key="genres")
    if st.button("Suggest Movies ↻"):
        show_df()


if __name__ == "__main__":
    main()