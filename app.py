import streamlit as st
import joblib
import pandas as pd

# Set page title and header
st.set_page_config(page_title="Sales Prediction App", layout="centered")
st.title("📈 Sales Prediction App")
st.write("Enter your advertising budgets below to predict the estimated sales.")

# Load the trained model safely using joblib
try:
    model = joblib.load('model.sav')
except Exception as e:
    st.error(f"Error loading the model. Ensure 'model.sav' is present. Details: {e}")
    st.stop()

# Create input form
with st.form("prediction_form"):
    tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, value=100.0, step=1.0)
    radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, value=20.0, step=1.0)
    newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, value=15.0, step=1.0)
    
    submit_button = st.form_submit_button("Predict Sales")

if submit_button:
    # Prepare the input data in the correct format with feature names matching the training set
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    
    # Run prediction
    prediction = model.predict(input_data)[0]
    
    st.success(f"🎯 Estimated Sales: **{prediction:.2f}** units")
