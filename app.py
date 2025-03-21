import streamlit as st
import numpy as np
import pickle

# Load the trained model (replace 'xgboost_model.pkl' with your actual model file)
model = pickle.load(open('xgboost_model.pkl', 'rb'))

st.title("Wine Quality Prediction")
st.markdown(" Enter the wine characteristics to predict quality")

# Input fields for the features
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=15.0, value=7.5)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=1.5, value=0.5)
citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.36)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=20.0, value=6.1)
chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.071)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, max_value=100.0, value=17.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, max_value=300.0, value=102.0)
density = st.number_input("Density", min_value=0.990, max_value=1.010, value=0.9978)
pH = st.number_input("pH", min_value=2.0, max_value=4.5, value=3.35)
sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, value=0.8)
alcohol = st.number_input("Alcohol", min_value=0.0, max_value=20.0, value=10.5)

# Prediction function
def predict_wine_quality():
    input_data = (fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                  free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)

    # Convert input data to a numpy array and reshape
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data_as_numpy_array)

    # Display the prediction result
    if prediction[0] == 1:
        st.success("Good Quality Wine")
    else:
        st.error("Bad Quality Wine")

# Predict button
if st.button("Predict Quality"):
    predict_wine_quality()
