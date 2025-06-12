
# Ejercicio: Análisis de Ventas de una Tienda Online
# Enunciado: Una tienda online quiere analizar las ventas de sus productos durante el último trimestre. Como analista de datos, debes crear un reporte completo usando Pandas con la siguiente información de ventas:

# Datos de ventas:

# Producto: Laptop, Smartphone, Tablet, Auriculares, Mouse
# Categoría: Computadoras, Teléfonos, Computadoras, Accesorios, Accesorios
# Precio: 1200, 800, 600, 150, 25
# Unidades_Vendidas: 45, 120, 80, 200, 300
# Mes: Octubre, Noviembre, Octubre, Diciembre, Noviembre

# Tareas a realizar:
# Crear el DataFrame con los datos de ventas
# Mostrar solo los nombres de productos y sus precios
# Filtrar productos con ventas superiores a 100 unidades
# Calcular una columna "Ingresos_Total" (Precio × Unidades_Vendidas)
# Encontrar el producto con mayor y menor ingreso total
# Calcular el promedio de unidades vendidas
# Contar cuántos productos hay por categoría
# Ordenar por ingresos totales de mayor a menor
# Obtener estadísticas descriptivas del DataFrame
# Analizar las ventas por mes

import pandas as pd

# Crear el DataFrame con los datos de ventas
data_ventas = {
    'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Auriculares', 'Mouse'],
    'Categoría': ['Computadoras', 'Teléfonos', 'Computadoras', 'Accesorios', 'Accesorios'],
    'Precio': [1200, 800, 600, 150, 25],
    'Unidades_Vendidas': [45, 120, 80, 200, 300],
    'Mes': ['Octubre', 'Noviembre', 'Octubre', 'Diciembre', 'Noviembre']
}

df_ventas = pd.DataFrame(data_ventas)
print(f'data_frame ventas:')
print(df_ventas)

print('-----------------------------------------------------------')

# Mostrar solo los nombres de productos y sus precios
productos_precios = df_ventas[['Producto', 'Precio']]
print(f'productos_precios:')
print(productos_precios)

print('-----------------------------------------------------------')
# Filtrar productos con ventas superiores a 100 unidades
productos_venta_alta = df_ventas[df_ventas['Unidades_Vendidas'] > 100]
print(f'productos_venta_alta:')
print(productos_venta_alta)

print('-----------------------------------------------------------')
# Calcular una columna "Ingresos_Total" (Precio × Unidades_Vendidas)
df_ventas['Ingresos_Total'] = df_ventas['Precio'] * df_ventas['Unidades_Vendidas']
print(f'ingresos_total:')
print(df_ventas['Ingresos_Total']) 

print('-----------------------------------------------------------')
# Encontrar el producto con mayor y menor ingreso total
producto_max = df_ventas[df_ventas['Ingresos_Total'] == df_ventas['Ingresos_Total'].max()]
producto_min = df_ventas[df_ventas['Ingresos_Total'] == df_ventas['Ingresos_Total'].min()]
print('producto_max:')
print(producto_max)
print('producto_min:')
print(producto_min)

print('-----------------------------------------------------------')
# Calcular el promedio de unidades vendidas
promedio_unidades_vendidas = df_ventas['Unidades_Vendidas'].mean()
print('promedio_unidades_vendidas:')
print(promedio_unidades_vendidas)

print('-----------------------------------------------------------')
# Contar cuántos productos hay por categoría
producto_por_categoria = df_ventas['Categoría'].value_counts()
print('producto_por_categoria')
print(producto_por_categoria)

print('-----------------------------------------------------------')
# Ordenar por ingresos totales de mayor a menor
df_ventas_ordenado_descendent = df_ventas.sort_values('Ingresos_Total', ascending = False)
print(f'data_frame ventas descendente:')
print(df_ventas_ordenado_descendent)

# Obtener estadísticas descriptivas del DataFrame
data_descriptive = df_ventas.describe()
print(f'data descriptiva data_frame ventas:')
print(data_descriptive)

# Analizar las ventas por mes
data_analisis_venta_mes = df_ventas.groupby('Mes').agg({
    'Unidades_Vendidas': 'sum',
    'Ingresos_Total': 'sum'
})
print(f'data_analisis_venta_mes:')
print(data_analisis_venta_mes)