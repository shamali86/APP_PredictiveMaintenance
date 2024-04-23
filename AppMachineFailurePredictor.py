import streamlit as st 
import pandas as pd 
import joblib
import sklearn
import numpy as np


model = joblib.load("classifier2")

st. title("Machine Failure Prediction")

Airtemperature = st.number_input("Input Airtemperature")
Processtemperature = st.number_input("Input Processtemperature")
Rotationalspeed = st.number_input("Input Rotationalspeed")
Torque = st.number_input("Input Torque")
Toolwear = st.number_input("Input Toolwear")

def predict():
    row = np.array([Airtemperature, Processtemperature, Rotationalspeed, Torque, Toolwear])
    X = pd.DataFrame([row])
    prediction = model.predict(X)[0]

    if prediction == 0:
        st.success('No Failure in Machine :thumbsup:')
    else:
        st.error('Machine Failure :thumbsup:')    

st.button('Predict', on_click=predict)