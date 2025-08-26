'''
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay entre un número y uno. 
Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
'''
# def calcular_factorial_recursivo(n):
#     if n == 0 or n == 1:
#         return 1, "1"
#     sub_factorial, cadena = calcular_factorial_recursivo(n - 1)
#     return n * sub_factorial, f"{n} * {cadena}"
 
# def formatear_espanol(numero):
    # if isinstance(numero, int):
#         return f"{numero:,}".replace(",", ".")
#     elif isinstance(numero, float):
#         entero, decimal = f"{numero:,.2f}".split(".")
#         entero = entero.replace(",", ".")
#         return f"{entero},{decimal}"
#     return str(numero)
 
# def main():
#     try:
#         entrada = input("Ingresa un número entero o decimal no negativo: ").replace(",", ".")
#         numero = float(entrada)
#         if numero < 0 or not numero.is_integer():
#             print("Error: solo se aceptan números enteros no negativos.")
#         else:
#             numero = int(numero)
#             resultado, cadena = calcular_factorial_recursivo(numero)
#             resultado_formateado = formatear_espanol(resultado)
#             print(f"Factorial de {numero}: {cadena} = {resultado_formateado}")
#     except ValueError:
#         print("Error: debes ingresar un número válido.")
 
# if __name__ == "__main__":
#     main()

'''--------------------------------------------------------------------------------------------------------------'''

while True:
    num = int(input('Ingrese el numero'))
    if num > 0:
        break


# Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
factorial = 1
i = 1
while True:
    factorial *= i # factorial = fatorial * i
    i += 1
    if i > num:
        break
    
print(f'Fatorial del {num} es: {factorial}')   

'''--------------------------------------------------------------------------------------------------------------''' 

# factorial con libreria math
# import math  # importar libreria

# factorial = math.factorial(50)
# print(f'El factorial es: {factorial}')