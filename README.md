🎬 Personalized Movie Recommendation System
Created by Manas Mondal

This project builds a Personalized Movie Recommendation System by combining user behavior, belief elicitation data, and machine learning techniques.
It predicts movie ratings for users and recommends the best movies tailored to their preferences, all deployed through an interactive Streamlit web application.

🚀 Overview
This system predicts how users might rate movies by training an XGBoost regression model on a rich dataset of:

User ratings

User belief predictions

Genre-based features

The model's predictions are then served via a Streamlit app where users can select their User ID and get instant top movie recommendations!

🛠 Features
📈 Data Preprocessing: Merge ratings, beliefs, and genre data for feature engineering.

🤖 Machine Learning: XGBoost-based regression model to predict user ratings.

📊 Model Evaluation: RMSE and MAE used to evaluate model performance.

🎨 Streamlit App: Interactive UI where users select their User ID and get personalized movie recommendations.

💾 Model Persistence: Save and load trained models using joblib.

🧠 Belief Elicitation Integration: Uses both actual and predicted ratings to improve recommendations.


📊 Technologies Used
Python (pandas, numpy, sklearn, xgboost, joblib)

Streamlit (for web app UI)

Machine Learning (regression modeling)

Data Preprocessing (feature engineering from multiple datasets)

Model Deployment (joblib for model saving and loading)



📈 Model Performance
Root Mean Squared Error (RMSE): 1.4157

Mean Absolute Error (MAE): 1.0598

The model shows robust performance for personalized rating prediction.

🛤 Future Improvements
Integrate a hybrid recommendation engine (combining collaborative + content-based filtering).

Allow users to rate movies dynamically through the app.

Deploy the app using cloud platforms like AWS/GCP.

Add advanced deep learning-based recommendation algorithms.

📬 Contact
Feel free to connect with me for feedback, collaboration, or queries:

📧 Email: mondalmanas07@gmail.com

🔗 LinkedIn

Made using Python, XGBoost, and Streamlit.
