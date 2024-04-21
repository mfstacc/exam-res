import streamlit as st
import numpy as np

from pickle import load

features = {
    'Pregnancies': (0, 10, 4),
    'BloodPressure': (50, 120, 70),
    'DiabetesPedigreeFunction': (0.0, 2.0, 0.47),
    'Age': (10, 100, 33),
    'Glucose': (120, 300, 122),
    'BMI': (10.0, 45.0, 32.19)
}

models = {
    'Reglog': (
        load(open('./model_reglog.pkl', 'rb')),
        features
    ),
    'Árbol decisión': (
        load(open('./tree_classifier.pkl', 'rb')),
        {
            'Age': (10, 100, 33),
            'Glucose': (120, 300, 122),
            'BMI': (10.0, 45.0, 32.19)
        }
    )
}

st.title('Aplicación web para la predicción de diabetes')

with st.sidebar:
    st.title('Panel de configuración')

    st.header('Modelo de clasificación')

    selected_model = st.selectbox(label='Modelo',
                                  options=models.keys())
    model, features = models[selected_model]

    st.header('Ajuste de los parámetros')

    feat_values = []
    for name, vals in features.items():
        min, max, default = vals
        feat_values.append(st.slider(label=name, 
                                       min_value=min, 
                                       max_value=max, 
                                       value=default))
    input_values = np.array(feat_values).reshape(1, -1)

    predict = st.button(label='¡Predecir!🪬',
              type='primary')

if predict:
    prediction = model.predict(input_values)
    st.write(prediction)
    if prediction:
        st.error('El paciente está **enfermo**', icon='🤒')
    else:
        st.success('El paciente está **sano**', icon='👍')
