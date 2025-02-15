import os 
import json
from PIL import Image

import numpy as np
import pandas as pd
import tensorflow as tf
import streamlit as st

model_path = 'M:\\Projects\\Plant Disease Prediction with CNN\\plant_disease_prediction_model.h5'

model = tf.keras.models.load_model(model_path)

class_indices_path = 'M:\\Projects\\Plant Disease Prediction with CNN\\class_indices.json'
with open(class_indices_path, 'r') as f:
    class_indices = json.load(f)

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load the image
    img = Image.open(image_path)

    img = img.resize(target_size)

    img_array = np.array(img)

    img_array = np.expand_dims(img_array, axis=0)
    # Scale the image values to [0, 1]
    img_array = img_array.astype('float32') / 255.
    return img_array

def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)] 
    return predicted_class_name

# Streamlit App
st.title('PlantMedix')

st.write("""
    **PlantMedix** is a machine learning-powered tool designed to assist farmers in identifying the health of their plant leaves. 
    By simply uploading an image of a plant leaf, this app can classify it as either **healthy** or **diseased**, helping farmers 
    quickly detect and respond to plant health issues.
    
    This app  trained on a wide variety of plant diseases to recognize common symptoms and anomalies 
    in leaf images. With the accurate predictions provided by the app, farmers can take informed actions to protect their crops 
    and ensure a healthy harvest.
""")


uploaded_img = st.file_uploader('Upload the image:', type=['jpg', 'png', 'jpeg'])

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((150, 150))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):

            img_path = os.path.join("M:\Projects\Plant Disease Prediction with CNN\test", uploaded_img.name)

            actual_class_name = (img_path.split('_'))
            actual_name = (' '.join((actual_class_name[1:4])))
            st.write(f'Actual Class: {actual_name}')

            predict = predict_image_class(model, uploaded_img, class_indices)
            st.success(f'Prediction: {predict}')
