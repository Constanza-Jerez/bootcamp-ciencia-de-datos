'''
Imagina que eres parte del equipo de análisis de datos de una tienda en línea. El gerente te ha enviado un archivo CSV llamado ventas.csv, el cual contiene información sobre las ventas realizadas en la tienda. Sin embargo, debido a errores en el proceso de recolección de datos, el archivo tiene algunas inconsistencias y problemas que deben corregirse antes de que se pueda utilizar para el análisis.
Tu tarea será aplicar las técnicas que has visto para:
• Identificar y manejar valores perdidos.
• Detectar y eliminar valores duplicados.
• Filtrar y corregir outliers.
• Reemplazar valores incorrectos.
• Modificar la estructura del DataFrame.

REQUERIMIENTOS:
1. Cargar el archivo CSV y visualizar la información.
2. Identificar y manejar valores perdidos.
3. Detectar y eliminar registros duplicados.
4. Detectar y manejar outliers en la columna "Cantidad".
5. Reemplazar valores incorrectos y modificar la estructura del DataFrame..
'''
from pathlib import Path
# from lib_pandas import read_csv
import pandas as pd

def read_csv(file_name):
    '''función para lectura de csv con pandas'''
    path = Path(__file__).parent / file_name
    return pd.read_csv(path)

def println(text_init, value, text_end=''):
    print(f'{text_init}: \n {value} {text_end} \n')
    
def validate_null_fill_mode(data_frame, column, column_mode):
    if data_frame[column].isnull().any():
        data_frame[column] = data_frame[column].fillna(df_copy[column_mode].mode()[0])
        return data_frame    
    
# 1. Cargar el archivo CSV y visualizar la información.
df = read_csv('ventas.csv')
# df = pd.read_csv('ventas.csv')

print(f'Data frame ventas: \n {df} \n')
print(f'Info: \n {df.info()} \n')
print(f'Describe: \n {df.describe(include='all')} \n')
print(f'5 filas: \n {df.head()} \n')
print(f'tipo dato: \n {df.dtypes} \n')

# 2. Identificar y manejar valores perdidos.
valores_perdidos = df.isnull().sum()
print(f'valores_perdidos: \n {valores_perdidos} \n')

filas_valores_perdidos = df[df.isnull().any(axis=1)]
println('filas_valores_perdidos', filas_valores_perdidos)

# crear copia de data frame
df_copy = df.copy()

print(f'df_copy before fill: {df_copy}')

if df_copy['Precio'].isnull().any():
    df_copy['Precio'] = df_copy['Precio'].fillna(df_copy['Precio'].mode()[0], inplace=True)

println('df_copy after fill', df_copy)

# 3. Detectar y eliminar registros duplicados.
duplicados_completos = df_copy.duplicated()
println('duplicados_completos', duplicados_completos)
println('suma duplicados_completos', duplicados_completos.sum())

if duplicados_completos.any():
    println('duplicados_completos en df_copy', df_copy[duplicados_completos])
    
    df_no_duplicates = df_copy.drop_duplicates()

println('df_no_duplicates', df_no_duplicates)

# 4. Detectar y manejar outliers en la columna "Cantidad".
Q1 = df['Cantidad'].quantile(0.25)
Q3 = df['Cantidad'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
 
# Eliminar outliers
df_outliers = df[(df['Cantidad'] >= limite_inferior) & (df['Cantidad'] <= limite_superior)]
print(df_outliers)
print("4. Los outliers en la columna 'Cantidad' han sido eliminados usando IQR.")

# 5. Reemplazar valores incorrectos y modificar la estructura del DataFrame.
df['Método de Pago'] = df['Método de Pago'].str.strip().str.title()
print("5a. Los valores de la columna 'Método de Pago' han sido estandarizados y sin espacios adicionales.\n")
 
# Reordenar columnas (opcional)
df = df[['Cliente_ID', 'Nombre', 'Categoría', 'Fecha', 'Cantidad', 'Precio', 'Método de Pago']]
print("5b. Las columnas del DataFrame después de limpieza y transformación se han reordenado así:\n")
print(df.columns.tolist())