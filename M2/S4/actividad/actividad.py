'''
1. Crea una función calcular_area_rectangulo que reciba dos parámetros (largo y ancho) y retorne el área del rectángulo.
2. Crea una función calcular_circunferencia que reciba el radio de un círculo y retorne su circunferencia. Usa la constante pi del módulo math.
3. Crea una función calcular_promedio que reciba una lista de números y retorne el promedio.
4. Importa la función mean del módulo statistics y úsala en una nueva función calcular_promedio_avanzado para calcular el promedio de la misma lista de números del punto anterior.
5. Crea una función generar_numeros_aleatorios que reciba dos parámetros (cantidad y limite), y retorne una lista de números aleatorios entre 1 y el límite especificado. Usa el módulo random.
6. Escribe un programa que utilice cada una de las funciones anteriores e imprime los resultados de cada cálculo.
'''
import math
import statistics
import random

# calcular_area_rectangulo
# def nombre_funcion(parametros_entrada, separados_por_coma):
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho
    
# calcular_circunferencia
def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# calcular_promedio
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# calcular_promedio_avanzado
def calcular_promedio_avanzado(numeros):
    return statistics.mean(numeros)
    
# generar_numeros_aleatorios
def generar_numeros_aleatorios(cantidad, limite):
    return [random.randint(1, limite) for _ in range(cantidad)]

# iniciar el ciclo
while True: # mientras sea True el ciclo continuara infinito o hasta que suceda un break
    # impresion de menu
    print('1. calcular_area_rectangulo')
    print('2. calcular_circunferencia')
    print('3. calcular_promedio')
    print('4. calcular_promedio_avanzado')
    print('5. generar_numeros_aleatorios')
    print('6. Salir del menú')
    opcion = input('Ingrese una opción: ') # muestra mensaje y pide al usuario ingresar una opción en la terminal
    
    if opcion == '1': # opcion es igual a 1?
        print(f'area rentangulo {calcular_area_rectangulo(8,4)}')
    elif opcion == '2': 
        print(f' circunferencia {calcular_circunferencia(50)}')
    elif opcion == '3':
        print(f' promedio {calcular_promedio([8, 9, 4, 5])}')
    elif opcion == '4':
        print(f' promedio avanzado {calcular_promedio_avanzado([8, 9, 4, 5])}')
    elif opcion == '5':
        print(f' numeros aleatorios{generar_numeros_aleatorios(5, 10)}')
    elif opcion == '6':
        break
    else:
        print('Ha ingresado una opción invalida, por favor ingrese una opción')