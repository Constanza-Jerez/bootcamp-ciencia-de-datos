  
# • Crear tres variables en Python:
# - Precio_producto, que almacene el precio de un producto, por ejemplo, 1200.
precio_producto = 1200
# - Cantidad, que almacene la cantidad comprada, por ejemplo, 3.
cantidad = 3
# - Descuento, que almacene un descuento en porcentaje, por ejemplo, 10.
descuento = 10

# • Calcular el precio total sin descuento:
# - Multiplica precio_producto por cantidad y guárdalo en una nueva variable llamada total_sin_descuento.
total_sin_descuento = precio_producto * cantidad

# • Calcular el monto de descuento:
# - Usa la variable descuento (recuerda que es en porcentaje) y guárdalo en una variable llamada monto_descuento.
monto_descuento = (total_sin_descuento * descuento) / 100

# •Calcular el precio total con descuento:
# - Resta monto_descuento de total_sin_descuento, y almacénalo en una variable llamada total_con_descuento.
total_con_descuento = total_sin_descuento - monto_descuento

# •Imprime los resultados de cada cálculo con mensajes claros:
# - “Total sin descuento: ...”
print(f'Total sin descuento: {total_sin_descuento}')
# - “Monto de descuento: …”
print(f'Monto de descuento: {monto_descuento}')
# - “Total con descuento: …”
print(f'Total con descuento: {total_con_descuento}')
