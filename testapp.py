import streamlit as st
import pickle 
import pandas as pd
import requests



# Function to get movie recommendations
def recommendations(movie_title):
    movie_index = df[df['title'] == movie_title].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    # movie_posters = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)
        # movie_posters.append(fetch_poster(movie_id))
    return recommended_movies

# Load data and models
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
df = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")
option = st.selectbox("Select a movie:", df['title'].values)

# Initialize variables
names = []
# posters = []

if st.button('Recommend'):
    names = recommendations(option)
    if names:
        st.write("### Recommended Movies:")
        for i, movie_name in enumerate(names, start=1):
            st.write(f"{i}. {movie_name}")
else:
    st.write('sorry the no idea about this movie!!!!!')

