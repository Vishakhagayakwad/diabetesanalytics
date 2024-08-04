# Diabetes Prediction Project

## Overview

I'm excited to share my latest project involving the analysis and prediction of diabetes using a real-world dataset. This project enhances my understanding of data science, focusing on data cleaning, visualization, and machine learning to predict diabetes outcomes based on various health factors.

## Dataset

The dataset includes features such as:
- **Insulin**
- **Glucose**
- **Age**
- **Blood Pressure**
- **Pregnancy History**
- **BMI**
- **Skin Thickness**
- **Other critical factors**

## Project Steps

### 1. Data Cleaning and Preprocessing

- **Initial Analysis:** Observed that columns like glucose and insulin had '0' values, which were replaced with NaN to reflect missing data more accurately.
- **Data Cleaning:** Cleaned the dataset by plotting histograms to analyze data distribution. Replaced NaN values with mean or median based on the data distribution.

### 2. Data Visualization

- **Box Plots:** Created box plots of diabetes outcomes against each factor affecting diabetes. This visualization helped understand the distribution and impact of each feature on the diabetes outcome.

### 3. Data Preparation

- **Feature Scaling:** Applied the `StandardScaler` technique to normalize the features, preparing the dataset for accurate model training.

### 4. Model Building and Evaluation

- **Machine Learning Models:** Implemented and evaluated different models:
  - Random Forest
  - Decision Tree
  - Support Vector Machine (SVM)
- **Cross-Validation:** Used cross-validation to ensure robustness and reliability of the results. Random Forest achieved the highest accuracy among the models.
- **Model Saving:** Saved the trained Random Forest model into a file using `pickle` for future use.

### 5. Application Development

- **Windows Application:** Developed a user-friendly application using the Tkinter library to predict diabetes likelihood based on input parameters such as glucose levels, insulin, age, and blood pressure.

- **Web Application:** Created a web application using Streamlit to enhance accessibility. The app allows users to input parameters such as glucose levels, BMI, skin thickness, and other medical details. It uses Streamlit's intuitive interface with `st.button` for prediction and `st.number_input` for data entry to quickly determine diabetes risk.


### Running the Applications

- **Tkinter Application:** Run the Tkinter application script using: `python tkinter_app.py`
- **Streamlit Application:** Run the Streamlit app using: `streamlit run streamlit_app.py`

## Technologies and Libraries Used

- Python
- NumPy
- Pandas
- scikit-learn
- StandardScaler
- Random Forest
- Decision Tree
- Support Vector Machine (SVM)
- pickle
- Tkinter
- Streamlit

## Results and Insights

The project successfully predicts diabetes likelihood using various machine learning models. The developed applications provide user-friendly interfaces for real-time predictions, enhancing accessibility and usability.



