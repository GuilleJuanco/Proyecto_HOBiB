import pandas as pd
import numpy as np
import regex as re

#Investigacion
#POSIBLES PARAMETROS FUNCION: DF21 Y .CSV

#Pasar a DF
df21=pd.read_csv('../data/21.csv')

#Nombres hotel

# Check if 'string x' is present in column 1
mask = df21['0'].str.contains('Desayuno incluido')

# Assign values from column 2 to column 1 where 'Desayuno incluido' is present
df21.loc[mask, '0'] = df21.loc[mask, '1']

# Drop column 2
df21.drop('1', axis=1, inplace=True)

# Keep unique values in Hotel
df21['0'] = df21['0'].drop_duplicates()

#Renombrar columna
df21 = df21.rename(columns={'0': 'nombre'})

#Distrito

distritos = ['Centro', 'Arganzuela','Retiro', 'Salamanca', 'Chamartín', 'Tetuan', 'Chamberi', 'Fuencarral', 'Moncloa', 'Latina', 'Carabanchel', 'Usera', 'Vallecas', 'Moratalaz', 'Ciudad Lineal', 'Hortaleza', 'Villaverde', 'Vicalvaro', 'San Blas', 'Barajas']  # List of district names

# Create a boolean mask indicating if any district name is present in each cell
mask = df21.applymap(lambda cell: any(name in str(cell) for name in distritos))

# Create a new column 'distritos' with the matching district names
df21['distrito'] = df21[mask].apply(lambda row: next((name for name in distritos if name in str(row.values)), None), axis=1)

#Precio

# Create a new column 'price' and initialize it with None
df21['price'] = None

# Define a regular expression pattern to match the price
pattern = r'€\s*(\d+([.,]\d{1,2})?)'

# Define a lambda function to extract the price and convert it to an integer
def extract_price(row):
    for col in row.index:
        value = str(row[col])
        match = re.search(pattern, value)
        if match:
            price_str = match.group(1).replace(',', '')
            price_int = int(float(price_str.replace('.', '')))
            return price_int
    return None

# Apply the lambda function to each row and assign the extracted price to the 'price' column
df21['price'] = df21.apply(lambda row: extract_price(row), axis=1)

#Rating

ratings = ['Agradable', 'Bien','Muy bien', 'Fabuloso', 'Fantástico']  # List of district names

# Crea sistema booleano para analizar si los elementos de la lista se encuentran en alguna celda
mask = df21.applymap(lambda cell: any(name in str(cell) for name in ratings))

# Crea nueva columna con ratings
df21['rating'] = df21[mask].apply(lambda row: next((name for name in ratings if name in str(row.values)), None), axis=1)
