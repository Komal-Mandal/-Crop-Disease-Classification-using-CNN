import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

# Class names
class_names = ['Potato__Early_blight', 'Potato_Late_blight', 'Potato__healthy']

# Image properties
IMAGE_SIZE = 255

# Function to preprocess and predict
def predict(img):
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence

# Streamlit app
st.title("Potato Disease Classification")

st.write("Upload an image of a potato leaf to predict if it has Early Blight, Late Blight, or is Healthy.")

# File upload
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=300)

    

    # Predict button
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            
            predicted_class, confidence = predict(image)
        st.success(f"Prediction: {predicted_class}")
        st.info(f"Confidence: {confidence}%")
else:
    st.warning("Please upload an image file.")