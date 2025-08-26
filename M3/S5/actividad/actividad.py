'''
REQUERIMIENTOS:
1. Crear un DataFrame con Indexación Jerárquica
• Crea un DataFrame que contenga las siguientes columnas: "Estudiante", "Materia", "Calificación".
• Utiliza los siguientes datos de ejemplo para crear el DataFrame:
Estudiante Materia Calificación 
Juan Matemáticas 6.5 
JuanHistoria 5.8 
María Matemáticas 4.2 
María Historia 6.0
2. Acceder a datos con Indexación Jerárquic
• Consulta la clasificación de María en Historia.
3. Agrupar y Agregar Datos con groupby
• Agrupa el DataFrame por "Materia" y calcula:
o El promedio de calificaciones por materia.
o La calificación más alta por materia.
4. Pivoteo de DataFrame

REQUERIMIENTOS:
1. Crear un DataFrame con Indexación Jerárquica
• Crea un DataFrame que contenga las siguientes columnas: "Estudiante", "Materia", "Calificación".
• Utiliza los siguientes datos de ejemplo para crear el DataFrame:
Estudiante Materia Calificación Juan Matemáticas 6.5 Juan
Historia
5.8 María Matemáticas 4.2 María
Historia
6.0
2. Acceder a datos con Indexación Jerárquic
• Consulta la clasificación de María en Historia.
3. Agrupar y Agregar Datos con groupby
• Agrupa el DataFrame por "Materia" y calcula:
o El promedio de calificaciones por materia.
o La calificación más alta por materia.
4. Pivoteo de DataFrame
Convierte el DataFrame para que:
o Las filas representen a los estudiantes.
o Las columnas representen las materias.
o Las celdas contengan sus calificaciones.
5. Despivoteo de DataFrame con melt (1 punto)
• Aplica la función melt para transformar el DataFrame pivoteado a su formato largo.
6. Concatenación y Merge de DataFrames (2 puntos)
• Crea dos DataFrames:
o df1 con las columnas "ID_Estudiante", "Estudiante", "Carrera"
o df2 con las columnas "ID_Estudiante", "Materia", "Calificación"
• Concatena ambos DataFrames a lo largo del eje de filas.
• Luego, realiza un merge de ambos DataFrames basado en la columna "ID_Estudiante".
'''

import pandas as pd # importacion de pandas
from pathlib import Path

data = {
    'Estudiante': ['Juan', 'Juan', 'María', 'María'],
    'Materia': ['Matemáticas', 'Historia', 'Matemáticas', 'Historia'],
    'Calificación': [6.5, 5.8, 4.2, 6.0]
}

# 1. Crear un DataFrame con Indexación Jerárquica
ruta = Path(__file__).parent / 'calificaciones_enriquecido.csv'
df = pd.read_csv(ruta) # leer el csv con pandas

print(f'dataframe: \n {df.head(10)} \n')

# se agrega multi index al data frame
multi_index_df = df.set_index(['Estudiante', 'Materia'])
print(f'multi_index_df: \n {multi_index_df.head(10)} \n')

# 2. Acceder a datos con Indexación Jerárquica
# • Consulta la clasificación de María en Historia.
calificacion_maria_df = multi_index_df.loc[('Maria', 'Historia'), 'Calificacion']
print(f'calificacion_maria_df : \n {calificacion_maria_df} \n')

# 3. Agrupar y Agregar Datos con groupby
# • Agrupa el DataFrame por "Materia" y calcula:
# o El promedio de calificaciones por materia.
# o La calificación más alta por materia.

df_agrupado_materia = df.groupby('Materia')['Calificacion']
print(f'df_agrupado_materia: \n {df_agrupado_materia.head(10)}\n')

promedio = df_agrupado_materia.mean()
max_calificacion = df_agrupado_materia.max()
print(f'promedio: \n {promedio} \n')
print(f'max_calificacion : \n {max_calificacion} \n')

df_grouped_multi_agg = df.groupby('Materia')['Calificacion'].agg(['mean', 'max'])
print(f'df_grouped_multi_agg: \n {df_grouped_multi_agg.head(10)} \n')

# 4. Pivoteo de DataFrame
# Convierte el DataFrame para que:
# o Las filas representen a los estudiantes.
# o Las columnas representen las materias.
# o Las celdas contengan sus calificaciones.
df_pivot = df.pivot_table(index='Estudiante', columns='Materia', values='Calificacion', aggfunc='mean')
print(f'df_pivot: \n {df_pivot.head(10)} \n')


# 5. Despivoteo de DataFrame con melt
# • Aplica la función melt para transformar el DataFrame pivoteado a su formato largo.
df_melt = df_pivot.reset_index().melt(id_vars='Estudiante', var_name='Materia', value_name='Calificacion')
print(f'df_melt: \n {df_melt.head(10)} \n')

# 6. Concatenación y Merge de DataFrames
# • Crea dos DataFrames:
# o df1 con las columnas "ID_Estudiante", "Estudiante", "Carrera"
# o df2 con las columnas "ID_Estudiante", "Materia", "Calificación"
# • Concatena ambos DataFrames a lo largo del eje de filas.
# • Luego, realiza un merge de ambos DataFrames basado en la columna "ID_Estudiante".
df1 = df[['ID_Estudiante', 'Estudiante', 'Carrera']].drop_duplicates()
df2 = df[['ID_Estudiante', 'Materia', 'Calificacion']]
print(f'df1: \n {df1} \n')
print(f'df2: \n {df2} \n')

concat_df = pd.concat([df1, df2], axis=0)
print(f'concat_df: \n {concat_df} \n')

merge_df = pd.merge(df1, df2, on='ID_Estudiante')
print(f'merge_df: \n {merge_df} \n')


