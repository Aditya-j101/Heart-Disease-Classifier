🫀 Heart Disease Prediction App
An interactive web app to predict the likelihood of heart disease based on patient health metrics, built using Logistic Regression and deployed via Streamlit.

🚀 Try the Live App →
https://heart-disease-classifiergit-aglapdq6kbohwzusmy7v3c.streamlit.app/

📊 About the Project
Heart disease is a leading cause of death worldwide. This project uses machine learning to predict whether a patient has heart disease based on 13 clinical features from the UCI Heart Disease dataset.

The model used is a Logistic Regression classifier, trained and evaluated for maximum accuracy.

🧠 Features
Trained on the UCI Heart Disease dataset

Model built using Logistic Regression

Clean and intuitive Streamlit UI

Live prediction with real-time model inference

Responsive, mobile-friendly layout

Feature explanations and built-in data validation

🖼️ Demo
<img width="1132" height="791" alt="Screenshot 2025-07-29 193831" src="https://github.com/user-attachments/assets/6bbe2510-ff85-4646-be63-ee198d268fd5" />


📁 Dataset
Source: UCI Heart Disease Dataset

Columns:

age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

🛠️ Tech Stack
Component	Description
💻 Language	Python
📚 ML Model	Logistic Regression
📈 ML Library	scikit-learn
🧰 Deployment	Streamlit
📦 Package Mgmt	joblib, pandas, streamlit

🧪 Model Training
LogisticRegression(solver='liblinear', C=0.233)

Trained on 80% split using stratified sampling

Evaluated on 20% test data

Accuracy: ~86%
