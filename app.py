import streamlit as st
import pandas as pd
import numpy as np
import pickle


with open('random_forest_model.h5','rb') as file:
    model = pickle.load(file)

# Set up the Streamlit app
st.title("Steam Owners Classification")
st.write("Enter the dimensions of an steam games to classify its owners.")

# Collect user input
english = st.sidebar.selectbox('english', [0, 1], index=0)
required_age = st.sidebar.slider('Required Age', 0, 18, 0)
positive_ratings = st.sidebar.number_input('Positive Ratings', min_value=0, step=1, value=0)
negative_ratings = st.sidebar.number_input('Negative Ratings', min_value=0, step=1, value=0)
overall_ratings = st.sidebar.number_input('Overall Ratings', min_value=0, step=1, value=0)
average_playtime = st.sidebar.number_input('Average Playtime', min_value=0, step=1, value=0)
median_playtime = st.sidebar.number_input('Median Playtime', min_value=0, step=1, value=0)
price = st.sidebar.number_input('Price', min_value=0.0, step=0.01, value=0.0)
software_training = st.sidebar.selectbox('Software Training', [0, 1], index=0)
video_production = st.sidebar.selectbox('Video Production', [0, 1], index=0)
massively_multiplayer = st.sidebar.selectbox('Massively Multiplayer', [0, 1], index=0)
education = st.sidebar.selectbox('Education', [0, 1], index=0)
nudity = st.sidebar.selectbox('Nudity', [0, 1], index=0)
photo_editing = st.sidebar.selectbox('Photo Editing', [0, 1], index=0)
violent = st.sidebar.selectbox('Violent', [0, 1], index=0)
rpg = st.sidebar.selectbox('RPG', [0, 1], index=0)
sports = st.sidebar.selectbox('Sports', [0, 1], index=0)
racing = st.sidebar.selectbox('Racing', [0, 1], index=0)
adventure = st.sidebar.selectbox('Adventure', [0, 1], index=0)
design_illustration = st.sidebar.selectbox('Design & Illustration', [0, 1], index=0)
game_development = st.sidebar.selectbox('Game Development', [0, 1], index=0)
accounting = st.sidebar.selectbox('Accounting', [0, 1], index=0)
web_publishing = st.sidebar.selectbox('Web Publishing', [0, 1], index=0)
simulation = st.sidebar.selectbox('Simulation', [0, 1], index=0)
action = st.sidebar.selectbox('Action', [0, 1], index=0)
early_access = st.sidebar.selectbox('Early Access', [0, 1], index=0)
casual = st.sidebar.selectbox('Casual', [0, 1], index=0)
audio_production = st.sidebar.selectbox('Audio Production', [0, 1], index=0)
sexual_content = st.sidebar.selectbox('Sexual Content', [0, 1], index=0)
animation_modeling = st.sidebar.selectbox('Animation & Modeling', [0, 1], index=0)
indie = st.sidebar.selectbox('Indie', [0, 1], index=0)
utilities = st.sidebar.selectbox('Utilities', [0, 1], index=0)
free_to_play = st.sidebar.selectbox('Free to Play', [0, 1], index=0)
tutorial = st.sidebar.selectbox('Tutorial', [0, 1], index=0)
gore = st.sidebar.selectbox('Gore', [0, 1], index=0)
strategy = st.sidebar.selectbox('Strategy', [0, 1], index=0)
documentary = st.sidebar.selectbox('Documentary', [0, 1], index=0)
windows = st.sidebar.selectbox('Windows', [0, 1], index=0)
linux = st.sidebar.selectbox('Linux', [0, 1], index=0)
mac = st.sidebar.selectbox('Mac', [0, 1], index=0)
classify_button = st.button("Classify")
user_input = {
    'english': 0,
    'required_age': 0,
    'positive_ratings': 0,
    'negative_ratings': 0,
    'average_playtime': 0,
    'median_playtime': 0,
    'price': 0,
    'overall_reviews': 0,
    'Design & Illustration': 0,
    'Animation & Modeling': 0,
    'Audio Production': 0,
    'Software Training': 0,
    'Accounting': 0,
    'Tutorial': 0,
    'Racing': 0,
    'Simulation': 0,
    'Utilities': 0,
    'Sports': 0,
    'Gore': 0,
    'Sexual Content': 0,
    'Free to Play': 0,
    'Photo Editing': 0,
    'Casual': 0,
    'Early Access': 0,
    'Web Publishing': 0,
    'Documentary': 0,
    'Indie': 0,
    'Violent': 0,
    'Adventure': 0,
    'RPG': 0,
    'Massively Multiplayer': 0,
    'Strategy': 0,
    'Video Production': 0,
    'Game Development': 0,
    'Education': 0,
    'Nudity': 0,
    'Action': 0,
    'windows': 0,
    'linux': 0,
    'mac': 0
}
if classify_button:
    user_input['english'] = [english]
    user_input['required_age'] = [required_age]
    user_input['positive_ratings'] = [positive_ratings]
    user_input['overall_reviews'] = [overall_ratings]
    user_input['negative_ratings'] = [negative_ratings]
    user_input['average_playtime'] = [average_playtime]
    user_input['median_playtime'] = [median_playtime]
    user_input['price'] = [price]
    user_input['Nudity'] = [nudity]
    user_input['Casual'] = [casual]
    user_input['Web Publishing'] = [web_publishing]
    user_input['Massively Multiplayer'] = [massively_multiplayer]
    user_input['Racing'] = [racing]
    user_input['Sexual Content'] = [sexual_content]
    user_input['Simulation'] = [simulation]
    user_input['Game Development'] = [game_development]
    user_input['Tutorial'] = [tutorial]
    user_input['Education'] = [education]
    user_input['Sports'] = [sports]
    user_input['Adventure'] = [adventure]
    user_input['Action'] = [action]
    user_input['Strategy'] = [strategy]
    user_input['Design & Illustration'] = [design_illustration]
    user_input['Free to Play'] = [free_to_play]
    user_input['Indie'] = [indie]
    user_input['Documentary'] = [documentary]
    user_input['Utilities'] = [utilities]
    user_input['Gore'] = [gore]
    user_input['Audio Production'] = [audio_production]
    user_input['Video Production'] = [video_production]
    user_input['RPG'] = [rpg]
    user_input['Animation & Modeling'] = [animation_modeling]
    user_input['Photo Editing'] = [photo_editing]
    user_input['Early Access'] = [early_access]
    user_input['Violent'] = [violent]
    user_input['Software Training'] = [software_training]
    user_input['Accounting'] = [accounting]
    user_input['windows'] = [windows]
    user_input['linux'] = [linux]
    user_input['mac'] = [mac]
    
    # Convert the user input dictionary to a DataFrame
    user_input_df = pd.DataFrame(user_input)
    user_input_df
    # Make the prediction using the trained model
    predictions = model.predict(user_input_df)
    ans = f'the numbers of owners you can expect from a game like this is around {predictions}'
    ans    
