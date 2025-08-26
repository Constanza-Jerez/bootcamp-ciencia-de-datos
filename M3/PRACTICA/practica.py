'''
1. Limpieza y Transformación de Datos
• Carga el dataset en un DataFrame de Pandas.
• Identifica y trata valores perdidos en el dataset.
• Detecta y filtra outliers usando el método del rango intercuartílico (IQR).
• Reemplaza los valores de la columna "Razon_Migracion" usando mapeo de valores (ejemplo: "Económica" → "Trabajo", "Conflicto" → "Guerra").
2. Análisis Exploratorio
• Muestra las 5 primeras filas del dataset.
• Obtén información general del dataset con .info() y .describe().
• Calcula estadísticas clave:
o Media y mediana de la cantidad de migrantes.
o PIB promedio de los países de origen y destino: Usa .value_counts() para contar cuántos movimientos de migración ocurrieron por cada razón.

3. Agrupamiento y Sumarización de Datos
• Agrupa los datos por "Razon_Migracion" y calcula la suma total de migrantes para cada categoría.
• Obtén la media del IDH de los países de origen por cada tipo de migración.
• Ordena el DataFrame de mayor a menor cantidad de migrantes.
4. Filtros y Selección de Datos
• Filtra y muestra solo las migraciones por conflicto.
• Selecciona y muestra las filas donde el IDH del país de destino sea mayor a 0.90.
• Crea una nueva columna "Diferencia_IDH" que calcule la diferencia de IDH entre país de origen y destino.
5. Exportación de Dato
• Guarda el DataFrame final en un nuevo archivo CSV llamado "Migracion_Limpio.csv", sin el índice..
'''
import pandas as pd
from pathlib import Path

'''1. Limpieza y Transformación de Datos
• Carga el dataset en un DataFrame de Pandas.
• Identifica y trata valores perdidos en el dataset.
• Detecta y filtra outliers usando el método del rango intercuartílico (IQR).
• Reemplaza los valores de la columna "Razon_Migracion" usando mapeo de valores (ejemplo: "Económica" → "Trabajo", "Conflicto" → "Guerra").'''
path = Path(__file__).parent / 'migracion.csv'
df = pd.read_csv(path)
print(f'df: \n {df} \n')

# Identifica y trata valores perdidos en el dataset.
print(f'valores perdidos: \n {df.isnull().sum()} \n')
# para este ejemplo no hay valores perdidos, pero si existen usar dropna o fillna

# Detecta y filtra outliers usando el método del rango intercuartílico (IQR)
Q1 = df['Cantidad_Migrantes'].quantile(0.25)
Q3 = df['Cantidad_Migrantes'].quantile(0.75)
IQR = Q3 - Q1 # calculo IQR

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_sin_outliers = df[(df['Cantidad_Migrantes'] >= limite_inferior) & (df['Cantidad_Migrantes'] <= limite_superior)]
df_outliers = df[(df['Cantidad_Migrantes'] <= limite_inferior) & (df['Cantidad_Migrantes'] >= limite_superior)]

print(f'limite_inferior: \n {limite_inferior} \n')
print(f'limite_superior: \n {limite_superior} \n')
print(f'IQR: \n {IQR} \n')
print(f'df_sin_outliers: \n {df_sin_outliers} \n')
print(f'df_outliers: \n {df_outliers} \n')

# Reemplaza los valores de la columna "Razon_Migracion" usando mapeo de valores (ejemplo: "Económica" → "Trabajo", "Conflicto" → "Guerra").
mapa_razon = {'Económica': 'Trabajo', 'Conflicto': 'Guerra', 'Educativa': 'Estudios'}
df['Razon_Migracion'] = df['Razon_Migracion'].replace(mapa_razon)
print(f'df: \n {df} \n')

'''2. Análisis Exploratorio
• Muestra las 5 primeras filas del dataset.
• Obtén información general del dataset con .info() y .describe().
• Calcula estadísticas clave:
o Media y mediana de la cantidad de migrantes.
o PIB promedio de los países de origen y destino: Usa .value_counts() para contar cuántos movimientos de migración ocurrieron por cada razón.'''
print(f'cabecera: \n {df.head(5)} \n')
print(f'info: \n {df.info()} \n')
print(f'describe: \n {df.describe()} \n')

print("Estadísticas descriptivas:\n")
estadisticas = df.describe().round(2) # Redondear a 2 decimales
 
# Renombrar las filas al español
estadisticas.rename(index={
    'count': 'conteo',
    'mean': 'media',
    'std': 'desviación estándar',
    'min': 'mínimo',
    '25%': 'percentil 25',
    '50%': 'mediana (percentil 50)',
    '75%': 'percentil 75',
    'max': 'máximo'
}, inplace=True)
 
print(estadisticas)

# Media y mediana de la cantidad de migrantes.
print(f'Media migrantes: {df['Cantidad_Migrantes'].mean()}')
print(f'Mediana migrantes: {df['Cantidad_Migrantes'].median()}')

# PIB promedio de los países de origen y destino: Usa .value_counts() para contar cuántos movimientos de migración ocurrieron por cada razón.
print(f'Media PIB origen: \n {df['PIB_Origen'].mean()} \n')
print(f'Media PIB destino: \n {df['PIB_Destino'].mean()} \n')
print(f'Movimientos de migracion por razon: \n {df['Razon_Migracion'].value_counts()} \n')

'''3. Agrupamiento y Sumarización de Datos
• Agrupa los datos por "Razon_Migracion" y calcula la suma total de migrantes para cada categoría.
• Obtén la media del IDH de los países de origen por cada tipo de migración.
• Ordena el DataFrame de mayor a menor cantidad de migrantes.'''
# Agrupa los datos por "Razon_Migracion" y calcula la suma total de migrantes para cada categoría.
print(f'suma total migrantes: \n{df.groupby('Razon_Migracion')['Cantidad_Migrantes'].sum()}\n')
print(f'Media IDH por razon migracion: \n{df.groupby('Razon_Migracion')['IDH_Origen'].mean()}\n')
 
df_ordenado = df.sort_values('Cantidad_Migrantes', ascending=False)

'''4. Filtros y Selección de Datos
• Filtra y muestra solo las migraciones por conflicto.
• Selecciona y muestra las filas donde el IDH del país de destino sea mayor a 0.90.
• Crea una nueva columna "Diferencia_IDH" que calcule la diferencia de IDH entre país de origen y destino.'''

# df[df[columna] condicion filtro]

'''5. Exportación de Dato
• Guarda el DataFrame final en un nuevo archivo CSV llamado "Migracion_Limpio.csv", sin el índice.'''