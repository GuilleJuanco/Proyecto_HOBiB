import streamlit as st
import pandas as pd

st.title('HOBiB')
st.header('Hoteles en Madrid')

df = pd.read_csv('src/data/booking.csv')

nombre, distrito, precio, rating, checkin, plan = st.columns(6)

with nombre:
    nombre_filter = st.text_input('Nombre Hotel')
    if nombre_filter:
        df = df[df['nombre'].str.contains(nombre_filter, case=False)]

with distrito:
    distrito_selected = st.selectbox('Distrito', [''] + list(df.distrito.unique()))
    if distrito_selected:
        df = df[df['distrito'] == distrito_selected]

with precio:
    precio_min, precio_max = st.slider('Precio',
                                       min_value=df['precio'].min(),
                                       max_value=df['precio'].max(),
                                       value=(df['precio'].min(), df['precio'].max()))
    df = df[(df['precio'] >= precio_min) & (df['precio'] <= precio_max)]

with rating:
    rating_selected = st.selectbox('Rating', [''] + list(df.rating.unique()))
    if rating_selected:
        df = df[df['rating'] == rating_selected]

with checkin:
    fecha_seleccionada = st.date_input('Check-in')
    if fecha_seleccionada:
        df = df[df['checkin'] == str(fecha_seleccionada)]

with plan:
    plan_selected = st.selectbox('Plan', [''] + list(df.plan.unique()))
    if plan_selected:
        df = df[df['plan'] == plan_selected]

st.caption('Datos')
st.dataframe(df)
