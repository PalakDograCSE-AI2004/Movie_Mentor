import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=875189cb293cd34422166bc34bdff4fe&language=en-US'.format(movie_id))

    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # index fetch kia
    distances = similarity[movie_index]  # similarity matrix mai uss indx par gye
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
                  1:6]  # sort kia and fetched top 5

    recommended_movies=[]
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')
selected_movie_name= st.selectbox('Select movie',movies['title'].values)


# Custom CSS to set the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if st.button('Recommend'):
    names,posters =recommend(selected_movie_name)

    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
