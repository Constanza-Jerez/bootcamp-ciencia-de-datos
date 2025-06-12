# Ejercicio: Análisis de Temperaturas Mensuales
# Enunciado: Una estación meteorológica ha registrado las temperaturas promedio mensuales (en °C) de una ciudad durante un año. Realiza las siguientes operaciones:

# 1. Crear un array con las temperaturas: [15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17]
# 2. Calcular la temperatura promedio anual
# 3. Encontrar la temperatura máxima y mínima del año
# 4. Convertir todas las temperaturas de Celsius a Fahrenheit (F = C × 9/5 + 32)
# 5. Contar cuántos meses tuvieron temperatura superior a 25°C
# 6. Crear una matriz 3x4 reorganizando las temperaturas por trimestres

#1.
import numpy as np

temperaturas = np.array([15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17])
print(temperaturas)

#2. 
temperatura_promedio = np.mean(temperaturas)
print(f'Promedio anual de temperatura: {temperatura_promedio}')

#3.
temperatura_max = np.max(temperaturas)
print(f'temperatura maxima: {temperatura_max}')

temperatura_min = np.min(temperaturas)
print(f'temperatura minima: {temperatura_min}')



#4.
temperatura_fahrenheit = (temperaturas * 9/5 + 32)
print(f'Temperatura de Celsius a Fahrenheit: {temperatura_fahrenheit}')

#5.
# Crea un array de booleanos (True donde la temperatura > 25)
mascara = temperaturas > 25

# Cuenta los True
num_meses_calidos = mascara.sum()
print(f'Número de meses con más de 25°C: {num_meses_calidos}')

#6.
# Crear una matriz 4x3 reorganizando las temperaturas por trimestres
# primer trimestre  (ene-mar)
# segundo trimestre (abr-jun)
# tercer trimestre  (jul-sep)
# cuarto trimestre  (oct-dic)

matriz_trimestres = temperaturas_celsius.reshape(4,3)
print(f'matriz_trimestres: {matriz_trimestres}')
'''
[[15 18 22]
 [28 32 35]
 [38 37 33]
 [27 21 17]]
'''
# promedio por trimestre
for i in range(len(matriz_trimestres)):
    if i == 0:
        trimestre = 'primer trimestre  (ene-mar)'
    elif i == 1:
        trimestre = 'segundo trimestre (abr-jun)'
    elif i == 2:
        trimestre = 'tercer trimestre  (jul-sep)'
    else:
        trimestre = 'cuarto trimestre  (oct-dic)'        
    
    promedio_trimestre = np.mean(matriz_trimestres[i])
    print(f'{trimestre} promedio: {promedio_trimestre:.2f}')

