# Streamlit App: Movie Recommendation System
# Author: Manas Mondal

import streamlit as st
import pandas as pd
import joblib

# Prepare feature data (must match training process)
ratings = ratings.rename(columns={'rating': 'actual_rating'})
data = pd.merge(ratings, beliefs[['userId', 'movieId', 'userPredictRating', 'userCertainty']], on=['userId', 'movieId'], how='left')
data = pd.merge(data, movies[['movieId', 'title', 'genres']], on='movieId', how='left')

data['userPredictRating'].fillna(data['actual_rating'].mean(), inplace=True)
data['userCertainty'].fillna(data['userCertainty'].mean(), inplace=True)
data['genre_count'] = data['genres'].apply(lambda x: len(str(x).split('|')) if pd.notnull(x) else 0)

X = data[['userId', 'movieId', 'userPredictRating', 'userCertainty', 'genre_count']]

# Streamlit App Layout
st.title("🎬 Personalized Movie Recommendation System")

st.markdown("""
This app provides personalized movie recommendations based on user behavior and belief elicitation insights. 
Select your **User ID** to view your top recommended movies!
""")

# User ID selection
unique_users = X['userId'].unique()
user_id = st.selectbox("Select User ID", unique_users)

# Number of recommendations
top_n = st.slider("Number of Recommendations", 1, 20, 5)

# Recommendation function
def recommend(user_id, top_n=5):
    user_movies = X[X['userId'] == user_id]
    user_preds = model.predict(user_movies.values)
    user_movies = user_movies.copy()
    user_movies['predicted_rating'] = user_preds
    top_recommendations = user_movies.sort_values('predicted_rating', ascending=False).head(top_n)
    top_recommendations = pd.merge(top_recommendations, movies[['movieId', 'title']], on='movieId', how='left')
    return top_recommendations[['title', 'predicted_rating']]

# Recommend button
if st.button("Get Recommendations"):
    recommendations = recommend(user_id, top_n)
    st.subheader(f"Top {top_n} Recommended Movies for User {user_id}")
    st.table(recommendations)

# Footer
st.markdown("""
---
Created by **Manas Mondal**  
Powered by XGBoost + Streamlit 🚀
""")
