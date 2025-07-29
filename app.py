import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("Hear-Disease-model.pkl")

st.title("💓 Heart Disease Prediction App")

# Collect user input
st.header("Enter Patient Data:")

age = st.slider("Age", 29, 77, 50)
sex = st.selectbox("Sex", options=["Male", "Female"])
cp = st.slider("Chest Pain Type (0-3)", 0, 3, 1)
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 94, 200, 130)
chol = st.slider("Cholesterol (mg/dl)", 126, 564, 250)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.slider("Max Heart Rate Achieved", 71, 202, 150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.2, 1.0)
slope = st.selectbox("Slope of ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible)", [0, 1, 2, 3])

# Convert sex to numeric
sex = 1 if sex == "Male" else 0

# Create dataframe
input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]],
                          columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease (Confidence: {prob:.2%})")
    else:
        st.success(f"✅ Low risk of heart disease (Confidence: {prob:.2%})")
