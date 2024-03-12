import streamlit as st
from pickle import load
import numpy as np

st.title('Valoración del riesgo de diabetes')

model = load(open('model_reglog.pkl', 'rb'))

with st.sidebar:
    st.title('Parámetros')

    pregancies = st.slider(label='pregnancies', min_value=0, max_value=10, value=4)
    glucose = st.slider(label='glucose', min_value=120, max_value=300, value=122)
    blood_pressure = st.slider(label='blood_pressure', min_value=50, max_value=120, value=70)
    skin_thickness = st.slider(label='skin_thickness', min_value=5, max_value=50, value=21)
    bmi = st.slider(label='bmi', min_value=10.0, max_value=45.0, value=32.19)
    dpf = st.slider(label='dpf', min_value=0.0, max_value=2.0, value=0.47)
    age = st.slider(label='age', min_value=10, max_value=100, value=33)

    predict_button = st.button(label='Predict', type='primary')
    parameters = np.array([pregancies, glucose, blood_pressure, skin_thickness, bmi, dpf, age])

if predict_button:
    outcome = model.predict(parameters.reshape(1, -1))
    if not outcome:
        st.success('El paciente no está en riesgo de padecer diabetes', icon='👍')
    else:
        st.error('El paciente está en riesgo de padecer diabetes', icon='🤒')