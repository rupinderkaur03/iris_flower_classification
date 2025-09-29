# app.py
import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load('svm_iris_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Iris Flower Classification using SVM")
st.write("Enter the flower measurements:")

# User inputs
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"The predicted class is: **{class_names[prediction[0]]}**")
