# Big Data: Comercio Electrónico
# ---------------------------------------------------
# 1. Generación y almacenamiento de datos (simulación)

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Simular datos de transacciones
def generar_datos_transacciones():
    np.random.seed(42)
    clientes = [f"C{str(i).zfill(4)}" for i in range(1, 1001)]
    productos = [f"P{str(i).zfill(3)}" for i in range(1, 51)]
    fechas = [datetime.now() - timedelta(days=np.random.randint(0, 30)) for _ in range(10000)]
    datos = {
        'cliente_id': np.random.choice(clientes, 10000),
        'producto_id': np.random.choice(productos, 10000),
        'fecha': fechas,
        'cantidad': np.random.randint(1, 5, 10000),
        'precio_unitario': np.random.uniform(10, 100, 10000)
    }
    df = pd.DataFrame(datos)
    df['total'] = df['cantidad'] * df['precio_unitario']
    df.to_csv('transacciones.csv', index=False)
    print('Archivo transacciones.csv generado.')

# 2. Ingesta y procesamiento distribuido (PySpark)
def procesamiento_spark():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, sum as spark_sum

    spark = SparkSession.builder.appName("EcommerceBigData").getOrCreate()
    transacciones = spark.read.csv('transacciones.csv', header=True, inferSchema=True)

    # Calcular el total de ventas por producto
    ventas_producto = transacciones.groupBy('producto_id').agg(spark_sum('total').alias('ventas_totales'))
    ventas_producto.orderBy(col('ventas_totales').desc()).show(5)

    # Recomendar productos populares a un cliente
    cliente = 'C0001'
    productos_populares = ventas_producto.orderBy(col('ventas_totales').desc()).limit(3)
    print(f"Recomendaciones para {cliente}:")
    productos_populares.show()

    # Guardar resultados para análisis local
    ventas_producto.toPandas().to_csv('ventas_producto.csv', index=False)
    print('Archivo ventas_producto.csv generado.')

# 3. Visualización y análisis final (Python local)
def visualizar_resultados():
    import matplotlib.pyplot as plt
    ventas = pd.read_csv('ventas_producto.csv')
    plt.bar(ventas['producto_id'], ventas['ventas_totales'])
    plt.xlabel('Producto')
    plt.ylabel('Ventas Totales')
    plt.title('Ventas por Producto')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Paso 1: Generar datos
    generar_datos_transacciones()
    # Paso 2: Procesar con Spark (descomenta si tienes PySpark instalado)
    procesamiento_spark()
    # Paso 3: Visualizar resultados (descomenta después de ejecutar Spark)
    visualizar_resultados()

# Nota: Para ejecutar el paso 2 necesitas tener PySpark instalado y configurado.
# El paso 3 requiere que el archivo ventas_producto.csv haya sido generado por Spark.
