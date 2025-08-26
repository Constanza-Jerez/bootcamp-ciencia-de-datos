# Sesión 4: Obtención y Preparación de Datos
# ejemplos de código basados en la presentación
# "PRESENTACION SESION 4m3.pdf" para la Sesión 4.

import pandas as pd
import numpy as np

# --- 1. ¿Qué es un Valor Perdido? ---
# Un valor perdido son datos ausentes en un conjunto de datos.
# En Pandas, se representan con NaN (Not a Number).
# Causas comunes incluyen errores en la recolección, registros incompletos,
# conversión de formatos y eliminación accidental de valores.

# Creación de un DataFrame de ejemplo con valores perdidos para demostración
df_missing_values = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis", None],
    "Edad": [25, 30, None, 40]
})
print(df_missing_values)

# Identificación de Valores Perdidos
# isnull(): Identifica valores nulos (True si es nulo)
df_missing_values.isnull() # Muestra un DataFrame con True donde hay valores nulos

# notnull(): Identifica valores no nulos (True si NO es nulo)
df_missing_values.notnull()

# sum(): Cuenta la cantidad de valores nulos por columna
df_missing_values.isnull().sum() # Cuenta los valores nulos por columna

# Tratamiento de Valores Perdidos - Eliminación (dropna())
# Si los valores perdidos son pocos y no afectan el análisis, se pueden eliminar.

# Eliminar todas las filas con al menos un NaN (axis=0 por defecto, how="any" por defecto)
df_limpio = df_missing_values.dropna()

# Eliminar columnas con NaN (axis=1)
df_sin_columnas_nulas = df_missing_values.dropna(axis=1)

# Consideraciones adicionales para dropna():
# axis=0: Elimina filas (por defecto).
# axis=1: Elimina columnas.
# how="any": Elimina si hay al menos un NaN en la fila/columna (por defecto).
# how="all": Solo elimina si todas las celdas de la fila/columna son NaN.

# Tratamiento de Valores Perdidos - Imputación de Datos (fillna())
# En lugar de eliminar, podemos reemplazar los valores perdidos.

# Re-crear el DataFrame original para demostrar fillna
df_imputation = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis", None, "Sofía"],
    "Edad": [25, 30, None, 40, 28]
})

def change_empty_text(data_frame, columna, text_remplazo):
    data_frame[columna].fillna(text_remplazo, inplace=True)

# Rellenar con la media para datos numéricos
# Se usa inplace=True para modificar el DataFrame original directamente
df_imputation["Edad"].fillna(df_imputation["Edad"].mean(), inplace=True)

# Rellenar valores de texto (ej., "Desconocido")
df_imputation["Nombre"].fillna("Desconocido", inplace=True)

# Imputación de Valores Cualitativos (usando la moda)
df_categorical_imputation = pd.DataFrame({"Categoría": ["A", "B", "A", None, "C", "A"]})
df_categorical_imputation["Categoría"].fillna(df_categorical_imputation["Categoría"].mode(), inplace=True)

# --- 2. Detección y Filtrado de Outliers (Valores Atípicos) ---
# Un outlier es un valor que se encuentra fuera del rango esperado,
# determinado por el rango intercuartílico (IQR).

# Cálculo del IQR: IQR = Q3 - Q1
# Un dato es outlier si está fuera de Q1 - 1.5 * IQR o Q3 + 1.5 * IQR.

# ¿Qué son los Cuartiles?
# Los cuartiles dividen un conjunto de datos ordenados en cuatro partes iguales.
# Q1 (Primer cuartil): El 25% de los datos está por debajo (percentil 25).
# Q2 (Segundo cuartil): La mediana, 50% de los datos por debajo.
# Q3 (Tercer cuartil): El 75% de los datos está por debajo (percentil 75).

# Ejemplo en Python para detectar y filtrar outliers
df_outliers = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis", "María", "Juan", "Pedro", "Sofía", "Jorge"],
    "Edad": [25, 30, 22, 10, 80, 35, 150, 28]  # Incluyendo posibles outliers: 10, 80, 150
})

Q1 = df_outliers["Edad"].quantile(0.25) # Primer cuartil
Q3 = df_outliers["Edad"].quantile(0.75) # Tercer cuartil
IQR = Q3 - Q1 # Cálculo del IQR

# Definición de los límites para outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrar los datos dentro del rango permitido (excluyendo outliers)
df_filtrado_outliers = df_outliers[
    (df_outliers["Edad"] >= lower_bound) &
    (df_outliers["Edad"] <= upper_bound)
]

print(f'df_filtrado_outliers: {df_filtrado_outliers}')

# --- 3. ¿Qué es el Data Wrangling? ---
# El Data Wrangling es el proceso de transformar, limpiar y estructurar datos
# en un formato adecuado para el análisis.
# Principales tareas: Limpieza de datos (faltantes, duplicados, errores),
# Transformación de datos (cambio de formatos, nuevas variables)
# e Integración de datos (combinar fuentes).

# Creación de un DataFrame más grande para ejemplos de manipulación
df_manipulation = pd.DataFrame({
    "ID": range(1, 11),
    "Nombre": ["Ana", "Carlos", "Luis", "Maria", "Juan", "Pedro", "Sofía", "Jorge", "Laura", "Miguel"],
    "Edad": [25, 30, 22, 28, 35, 40, 27, 33, 29, 31],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Sevilla", "Barcelona", "Madrid", "Bilbao", "Valencia", "Sevilla"],
    "Puntuacion": [90, 85, 88, 92, 75, 80, 95, 78, 84, 89]
})

# Muestreo Aleatorio (sample())
df_muestra = df_manipulation.sample(n=5) # Selecciona 5 registros aleatorios
print(f'df_muestra: {df_muestra}')

# Permutación de la Data (np.random.permutation())
df_permutado = df_manipulation.iloc[np.random.permutation(len(df_manipulation))]
print(f'df_permutado: {df_permutado}')

# Ordenamiento (sort_values())
df_ordenado = df_manipulation.sort_values(by="Edad", ascending=False) # Ordena por 'Edad' descendente

# Detección y Eliminación de Duplicados
df_duplicates_example = pd.DataFrame({
    'A': [1, 2, 2, 3, 1],
    'B': [10, 20, 20, 30, 10],
    'C': ['X', 'Y', 'Y', 'Z', 'X']
})

# Identificación de duplicados (duplicated())
df_duplicates_example.duplicated()

# Eliminación de duplicados (drop_duplicates())
df_sin_duplicados = df_duplicates_example.drop_duplicates()

# Reemplazo de Valores (replace())
df_replace_example = pd.DataFrame({"Categoría": ["M", "F", "M", "F", "M", "X"]})


# Reemplazar valores específicos
df_replace_example["Categoría"] = df_replace_example["Categoría"].replace({"M": "Masculino", "F": "Femenino"})

# Reemplazar múltiples valores con un valor único (ej. NaN)
df_multi_replace_example = pd.DataFrame({"Estado": ["Activo", "Desconocido", "Inactivo", "N/A", "Activo"]})
df_multi_replace_example.replace(["Desconocido", "N/A"], np.nan, inplace=True)

# Discretización y Binning (pd.cut())
# Transforma variables continuas en discretas (intervalos).
# Sintaxis básica: pd.cut(x, bins, labels=False, include_lowest=False)

df_binning_example = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis", "Maria", "Juan", "Pedro"],
    "Edad": [18, 25, 35, 45, 60, 75]
})

# Agrupar valores numéricos en intervalos
df_binning_example["Rango_Edad"] = pd.cut(
    df_binning_example["Edad"],
    bins=[0, 20, 30, 50, 100], # Intervalos de edad
    labels=["Joven", "Adulto Joven", "Adulto", "Mayor"] # Etiquetas para los intervalos
)

print(f'df_binning_example: \n {df_binning_example} \n')

# Aplicación de Funciones y Expresiones Lambda (apply())
# apply(): Aplica funciones a los datos de forma eficiente.
# Expresiones lambda: Funciones anónimas para operaciones rápidas.

df_apply_example = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [25, 30, 22]
})

# Aplicar una función para calcular la edad en 10 años (usando lambda)
def sum_value(df, column, value):
    return df[column].apply(lambda temp: temp + value)

def upper_value(df, column):
    return df[column].apply(lambda temp: temp.upper())

df_apply_example["Edad_Futura"] = df_apply_example["Edad"].apply(lambda x: x + 10)

# Convertir nombres a mayúsculas (usando lambda)
df_apply_example["Nombre_Mayus"] = df_apply_example["Nombre"].apply(lambda x: x.upper())

# Manipulación de DataFrames - Agregar, Eliminar y Redimensionar Columnas 

# Re-inicializar un DataFrame simple para estos ejemplos
df_column_manipulation = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [25, 30, 22]
})

# Agregar Columnas: df['Nueva'] = valores 
df_column_manipulation["Salario"] = [2000, 2500, 1800]

# Eliminar Columnas: df.drop(columns=['Columna']) 
df_column_manipulation = df_column_manipulation.drop(columns=["Salario"])

# Redimensión: melt() 
# Útil para transformar DataFrames de formato "ancho" a "largo".
df_melt_example = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [25, 30, 22],
    "Edad_Futura": [35, 40, 32]
})

df_melted_result = df_melt_example.melt(
    id_vars=["Nombre"],
    value_vars=["Edad", "Edad_Futura"],
    var_name="Tipo_Edad", # Nombre de la nueva columna para las variables
    value_name="Valor"   # Nombre de la nueva columna para los valores
)

print(f'df_melted_result: \n {df_melted_result} \n')

# Renombrar y Redefinir Índices 

df_index_rename = pd.DataFrame({
    "Nombre": ["Ana", "Carlos", "Luis"],
    "Edad": [25, 30, 65],
    "Categoria_Edad": ["Joven", "Adulto", "Mayor"]
})

# set_index(): Define un índice 
df_indexed = df_index_rename.set_index("Nombre") # Usar "Nombre" como índice 

# reset_index(): Restablece el índice original 
df_reset = df_indexed.reset_index() # Volver al índice original 

# rename(): Cambia nombres de columnas 
df_renamed = df_index_rename.rename(columns={"Edad": "Años", "Categoria_Edad": "Grupo_Etario"})