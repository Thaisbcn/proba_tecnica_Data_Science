# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import joblib
from prophet import Prophet
import matplotlib.pyplot as plt

# Cargar el modelo entrenado
model = joblib.load(r'C:\\Users\\thais\\Documents\\00_MACHINE_LEARNING\\PROVA TECNICA DATA SCIENCE\\prophet_model.pkl')

# Cargar los datos
file_path = r"C:\\Users\\thais\\Documents\\00_MACHINE_LEARNING\\PROVA TECNICA DATA SCIENCE\\LOCALES.csv"
data = pd.read_csv(file_path, low_memory=False)

# Preparar los datos
df_analysis = data[['Data_Revisio', 'Codi_Districte', 'Nom_Principal_Activitat']].dropna()
df_analysis['Data_Revisio'] = pd.to_datetime(df_analysis['Data_Revisio'], errors='coerce')
df_analysis['Activo'] = df_analysis['Nom_Principal_Activitat'].notna().astype(int)
activity_trend_location = df_analysis.groupby(['Data_Revisio', 'Codi_Districte'])['Activo'].sum()

# Interfaz de Streamlit
st.title('Predicción de Locales Activos por Distrito')

# Entrada del usuario para el distrito
distrito = st.selectbox('Selecciona el distrito', df_analysis['Codi_Districte'].unique())

# Entrada para el número de días a predecir
num_days = st.number_input('Número de días para predecir', min_value=1, max_value=365, value=30)

# Preparar los datos para el distrito seleccionado
df_prophet_district = activity_trend_location.xs(distrito, level='Codi_Districte').reset_index()
df_prophet_district.columns = ['ds', 'y']

# Realizar predicción con el modelo
future = model.make_future_dataframe(df_prophet_district, periods=num_days)
forecast = model.predict(future)

# Graficar la predicción
st.write(f"Predicción de locales activos para el distrito {distrito} en los próximos {num_days} días.")
st.line_chart(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].set_index('ds'))
