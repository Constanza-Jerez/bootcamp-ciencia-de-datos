'''
1. Definir Variables 
● Identificar el tipo de variable (categórica, cuantitativa discreta o continua) de cada columna en el conjunto de datos.
2. Construcción de una Tabla de Frecuencia 
● Generar una tabla de frecuencia para una variable categórica y otra para una variable cuantitativa discreta.
3. Cálculo de Medidas de Tendencia Central 
● Calcular la media, mediana y moda de una variable cuantitativa.
4. Cálculo de Medidas de Dispersión 
● Calcular el rango, varianza y desviación estándar de la misma variable utilizada en el punto anterior.
5. Visualización de Datos 
Crear un histograma para una variable cuantitativa y un boxplot para otra variable del dataset.
'''

# importar librerias a usar
import pandas as pd # lectura
from pathlib import Path # lectura
import matplotlib.pyplot as plt # visualizacion
import seaborn as sns # visualizacion

ruta = Path(__file__).parent / 'datos_estadistica.csv'
print(ruta)

df = pd.read_csv(ruta)
print(df.info())
print(df.head(10))

'''
1. Definir Variables 
● Identificar el tipo de variable (categórica, cuantitativa discreta o continua) de cada columna en el conjunto de datos.
'''

# ID       | cuantitativa discreta
# Nombre   | categorica
# Edad     | cuantitativa discreta
# Ingresos | cuantitativa discreta   
# Genero   | categorica        
# Ciudad   | categorica

'''
2. Construcción de una Tabla de Frecuencia 
● Generar una tabla de frecuencia para una variable categórica y otra para una variable cuantitativa discreta.
'''
print(df["Genero"].value_counts())
print(df["Edad"].value_counts())

# tabla de frecuencia para variable categorica
tabla_frecuencia = df["Genero"].value_counts().sort_index().to_frame("Frecuencia Absoluta")
tabla_frecuencia["Frecuencia Relativa"] = tabla_frecuencia["Frecuencia Absoluta"] / tabla_frecuencia["Frecuencia Absoluta"].sum()
tabla_frecuencia["Frecuencia Acumulada"] = tabla_frecuencia["Frecuencia Absoluta"].cumsum()
tabla_frecuencia["Frecuencia Relativa Acumulada"] = tabla_frecuencia["Frecuencia Relativa"].cumsum()
print(f'{tabla_frecuencia} \n')

# tabla de frecuencia para variable cuantitativa
tabla_frecuencia = df["Edad"].value_counts().sort_index().to_frame("Frecuencia Absoluta")
tabla_frecuencia["Frecuencia Relativa"] = tabla_frecuencia["Frecuencia Absoluta"] / tabla_frecuencia["Frecuencia Absoluta"].sum()
tabla_frecuencia["Frecuencia Acumulada"] = tabla_frecuencia["Frecuencia Absoluta"].cumsum()
tabla_frecuencia["Frecuencia Relativa Acumulada"] = tabla_frecuencia["Frecuencia Relativa"].cumsum()
print(f'{tabla_frecuencia} \n')

'''
3. Cálculo de Medidas de Tendencia Central 
● Calcular la media, mediana y moda de una variable cuantitativa.
'''
media = df['Ingresos'].mean()
mediana = df['Ingresos'].median()
moda = df['Ingresos'].mode()[0]

cadena_caracteres = f'media: {int(media)}'
print(cadena_caracteres)
print(f'media: {media:.2f}')
print(f'mediana" {mediana:.2f}')
print(f'moda: {moda:.2f}')

'''
4. Cálculo de Medidas de Dispersión 
● Calcular el rango, varianza y desviación estándar de la misma variable utilizada en el punto anterior.
'''
categoria = df['Ingresos']
rango = categoria.max() - categoria.min()
varianza = categoria.var()
desviacion_estandar = categoria.std()
print(f'rango: {rango}')
print(f'varianza: {varianza}')
print(f'desviacion estandar: {desviacion_estandar}')

'''
5. Visualización de Datos 
Crear un histograma para una variable cuantitativa y un boxplot para otra variable del dataset.
'''
