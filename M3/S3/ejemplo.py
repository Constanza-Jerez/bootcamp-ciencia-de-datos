import pandas as pd

# lectura csv

pd.read_csv('ruta/archivo', sep=',', na_values=['NA', 'NULL'])

# lectura excel
'''
Archivos Excel en Pandas

Leyendo un archivo Excel

Parámetros Comunes de read_excel()
sheet_name="Hoja1": Especifica la hoja a leer (por defecto es la primera).
index_col=0: Define que columna se usara como índice del DataFrame.
usecols=["Nombre", "Edad"]: Permite seleccionar solo ciertas columnas.

Ejemplo con parámetros personalizados:

df = pd.read_excel("datos.xlsx", sheet_name="Ventas", usecols=["Cliente", "Total"], index_col="Cliente")
'''
df = pd.read_excel("datos.xlsx", sheet_name="Ventas", usecols=["Cliente", "Total"], index_col="Cliente")

# escritura excel
'''
Archivos Excel en Pandas

Escribiendo un archivo Excel:

Para exportar datos de Pandas a Excel, se usa to_excel().

Ejemplo básico de escritura en Excel:

df.to_excel("nuevo_archivo.xlsx", index=False)
'''
df.to_excel("nuevo_archivo.xlsx", index=False)

'''
Archivos Excel en Pandas

Escribiendo un archivo Excel:

Opciones útiles en to_excel():
sheet_name="Resultados": Define el nombre de la hoja donde se guardarán los datos.
na_rep="Sin datos": Define cómo se guardarán los valores nulos.

Ejemplo con parámetros personalizados

.

df.to_excel("resultados.xlsx", sheet_name="Datos Analizados", index=False, na_rep="Sin datos")
'''
df.to_excel("resultados.xlsx", sheet_name="Datos Analizados", index=False, na_rep="Sin datos")

