import pickle
import streamlit as st
import numpy as np

with open("iris_dataset.pkl", "rb") as f:
    model = pickle.load(f)
    
st.title("Iris Flower Prediction 🌸")

species_map = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

SepalLengthCm = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
SepalWidthCm = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.1)
PetalLengthCm = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=4.35, step=0.1)
PetalWidthCm = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.3, step=0.1)

if st.button("Predict Flower Type"):
    input_data = np.array([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    prediction = model.predict(input_data)
    species_name = species_map.get(int(round(prediction[0])), "Unknown")
    st.success(f"🌼 The predicted Iris species is: **{species_name}**")
    