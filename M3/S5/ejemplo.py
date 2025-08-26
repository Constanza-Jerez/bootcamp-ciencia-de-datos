import pandas as pd

print("--- Sesión 5: Obtención y Preparación de Datos ---")
print("---------------------------------------------------\n") # Título de la sesión

# --- 1. Indexación Jerárquica (MultiIndex) ---
print("### 1. Indexación Jerárquica: Organizando Datos Multinivel ###")
print("La indexación jerárquica (MultiIndex) permite tener múltiples niveles de índices en un DataFrame, facilitando la organización y manipulación de datos con estructura multinivel o multidimensional.")
print("Sus ventajas incluyen un acceso más fácil a subconjuntos de datos específicos y la capacidad de realizar operaciones complejas de manera más intuitiva, especialmente con datos que tienen relaciones jerárquicas naturales.")

# DataFrame Original
print("\nDataFrame Original:")
data = {
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona'],
    'Año': [2020, 2021, 2020, 2021],
    'Ventas': [100, 150, 200, 250]
}
df = pd.DataFrame(data)
print(df)

# Creación de MultiIndex
print("\nTransformación: Estableciendo el índice jerárquico con .set_index(['Ciudad', 'Año'], inplace=True)")
df.set_index(['Ciudad', 'Año'], inplace=True)
print(df)

# Acceso a Datos con MultiIndex
print("\nAcceso a Datos: Accediendo a las ventas de Barcelona en 2021 usando df.loc[('Barcelona', 2021), :]")
print(df.loc[('Barcelona', 2021), :])

# Otros métodos útiles con MultiIndex
print("\nOtros métodos útiles con MultiIndex:")

# swaplevel()
print("\nswaplevel(): Permite intercambiar los niveles del índice.")
df_swapped = df.swaplevel()
print(df_swapped)

# stack()
print("\nstack(): Convierte columnas en niveles del índice (útil para transformar datos).")
# Para ilustrar stack, agregamos otra columna
df2 = df.copy()
df2['Costos'] = [60, 90, 120, 140]
print("DataFrame con columna extra:")
print(df2)
df_stacked = df2.stack()
print("Resultado de df2.stack():")
print(df_stacked)

# unstack()
print("\nunstack(): Convierte un nivel del índice en columnas (inverso de stack).")
df_unstacked = df2.unstack()
print("Resultado de df2.unstack():")
print(df_unstacked)

print("\n---------------------------------------------------\n")
























# --- 2. Agrupamiento con GroupBy: Dividir-Aplicar-Combinar ---
print("### 2. Agrupamiento con GroupBy: Dividir-Aplicar-Combinar ###")
print("La función .groupby() es fundamental para el análisis de datos, siguiendo el paradigma 'Dividir-Aplicar-Combinar'.")
print("1. **Dividir**: La función .groupby() divide los datos en grupos según los valores de una o más columnas.")
print("2. **Aplicar**: Una vez divididos los datos, se aplican funciones de agregación como sum(), mean(), count(), max() o min() a cada grupo por separado.")
print("3. **Combinar**: Finalmente, los resultados de cada grupo se combinan en un nuevo DataFrame, proporcionando una vista resumida.")

# Restablecemos el DataFrame original para el ejemplo de groupby
df_original = pd.DataFrame(data)

# Agrupamiento Simple
print("\nEjemplos de Agrupamiento y Agregación:")
print("Agrupamiento Simple: df_original.groupby('Ciudad')['Ventas'].sum()")
df_grouped_sum = df_original.groupby('Ciudad')['Ventas'].sum()
print("Suma de ventas por ciudad:")
print(df_grouped_sum)

# Múltiples Funciones de Agregación
print("\nMúltiples Funciones: df_original.groupby('Ciudad')['Ventas'].agg(['sum', 'mean', 'count', 'max', 'min'])")
df_grouped_multi_agg = df_original.groupby('Ciudad')['Ventas'].agg(['sum', 'mean', 'count', 'max', 'min'])
print("Múltiples agregaciones de ventas por ciudad:")
print(df_grouped_multi_agg)

print("\n---------------------------------------------------\n")



















# --- 3. Pivoteo de DataFrames ---
print("### 3. Pivoteo de DataFrames ###")
print("El pivoteo transforma datos de formato largo (muchas filas) a formato ancho (más columnas) para facilitar análisis y visualizaciones.")

# DataFrame para pivoteo (usamos el original para el ejemplo)
print("\nDataFrame para Pivoteo:")
df_pivot_example = pd.DataFrame({
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona'],
    'Año': [2020, 2021, 2020, 2021],
    'Ventas': [100, 150, 200, 250]
})
print(df_pivot_example)
print("\nEjemplo de Pivoteo con pivot_table: df_pivot = df_pivot_example.pivot_table(values='Ventas', index='Ciudad', columns='Año', aggfunc='sum')")
df_pivot = df_pivot_example.pivot_table(values='Ventas', index='Ciudad', columns='Año', aggfunc='sum')
print(df_pivot)

print("\n---------------------------------------------------\n")

# --- 4. Despivoteo con Melt ---
print("### 4. Despivoteo con Melt: De Formato Ancho a Largo ###")
print("El despivoteo es la operación inversa al pivoteo, transformando datos de formato ancho (muchas columnas) a formato largo (más filas). Esto es útil para análisis estadísticos y visualizaciones específicas.")

# DataFrame en formato ancho para despivoteo
print("\nDataFrame en formato ancho para Despivoteo:")
df_melt_example = pd.DataFrame({
    'Ciudad': ['Madrid', 'Barcelona'],
    '2020': [100, 200],
    '2021': [150, 250]
})
print(df_melt_example)
df_melted = pd.melt(df_melt_example, id_vars=['Ciudad'], value_vars=['2020', '2021'], var_name='Año', value_name='Ventas')
print("Resultado de pd.melt:")
print(df_melted)

print("\n---------------------------------------------------\n")

















# --- 5. Concatenación de DataFrames ---
print("### 5. Concatenación de DataFrames ###")
print("La concatenación une DataFrames por filas o columnas, útil cuando los DataFrames tienen la misma estructura y se quieren combinar secuencialmente.")

# Crear dos DataFrames para concatenación
df1 = pd.DataFrame({'ID': [1, 2], 'Ventas': [100, 150]})
df2 = pd.DataFrame({'ID': [3, 4], 'Ventas': [200, 250]})
print("Concatenación vertical (por filas):")
df_concat_vertical = pd.concat([df1, df2], axis=0)
print(df_concat_vertical)

# Concatenación horizontal (unir columnas)
df3 = pd.DataFrame({'ID': [1, 2, 3], 'Descuento': [10, 20, 30]})
print("\nDataFrame para concatenación horizontal:")
print(df3)
print("Concatenación horizontal (por columnas):")
df_concat_horizontal = pd.concat([df1, df3], axis=1)
print(df_concat_horizontal)

print("\n---------------------------------------------------\n")

# --- 6. Merge de DataFrames: Uniones Tipo SQL ---
print("### 6. Merge de DataFrames: Uniones Tipo SQL ###")
print("La función pd.merge() permite combinar DataFrames basándose en una clave común, similar a una unión (JOIN) en SQL.")

# Tipos de Merge
print("Tipos de Merge disponibles:")
print("- **inner** (intersección): Solo valores comunes. (Por defecto si no se declara 'how')")
print("- **left** (izquierda): Conserva todos los valores del primer DataFrame y agrega los del segundo si hay coincidencia.")
print("- **right** (derecha): Conserva todos los valores del segundo DataFrame.")
print("- **outer** (unión): Conserva todos los valores de ambos DataFrames, rellenando con NaN si no hay coincidencia.")

# Ejemplo simple de merge
df_left = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Ana', 'Luis', 'Eva']})
df_right = pd.DataFrame({'ID': [2, 3, 4], 'Ciudad': ['Madrid', 'Barcelona', 'Valencia']})

print("\nDataFrames para merge:")
print("df_left:")
print(df_left)
print("df_right:")
print(df_right)

print("\nMerge inner (solo IDs comunes):")
print(pd.merge(df_left, df_right, on='ID', how='inner'))

print("\nMerge left (todos los de df_left):")
print(pd.merge(df_left, df_right, on='ID', how='left'))

print("\nMerge right (todos los de df_right):")
print(pd.merge(df_left, df_right, on='ID', how='right'))

print("\nMerge outer (todos):")
print(pd.merge(df_left, df_right, on='ID', how='outer'))

# Merge con múltiples claves y sufijos
print("\nMerge con múltiples claves y sufijos:")
df_ventas = pd.DataFrame({
    'id': [1, 2, 3],
    'fecha': ['2021-01', '2021-02', '2021-03'],
    'monto': [500, 600, 700]
})
df_costos = pd.DataFrame({
    'id': [1, 2, 3],
    'fecha': ['2021-01', '2021-02', '2021-03'],
    'monto': [300, 350, 400]
})
print("df_ventas:")
print(df_ventas)
print("df_costos:")
print(df_costos)
df_merged = pd.merge(df_ventas, df_costos, on=['id', 'fecha'], suffixes=('_venta', '_costo'))
print("Resultado del merge con múltiples claves y sufijos:")
print(df_merged)

print("\nLa elección entre concat() y merge() depende fundamentalmente de la estructura de tus datos y el tipo de combinación que necesites realizar.")
print("\n- **pd.concat()**: Usarlo para unir filas o columnas sin depender de claves comunes.")
print("  - Descripción: Une DataFrames por filas (axis=0) o columnas (axis=1). Si los DataFrames tienen la misma estructura y solo necesitas unirlos secuencialmente, concat() es la opción más directa.")
print("\n- **pd.merge()**: Usarlo para combinar datos con una clave común, como en SQL.")
print("  - Descripción: Combina DataFrames según una clave (inner, left, right, outer). Si necesitas combinar información relacionada basada en valores comunes entre diferentes conjuntos de datos, merge() ofrece la flexibilidad de las uniones tipo SQL.")