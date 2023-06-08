import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import folium
from streamlit_folium import folium_static

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


#Sidebar
st.sidebar.image(Image.open('src/images/hobib.png'))

url = 'https://www.booking.com'
enlace = "[Booking.com](" + url + ")"
st.sidebar.caption('## Reserva tu hotel accediendo en ' + enlace)

#3 Hoteles mas baratos
# Sort the DataFrame by price in ascending order to get the three cheapest hotels
cheapest_hotels = df.sort_values('precio').head(3)

# Display the three cheapest hotels
st.header('Top 3 Hoteles Baratos')
for index, hotel in cheapest_hotels.iterrows():
    st.subheader(hotel['nombre'])
    st.text('--------------------')
    st.write(f'**Distrito:** {hotel["distrito"]}')
    st.write(f'**Precio:** {hotel["precio"]} €')
    st.text('--------------------')

#Numero de hoteles por distrito.

# Group the data by 'distrito' and count the number of hotels in each district
district_counts = df['distrito'].value_counts()

# Create a pie chart
fig, ax = plt.subplots()
pie = ax.pie(district_counts.values, labels=None, autopct='%1.0f%%')

# Customize the labels to display the percentage of hotels
for i, p in enumerate(pie[0]):
    percentage = p.get_label()
    count = district_counts.values[i]
    p.set_label(f'{percentage} ({count})')

# Configure the plot
ax.legend(pie[0], district_counts.index, title='Distritos', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
st.header('Distribución de Hoteles por Distrito')

# Display the chart using Streamlit
st.pyplot(fig)



#Precio medio por distrito
# Calculate the mean price per district in euros
mean_prices = df.groupby('distrito')['precio'].mean().round().sort_values()

# Create a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(mean_prices.index, mean_prices.values)

# Add labels to the data points
for x, y in zip(mean_prices.index, mean_prices.values):
    ax.text(x, y, str(int(y)), ha='center', va='bottom')

# Configure the plot
ax.set_xlabel('Districts')
ax.set_ylabel('Price (€)')
st.header('Media Precio Hoteles por Distrito')

# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')

# Display the chart using Streamlit
st.pyplot(fig)


#MAPA

# Define the district names and their corresponding latitude and longitude coordinates
dic_distritos = {
    'Centro': (40.41831, -3.70275),
    'Arganzuela': (40.40021, -3.69618),
    'Retiro': (40.41317, -3.68307),
    'Salamanca': (40.42972, -3.67975),
    'Chamartín': (40.46206, -3.6766),
    'Tetuan': (40.45975, -3.6975),
    'Chamberi': (40.43404, -3.70379),
    'Fuencarral': (40.4984, -3.7314),
    'Moncloa': (40.43547, -3.7317),
    'Latina': (40.38897, -3.74569),
    'Carabanchel': (40.39094, -3.7242),
    'Usera': (40.38866, -3.70035),
    'Moratalaz': (40.40742, -3.664935),
    'Ciudad Lineal': (40.44505, -3.65132),
    'Hortaleza': (40.47444, -3.6411),
    'Villaverde': (40.35, -3.7),
    'Vallecas': (40.383, -3.6361),
    'Vicalvaro': (40.394, -3.60288),
    'San Blas': (40.43893, -3.61537),
    'Barajas': (40.4736600, -3.5777700)
}

# Calculate the median price per district
median_prices = df.groupby('distrito')['precio'].median()

# Calculate the maximum count of the most repeated rating by district
max_rating_counts = df.groupby('distrito')['rating'].apply(lambda x: x.value_counts().max())

# Create a map centered around Madrid
madrid_coords = (40.4168, -3.7038)
m = folium.Map(location=madrid_coords, zoom_start=12)

# Add markers for each district with the median price and most repeated rating as labels
for distrito, coords in dic_distritos.items():
    if distrito in median_prices.index and distrito in max_rating_counts.index:
        median_price = int(median_prices.loc[distrito])
        most_repeated_rating = df[df['distrito'] == distrito]['rating'].value_counts().idxmax()

        folium.Marker(
            location=coords,
            popup=f'Distrito: {distrito}\nPrecio: {median_price} €\nRating: {most_repeated_rating}',
            icon=folium.Icon(color='gray', icon='info-sign')
        ).add_to(m)

# Display the map using Streamlit
st.header('Precio Común y Rating Estrella por Distrito')
folium_static(m)

# Display the DataFrame
st.header('Datos')
st.dataframe(df)















