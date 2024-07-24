import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))

df = pd.read_csv("diabetes.csv",
                 dtype={'Pregnancies': np.float64,
                            'Glucose': np.float64,
                            'BloodPressure': np.float64,
                            'SkinThickness': np.float64,
                            'Insulin': np.float64,
                            'BMI': np.float64,
                            'DiabetesPedigreeFunction': np.float64,
                            'Age': np.float64,
                            'Outcome': np.float64})
st.title("Population of Canada")

years = df['Age'].astype(int)
min_year=years.min()
max_year=years.max()

Blood = df['BloodPressure'].astype(int)
min_Blood = Blood.min()+1
max_Blood = Blood.max()


with st.expander("see full data here"):
    st.write(df)

with st.form("population-form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("select the starting date")
        start_year = st.slider('Year', min_value=min_year,max_value=max_year,value=min_year,step=1)
        start_Blood = st.slider('BloodPressure', min_value=min_Blood, max_value=max_Blood, value=min_Blood, step=1)

    with col2:
        st.write("select the endind date")
        ending_year = st.slider('Year', min_value=min_year,max_value=max_year,value=max_year,step=1)
        ending_Blood = st.slider('BloodPressure', min_value=min_Blood, max_value=max_Blood, value=max_Blood, step=1)

    with col3:
        st.write("select the region")
        #target=st.selectbox("choose location",options=df.columns[1:], index=0)
        target = st.selectbox("choose location", options=["Glucose", "Insulin", "DiabetesPedigreeFunction"], index=0)

    submit_button=st.form_submit_button("Analyze", type="primary")


start_idx = df[(df["Age"] == start_year) & (df["BloodPressure"] >= start_Blood)].index[0]
end_idx = df[(df["Age"] == ending_year) & (df["BloodPressure"] <= ending_Blood)].index[0]
filtered_df = df.iloc[start_idx:end_idx + 1]


fig, ax = plt.subplots()
ax.bar(filtered_df['Age'], filtered_df[target])
ax.set_xlabel('Age')
ax.set_ylabel(target)
fig.autofmt_xdate()
st.pyplot(fig)


col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')

diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):

    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                  BMI, DiabetesPedigreeFunction, Age]

    user_input = [float(x) for x in user_input]

    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'

st.success(diab_diagnosis)
