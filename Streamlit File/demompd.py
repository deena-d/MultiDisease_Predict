# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:12:17 2023

@author: DD
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Load your trained models
diabetes_model = pickle.load(open("D:/trained model/diabetes_trained.sav", 'rb'))
breast_cancer_model = pickle.load(open('D:/trained model/Breast_cancer_trained.sav', 'rb'))
parkinson_model = pickle.load(open('D:/trained model/parkinson_trained.sav', 'rb'))
heart_disease_model = pickle.load(open('D:/trained model/Heart_disease_trained.sav', 'rb'))

# Create a Streamlit sidebar in landscape mode
st.set_page_config(layout="wide")

# Define custom CSS for styling
st.markdown("""
<style>
    .stSelectbox {
        background-color: #013220;
        color: #333333;
    }
    .stButton button {
        background-color: #008C76;
        color: #FFFFFF;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #4CAF50;
        color: #FFFFFF;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
    }
    .stTextInput input {
        background-color: #f4f4f4;
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

# Add a title and description
st.title("Multi Disease Prediction")
st.subheader("Predict various diseases with this app")

with st.sidebar:
    st.title("Select a Disease Prediction")
    selected = option_menu(
        menu_title="Select a Disease Prediction",
        options=["⚕ Diabetes predict", "🤱 Breast Cancer predict", "🫀 Heart Disease predict", "☢ Parkinson predict"],
        icons=['activity', 'yelp', 'heart-pulse', 'person'],
        default_index=0,
        orientation="horizontal",
    )

# Main content area

if selected == '⚕ Diabetes predict':
    st.title("Diabetes Prediction")

    st.markdown('''**Attribute Information:**

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)''')

    Pregnancies = st.text_input("Number of times pregnant")
    Glucose = st.text_input("Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    BloodPressure = st.text_input("Diastolic blood pressure (mm Hg)")
    SkinThickness = st.text_input("Triceps skin fold thickness (mm)")
    Insulin = st.text_input("2-Hour serum insulin (mu U/ml)")
    BMI = st.text_input("Body mass index (weight in kg/(height in m)^2)")
    DiabetesPedigreeFunction = st.text_input("Diabetes pedigree function")
    Age = st.text_input("Age")

    diabetic_diagnosis = ''

    if st.button('⚕ Diabetes predict Result'):
        diabetic_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diabetic_prediction[0] == 1:
            diabetic_diagnosis = 'The person is diabetic'
        else:
            diabetic_diagnosis = 'The person is not diabetic'

    st.markdown(diabetic_diagnosis, unsafe_allow_html=True)

# Repeat the similar styling for other disease predictions
# ...

# Optionally, you can add a footer with some information
st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.info("This app is for educational purposes only. Do not use the predictions for medical decisions.")


# ... (previous code)

# Main content area

# ... (previous code)

# Main content area

if selected == '🤱 Breast Cancer predict':
    st.title('Breast Cancer Prediction')

    st.markdown('''**Attribute Information:**

- a) radius (mean of distances from center to points on the perimeter)

- b) texture (standard deviation of gray-scale values)

- c) perimeter

- d) area

- e) smoothness (local variation in radius lengths)

- f) compactness (perimeter^2 / area - 1.0)

- g) concavity (severity of concave portions of the contour)

- h) concave points (number of concave portions of the contour)

- i) symmetry

- j) fractal dimension ("coastline approximation" - 1)

- The mean, standard error and "worst" or largest (mean ofthe three largest values) of these features were computed for each image, resulting in 30 features. 

- For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.''')

    radius_mean = st.text_input("Mean of distances from center to points on the perimeter")
    texture_mean  = st.text_input("Standard deviation of gray-scale values")
    perimeter_mean = st.text_input("Perimeter_mean")
    area = st.text_input("Area_mean ")
    smoothness_mean  = st.text_input("local variation in radius lengths")
    compactness_mean  = st.text_input("Perimeter^2 / area - 1.0")
    concavity_mean  = st.text_input("Severity of concave portions of the contour")
    concave_points_mean = st.text_input("Number of concave portions of the contour")
    symmetry_mean    = st.text_input(" Symmetry_mean   ")
    fractal_dimension_mean = st.text_input("Coastline approximation")
    radius_se = st.text_input("Radius Standard error")
    texture_se   = st.text_input("Texture Standard error  ")
    perimeter_se = st.text_input("Perimeter Standard error  ")
    area_se = st.text_input("area Standard error")
    smoothness_se = st.text_input("Smoothness Standard error")
    compactness_se = st.text_input("Compactness Standard error")
    concavity_se = st.text_input("Concavity Standard error")
    concave_points_se = st.text_input("Concave Points Standard error")
    symmetry_se = st.text_input("Symmetry Standard error")
    fractal_dimension_se = st.text_input("Fractal Dimension Standard error")
    radius_worst = st.text_input("Radius Worst")
    texture_worst = st.text_input("Texture Worst ")
    perimeter_worst  = st.text_input("Perimeter Worst")
    area_worst = st.text_input("Area Worst")
    smoothness_worst = st.text_input("Smoothness Worst")
    compactness_worst = st.text_input("Compactness Worst")
    concavity_worst  = st.text_input("Concavity Worst ")
    concave_points_worst = st.text_input("Concave Points Worst")
    symmetry_worst = st.text_input("Symmetry Worst")
    fractal_dimension_worst = st.text_input("Fractal Dimension Worst")

    breast_diagnosis = ''

    if st.button('🤱 Breast Cancer predict Result'):
        
        
        # Add your breast cancer prediction logic here using the input values
        # Example: breast_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, ...]])
        # You should use your trained model for prediction

        # Placeholder result (customize with your model's actual output)
        breast_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area, smoothness_mean, compactness_mean, concavity_mean,concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]]) # 0 for benign, 1 for malignant

        if breast_prediction == 0:
            breast_diagnosis = 'The Breast cancer is Benign, no worry'
        else:
            breast_diagnosis = 'The Breast Cancer is Malignant, serious stage'

    st.markdown(breast_diagnosis, unsafe_allow_html=True)

if selected == '🫀 Heart Disease predict':
    st.title('Heart Disease Prediction')

    st.markdown('''**Attribute Information:**

1. Age: Age in years
2. Sex: Sex (1 = male; 0 = female)
3. Chest Pain Type:
   - 0: Typical angina
   - 1: Atypical angina
   - 2: Non-anginal pain
   - 3: Asymptomatic
4. Resting Blood Pressure: Resting blood pressure (in mm Hg on admission to the hospital)
5. Serum Cholestoral: Serum cholestoral in mg/dl
6. Fasting Blood Sugar: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
7. Resting ECG Results:
   - 0: Normal
   - 1: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
   - 2: Showing probable or definite left ventricular hypertrophy by Estes' criteria
8. Maximum Heart Rate Achieved: Maximum heart rate achieved
9. Exercise Induced Angina: Exercise induced angina (1 = yes; 0 = no)
10. ST Depression: ST depression induced by exercise relative to rest
11. Slope: The slope of the peak exercise ST segment
   - 0: Upsloping
   - 1: Flat
   - 2: Downsloping
12. Number of Major Vessels: Number of major vessels (0-3) colored by fluoroscopy
13. Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect and the label''')

    age = st.text_input("Age")
    sex = st.radio("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
    trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
    chol = st.text_input("Serum Cholestoral (mg/dl)")
    fbs = st.checkbox("Fasting Blood Sugar > 120 mg/dl")
    restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    thalach = st.text_input("Maximum Heart Rate Achieved")
    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.text_input("ST Depression Induced by Exercise")
    slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])
    thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])

    heart_diagnosis = ''

    if st.button('🫀 Heart Disease predict Result'):
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
       
        # Add your heart disease prediction logic here using the input values
        # Example: heart_prediction = heart_disease_model.predict([[age, sex, cp, ...]])
        # You should use your trained model for prediction

        # Placeholder result (customize with your model's actual output)
          # 0 for healthy, 1 for heart disease

        if heart_prediction == 0:
            heart_diagnosis = 'The person is healthy'
        else:
            heart_diagnosis = 'The person has heart disease'

    st.markdown(heart_diagnosis, unsafe_allow_html=True)

if selected == '☢ Parkinson predict':
    st.title('Parkinson Prediction')

    st.markdown('''**Attribute Information:**

- MDVP Fo(Hz): Average vocal fundamental frequency
- MDVP Fhi(Hz): Maximum vocal fundamental frequency
- MDVP Flo(Hz): Minimum vocal fundamental frequency
- MDVP Jitter(%): MDVP Jitter(%)
- MDVP Jitter(Abs): MDVP Jitter(Abs)
- MDVP RAP: MDVP RAP
- MDVP PPQ: MDVP PPQ
- Jitter DDP: Several measures of variation in fundamental frequency
- MDVP Shimmer: MDVP Shimmer
- MDVP Shimmer(dB): MDVP Shimmer(dB)
- Shimmer APQ3: Shimmer APQ3
- Shimmer APQ5: Shimmer APQ5
- MDVP APQ: MDVP APQ
- Shimmer DDA: Shimmer DDA
- NHR: Two measures of the ratio of noise to tonal components in the voice
- HNR: Two measures of the ratio of noise to tonal components in the voice
- RPDE: Two nonlinear dynamical complexity measures
- DFA: Signal fractal scaling exponent
- spread1: Spread1
- spread2: Spread2
- D2: Two nonlinear dynamical complexity measures
- PPE: PPE''')

    MDVP_Fo = st.text_input("MDVP Fo(Hz)")
    MDVP_Fhi = st.text_input("MDVP Fhi(Hz)")
    MDVP_Flo = st.text_input("MDVP Flo(Hz)")
    MDVP_Jitter = st.text_input("MDVP Jitter(%)")
    MDVP_Jitter_Abs = st.text_input("MDVP Jitter(Abs)")
    MDVP_RAP = st.text_input("MDVP RAP")
    MDVP_PPQ = st.text_input("MDVP PPQ")
    Jitter_DDP = st.text_input("Jitter DDP")
    MDVP_Shimmer = st.text_input("MDVP Shimmer")
    MDVP_Shimmer_dB = st.text_input("MDVP Shimmer(dB)")
    Shimmer_APQ3 = st.text_input("Shimmer APQ3")
    Shimmer_APQ5 = st.text_input("Shimmer APQ5")
    MDVP_APQ = st.text_input("MDVP APQ")
    Shimmer_DDA = st.text_input("Shimmer DDA")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")

    parkinson_diagnosis = ''

    if st.button('☢ Parkinson predict Result'):
        parkinson_prediction = diabetes_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
       
        # Add your Parkinson's disease prediction logic here using the input values
        # Example: parkinson_prediction = parkinson_model.predict([[MDVP_Fo, MDVP_Fhi, MDVP_Flo, ...]])
        # You should use your trained model for prediction

        # Placeholder result (customize with your model's actual output)
          # 0 for healthy, 1 for Parkinson's disease

        if parkinson_prediction == 0:
            parkinson_diagnosis = 'The person is Healthy'
        else:
            parkinson_diagnosis = 'The person has Parkinson\'s disease'

    st.markdown(parkinson_diagnosis, unsafe_allow_html=True)

# ... (footer and other sections)
