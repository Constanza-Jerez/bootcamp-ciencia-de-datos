# Ejemplo completo: Análisis de empleados
import pandas as pd

empleados_data = {
    'ID': range(1, 11),
    'Nombre': ['Ana García', 'Carlos López', 'María Rodríguez', 'Juan Pérez', 'Laura Martín',
               'Pedro Sánchez', 'Carmen Jiménez', 'Miguel Torres', 'Isabel Ruiz', 'Antonio Moreno'],
    'Departamento': ['IT', 'Marketing', 'IT', 'Ventas', 'Marketing', 
                    'IT', 'Ventas', 'IT', 'Marketing', 'Ventas'],
    'Salario': [45000, 38000, 52000, 35000, 41000, 48000, 36000, 55000, 39000, 42000],
    'Años_Exp': [3, 2, 5, 1, 3, 4, 2, 6, 2, 4],
    'Edad': [28, 25, 32, 24, 29, 31, 26, 35, 27, 33]
}

df_empleados = pd.DataFrame(empleados_data)

print("=== ANÁLISIS COMPLETO DE EMPLEADOS ===")
print("Primeras 5 filas:")
print(df_empleados.head())
'''
   ID           Nombre Departamento  Salario  Años_Exp  Edad
0   1       Ana García           IT    45000         3    28
1   2     Carlos López    Marketing    38000         2    25
2   3  María Rodríguez           IT    52000         5    32
3   4       Juan Pérez       Ventas    35000         1    24
4   5     Laura Martín    Marketing    41000         3    29
'''
print('------------------------------------------------------------------------------------------------')

print("Información general:")
df_empleados.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9

Data columns (total 6 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   ID            10 non-null     int64
 1   Nombre        10 non-null     object
 2   Departamento  10 non-null     object
 3   Salario       10 non-null     int64
 4   Años_Exp      10 non-null     int64
 5   Edad          10 non-null     int64
dtypes: int64(4), object(2)
memory usage: 612.0+ bytes
'''
print('------------------------------------------------------------------------------------------------')

print("Estadísticas por departamento:")
print(df_empleados.groupby('Departamento').agg({
    'Salario': ['mean', 'min', 'max'],
    'Años_Exp': 'mean',
    'Edad': 'mean'
}).round(2))
print('------------------------------------------------------------------------------------------------')
'''
               Salario               Años_Exp   Edad
               Salario               Años_Exp   Edad
                  mean    min    max     mean   mean
Departamento
Departamento
IT            50000.00  45000  55000     4.50  31.50
Marketing     39333.33  38000  41000     2.33  27.00
Ventas        37666.67  35000  42000     2.33  27.67
'''


print("Empleados con salario > 40000:")
print(df_empleados[df_empleados['Salario'] > 40000][['Nombre', 'Departamento', 'Salario']])
'''
Empleados con salario > 40000:
            Nombre Departamento  Salario
0       Ana García           IT    45000
2  María Rodríguez           IT    52000
4     Laura Martín    Marketing    41000
5    Pedro Sánchez           IT    48000
7    Miguel Torres           IT    55000
9   Antonio Moreno       Ventas    42000
'''