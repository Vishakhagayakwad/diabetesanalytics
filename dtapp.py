
import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
with open('diabetes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('sc.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Create the Streamlit web app
st.title('Diabetes Prediction App')

# Input fields
pregnancies = st.number_input('Pregnancies', min_value=0, value=0)
glucose = st.number_input('Glucose', min_value=0.0, value=0.0)
blood_pressure = st.number_input('Blood Pressure', min_value=0.0, value=0.0)
skin_thickness = st.number_input('Skin Thickness', min_value=0.0, value=0.0)
insulin = st.number_input('Insulin', min_value=0.0, value=0.0)
bmi = st.number_input('BMI', min_value=0.0, value=0.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, value=0.0)
age = st.number_input('Age', min_value=0, max_value=120, value=0)

# Prepare the feature vector
features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]], dtype=np.float64)

# Scale the features
features_scaled = scaler.transform(features)

# Predict using the loaded model
predicted_class = model.predict(features_scaled)

# Display the result
if st.button('Predict'):
    if predicted_class[0] == 1:
        st.write("Prediction: You have Diabetes.")
    else:
        st.write("Prediction: You do not have Diabetes.")
