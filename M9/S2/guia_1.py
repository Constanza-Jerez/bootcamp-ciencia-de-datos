from pyspark.sql import SparkSession
from pyspark.sql.functions import col
 
#crear sparksession
 
spark=SparkSession.builder.master('local').appName('AnalisisVentas').getOrCreate()
 
#verificar que las sesión de spark se ha creado correctamente
 
print('SparkSession creada correctamente')
 
#cargar datos desde archivo CSV

file_path= 'D:/BOOTCAMP 0065 - FUNDAMENTOS DATA SCIENCE/M9/S2/transacciones.csv'
df=spark.read.option('header', 'true').csv(file_path)
 
#ver df
df.show()
 
#filtrar ventas 'producto_id'
 
df_producto= df.filter(df['producto_id']== 'Productos')
df_producto = df_producto.withColumn('cantidad', col('cantidad').cast('int'))
 
#agrupar las ventas pro fecha y calcular la cantidad total de ventas
 
df_agrupado= df_producto.groupby('fecha').sum('cantidad')

#ver df
df_agrupado.show()
 