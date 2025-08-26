'''
Enunciado:
Una universidad ha registrado información de sus estudiantes en el archivo estudiantes.csv. Cada fila representa un registro con las siguientes columnas:
ID_Registro, Fecha, Nombre, Edad, Genero, Curso, Nota, Asistencia, Campus

Requerimientos:
1. Cargar el archivo CSV en un DataFrame.
2. Mostrar las primeras 5 filas del archivo.
3. Extraer solo las columnas "Nombre", "Curso" y "Nota".
4. Filtrar los estudiantes con nota mayor o igual a 9.
5. Guardar el DataFrame filtrado en un nuevo archivo CSV.
'''
from pathlib import Path
import pandas as pd

# ruta = 'M3/S3/ejercicio/estudiantes.csv'
ruta = Path(__file__).parent / 'estudiantes.csv'

df = pd.read_csv(ruta)
print(f'1. DataFrame cargado correctamente: \n {df} \n')

# 2. Mostrar las primeras 5 filas del archivo.
print(f'2. Primeras 5 filas: \n {df.head()} \n')

# 3. Extraer solo las columnas "Nombre", "Curso" y "Nota".
nombre_curso_nota = df[['Nombre', 'Curso', 'Nota']]
print(f'3. columnas "Nombre", "Curso" y "Nota": \n {nombre_curso_nota} \n')

# 4. Filtrar los estudiantes con nota mayor o igual a 9.
filtrado_nota = df[df['Nota'] >= 9]
print(f'4. Notas filtradas >= 9: \n {filtrado_nota} \n')

# 5. Guardar el DataFrame filtrado en un nuevo archivo CSV.
# dataFrame.to_csv(ruta)
                    # /M3/S3/ejercicio/estudiantes_filtrados.csv
filtrado_nota.to_csv('../../../estudiantes_filtrados.csv', index=False)