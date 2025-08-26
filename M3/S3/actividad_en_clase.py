"""
Requerimientos:
1. Cargar el archivo CSV en un DataFrame.
2. Mostrar las primeras 5 filas del archivo.
3. Extraer solo las columnas "Nombre", "Curso" y "Nota".
4. Filtrar los estudiantes con nota mayor o igual a 9.
5. Guardar el DataFrame filtrado en un nuevo archivo csv.
"""

from pathlib import Path
import pandas as pd

# 1. Cargar el archivo CSV en un DataFrame.
# ruta = 'M3/S3/archivo/estudiantes.csv'

base = Path(__file__).parent 
ruta = base / "archivo" / "estudiantes.csv"

df = pd.read_csv(ruta)
print(f'1. DataFrame cargado correctamente: \n{df}\n')
print('----------------------------------------------------------------------')

# 2. Mostrar las primeras 5 filas del archivo.

print(f'2. Primeras 5 filas: \n {df.head()} \n')
print('----------------------------------------------------------------------')

# 3. Extraer solo las columnas "Nombre", "Curso" y "Nota".

nombre_curso_nota = df[['Nombre', 'Curso', 'Nota']]
print(f'3. columnas "Nombre", "Curso" y "Nota": \n {nombre_curso_nota} \n')
print('----------------------------------------------------------------------')

# 4. Filtrar los estudiantes con nota mayor o igual a 9.

filtrado_nota = df[df['Nota'] >= 9]
print(f'4. Notas filtradas >= 9: \n {filtrado_nota} \n')
print('----------------------------------------------------------------------')

# 5. Guardar el DataFrame filtrado en un nuevo archivo CSV.
# dataFrame.to_csv(ruta)

filtrado_nota.to_csv('M3/S3/archivo/estudiantes_filtrados.csv', index=False )