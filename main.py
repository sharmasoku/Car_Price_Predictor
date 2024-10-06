import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Page configuration
st.set_page_config(layout='wide', page_title='Car Price Predictor')

# Load the trained model
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

# Load the car dataset
car = pd.read_csv('Cleaned Car Dataset.csv')
car_name = sorted(car['name'].unique())
company = sorted(car['company'].unique())
year = sorted(car['year'].unique(), reverse=True)
fuel_type = sorted(car['fuel_type'].unique())

# Set up the black background for the entire app
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Heading section with a gradient background
st.markdown("""
    <div style="
        background: linear-gradient(90deg, rgba(0, 123, 255, 1) 0%, rgba(0, 63, 128, 1) 100%);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
        margin-bottom: 20px;
    ">
        <h1 style="
            color: white;
            font-family: 'Verdana', sans-serif;
            font-size: 3em;
            letter-spacing: 2px;
            animation: glowing 1.5s infinite;
        ">
            Welcome to <span style="color: #ADD8E6;">Car Price Predictor</span> 🚗
        </h1>
        <p style="
            color: #E0F7FA;
            font-size: 1.3em;
            margin-top: 10px;
            font-style: italic;
        ">
            Predict your car's value with precision and ease.
        </p>
    </div>

    <style>
        @keyframes glowing {
            0% { text-shadow: 0 0 5px #ADD8E6, 0 0 10px #ADD8E6; }
            50% { text-shadow: 0 0 20px #87CEFA, 0 0 30px #87CEFA; }
            100% { text-shadow: 0 0 5px #ADD8E6, 0 0 10px #ADD8E6; }
        }
    </style>
""", unsafe_allow_html=True)

# Selection widgets
selected_company = st.selectbox('Select Company', company)
if selected_company:
    filtered_model_name = [model for model in car_name if selected_company in model]
    selected_model = st.selectbox('Select Model', filtered_model_name)

selected_year = st.selectbox('Select Year of Purchase', year)
selected_fuel_type = st.selectbox('Select Fuel Type', fuel_type)
selected_kms_driven = st.text_input('Enter Number of Kilometers Driven')

# Predict button and display
button = st.button('Predict Price')
try:
    if button:
        # Prediction logic
        prediction = model.predict(pd.DataFrame([[selected_model, selected_company, selected_year, selected_kms_driven, selected_fuel_type]],
                                                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))

        # Formatting the price with commas and in INR format
        formatted_price = f"₹ {int(prediction[0]):,}"
        st.markdown("""
            <div style="background-color: #333; padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center;">
                <h2 style="color: green; font-size: 3em;">Predicted Price: {}</h2>
            </div>
        """.format(formatted_price), unsafe_allow_html=True)

except:
    st.warning('Please Provide Kilometers Driven by Car')
