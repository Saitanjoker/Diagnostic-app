import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
st.title("Medical Diagnostic WebApp")

# step 1 : load the model
model = open("rfc.pickle","rb")
clf = pickle.load(model)
model.close()

# step 2 : Get the frontend end user input
pregs= st.number_input('Pregnancies',1,20,step=1)
glucose=st.slider('Glucose',40,200,40) 
bp=st.slider('BloodPressure',24,122,24)
skin = st.slider('SkinThickness',7,99,9)
insulin = st.slider('Insulin',18,850,18)
bmi = st.slider('BMI',18,67,18) 
dpf=st.slider('DiabetesPedigreeFunction',0.05,2.5,0.05) 
age=st.slider('Age',21,81,21)

#step 3: converting user input to model input
data = {"Pregnancies": pregs,
       "Glucose":glucose,
       "BloodPressure":bp,
       "SkinThickness":skin,
       "Insulin":insulin,
       "BMI":bmi,
       "DiabetesPedigreeFunction":dpf,
       "Age":age}
input_data =pd.DataFrame([data])

# step4 : get the predictions
pred = clf.predict(input_data)[0]
if st.button("Predict"):
    if pred == 1:
        st.error("The Person has Diabetes")
    if pred == 0:
        st.success("THe person has no Diabetes")
