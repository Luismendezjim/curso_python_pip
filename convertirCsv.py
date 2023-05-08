import pandas as pd

# Cargar el archivo CSV en un objeto DataFrame
df = pd.read_csv('FoodMart-Transactions-1997.csv')
# Crear una nueva columna "Fecha_Nueva" con el formato "DD/MM/AA"
df['transaction_date_new'] = pd.to_datetime(df['transaction_date'], format='%m/%d/%y').dt.strftime('%d/%m/%y')

# Guardar el nuevo archivo CSV
df.to_csv('nuevo_archivo.csv', index=False)


