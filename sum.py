import pandas as pd

# Lee el primer archivo Excel
archivo1 = pd.read_excel('KLIMAS Q1.xlsx')

# Lee el segundo archivo Excel
archivo2 = pd.read_excel('KLIMAS Q2.xlsx')

# Concatena los dos DataFrames para asegurarnos de tener todos los nombres
todos_los_datos = pd.concat([archivo1, archivo2])

# Agrupa por el nombre y suma los valores
resultado = todos_los_datos.groupby('NOMBRE').agg({
    'DUI': 'first',  # Puedes ajustar esto según tu necesidad
    'Total devengado': 'sum',
    'ISSS': 'sum',
    'AFP': 'sum',
    'ISR': 'sum'
}).reset_index()

# Quita el carácter '-' de la columna "DUI"
resultado['DUI'] = resultado['DUI'].str.replace('-', '')

# Guarda el resultado en un nuevo archivo
resultado.to_excel('KLIMAS DIC 23.xlsx', index=False)




