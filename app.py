import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


disp_button =  st.button('Construir grafico dispercion')

if disp_button:
    st.write('creacion de un grafico de dispercion de datos de ventas de coches')
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    st.plotly_chart(fig, use_container_width=True)
