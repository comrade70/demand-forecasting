# Import required libraries for the application
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Cache the model and encoders
@st.cache_resource
def load_artifacts():
    # Open and load the trained XGBoost demand forecasting model from the pickle file
    with open("xgboost_demand_model.pkl", "rb") as f:
        model = pickle.load(f)

    # Open and load the label encoders used during model training
    with open("label_encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

    # Return both the model and encoders for use in the app
    return model, encoders

# Load the model and encoders when the app starts
model, label_encoders = load_artifacts()

st.title("Demand Forecasting Application")
st.divider()
st.header("Input Features")

price = st.number_input("Price", min_value=0.0, value=50.0)
discount = st.number_input("Discount (%)", min_value=0, max_value=100, value=10)
inventory_level = st.number_input("Inventory Level", min_value=0, value=100)
promotion = st.selectbox("Promotion", [0, 1])
competitor_pricing = st.number_input("Competitor Pricing", min_value=0.0, value=50.0)

# Select box for product category using the classes stored in the label encoder
category = st.selectbox(
    "Category",
    label_encoders["Category"].classes_.tolist()
)


# Create a DataFrame containing the user inputs
input_data = pd.DataFrame({
    "Price": [price],
    "Discount": [discount],
    "Inventory Level": [inventory_level],
    "Promotion": [promotion],
    "Competitor Pricing": [competitor_pricing],
    "Category": [category]
})

# Apply label encoding
for col, encoder in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = encoder.transform(input_data[col])
        
st.divider()

# Create a button that triggers the demand prediction
if st.button("Predict Demand"):
    prediction = model.predict(input_data)[0]

    # Display the predicted demand as a success message
    st.success(f"Predicted Demand: {int(prediction)} Units")