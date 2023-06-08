# HOBiB: 

![HOBiB Logo]('src/images/hobib.png')

HOBiB (Hotel Booking Information in Madrid) es un proyecto diseñado para extraer, limpiar, transformar y visualizar datos de hoteles en Madrid utilizando técnicas de ETL (Extract, Transform, Load) y web scraping con Selenium. El objetivo principal es obtener información relevante sobre los hoteles disponibles en la ciudad desde Booking.com y presentarla de manera visual y accesible a través de una interfaz interactiva creada con Streamlit.

## Procesos ETL

El proceso de extracción, transformación y carga de datos en HOBiB se realiza en varias etapas:

- **Extracción**: Se utiliza web scraping con Selenium para obtener información detallada de los hoteles en Madrid desde Booking.com. Se recopilan datos como el nombre del hotel, precio, distrito y rating.

- **Limpieza y transformación**: Utilizando la biblioteca de Python llamada Pandas, se lleva a cabo la limpieza y transformación de los datos extraídos. Se eliminan valores nulos, se ajusta el formato de los datos y se realizan cálculos o transformaciones necesarias para preparar los datos para su visualización.

- **Carga**: Los datos limpios y transformados se cargan en una estructura de datos adecuada para su posterior visualización y análisis.

## Web Scraping con Selenium

Selenium es una herramienta ampliamente utilizada para realizar web scraping en sitios web dinámicos. En el contexto de HOBiB, Selenium se utiliza para automatizar la interacción con el sitio web de Booking.com y extraer información de los hoteles en Madrid. Se simula la navegación de un usuario y se extraen los datos necesarios de cada página.

## Limpieza y Transformación con Pandas

Pandas es una biblioteca de Python ampliamente utilizada para el análisis y manipulación de datos. En HOBiB, se utiliza Pandas para realizar la limpieza y transformación de los datos extraídos. Esto puede incluir la eliminación de filas o columnas con valores nulos, el ajuste del formato de los datos, el cálculo de estadísticas descriptivas o cualquier otra transformación necesaria para preparar los datos para su visualización.

## Visualización con Streamlit

Streamlit es una biblioteca de Python que permite crear fácilmente aplicaciones web interactivas para la visualización de datos. En HOBiB, se utiliza Streamlit para crear una interfaz interactiva que permite a los usuarios explorar y visualizar los datos de los hoteles en Madrid. Se pueden crear gráficos, tablas y otros elementos visuales para presentar los datos de manera clara y comprensible.

## Retos en el Proceso

Durante el desarrollo del proyecto HOBiB, nos encontramos con algunos retos que fueron superados de la siguiente manera:

- **Ventanas emergentes (pop-up windows)**: En cada paso del proceso de web scraping con Selenium, nos enfrentamos a ventanas emergentes. Para manejar estas ventanas, utilizamos la estructura `try/except` para identificar y hacer clic en los elementos necesarios dentro de las ventanas emergentes.

  ```python
  try:
      popup_button = driver.find_element(By.CLASS_NAME, 'popup-button

-class')
      popup_button.click()
  except:
      # No se encontró ninguna ventana emergente, se continúa con la lógica de scraping
      pass
  ```

- **Filtros dinámicos**: Booking.com utiliza filtros dinámicos que se actualizan en tiempo real a medida que el usuario interactúa con ellos. Para abordar este desafío, utilizamos localizadores por XPath para encontrar y seleccionar los elementos específicos relacionados con los filtros dinámicos en el sitio web.

  ```python
  # Ejemplo de selección de un filtro dinámico utilizando XPath
  filter_element = driver.find_element(By.XPATH, "//div[contains(text(), 'Filter Text')]")
  filter_element.click()
  ```

## Creación de columnas "rating" y "distrito"

Para crear las columnas "rating" y "distrito" se inspeccionaron las filas donde se encontraba presente la string presente en la lista dada:

```python
distritos = ['Centro', 'Arganzuela', 'Retiro', 'Salamanca', 'Chamartín', 'Tetuan', 'Chamberi', 'Fuencarral', 'Moncloa', 'Latina', 'Carabanchel', 'Usera', 'Vallecas', 'Moratalaz', 'Ciudad Lineal', 'Hortaleza', 'Villaverde', 'Vicalvaro', 'San Blas', 'Barajas']  # Lista de nombres de distritos

# Crear una máscara booleana que indique si algún nombre de distrito está presente en cada celda
mask = df.applymap(lambda cell: any(name in str(cell) for name in distritos))

# Crear una nueva columna 'distrito' con los nombres de distrito coincidentes
df['distrito'] = df[mask].apply(lambda row: next((name for name in distritos if name in str(row.values)), None), axis=1)

# Crear una nueva columna 'rating' a partir del contenido de la columna 'distrito'
df['rating'] = df['distrito'].apply(lambda x: x.split(' ')[0] if isinstance(x, str) else None)

# Rellenar los valores nulos en la columna 'distrito' con 'Otro'
df['distrito'] = df['distrito'].fillna('Otro')

# Rellenar los valores nulos en la columna 'rating' con 0
df['rating'] = df['rating'].fillna(0)
```

Esta función crea una máscara booleana que verifica si algún nombre de distrito está presente en cada celda del DataFrame. Luego, se utiliza la máscara para seleccionar las filas que coinciden con los distritos y asignar el nombre del distrito correspondiente a la columna 'distrito'. A continuación, se crea la columna 'rating' a partir del contenido de la columna 'distrito', utilizando solo la parte del rating si está presente. Los valores nulos en las columnas 'distrito' y 'rating' se rellenan con 'Otro' y 0, respectivamente.

## Contribuciones y Contacto

Si estás interesado en contribuir a este proyecto, tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros. Puedes enviar un correo electrónico a [correo electrónico de contacto] o visitar nuestra página de GitHub en [enlace a tu repositorio en GitHub].

Esperamos que HOBiB sea una herramienta útil
