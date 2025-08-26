<<<<<<< HEAD
'''
Ejercicio: Análisis de Temperaturas Mensuales
Enunciado: Una estación meteorológica ha registrado las temperaturas promedio mensuales (en °C) de una ciudad durante un año. Realiza las siguientes operaciones:

Crear un array con las temperaturas: [15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17]
Calcular la temperatura promedio anual
Encontrar la temperatura máxima y mínima del año
Convertir todas las temperaturas de Celsius a Fahrenheit (F = C × 9/5 + 32)
Contar cuántos meses tuvieron temperatura superior a 25°C
Crear una matriz 4x3 reorganizando las temperaturas cuatrimestre
'''
import numpy as np # importar libreria numpy asignando alias np

# Crear un array con las temperaturas: [15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17]
temperaturas_celsius = np.array([15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17])
print(f'temperaturas_celsiuis: {temperaturas_celsius}')

# Calcular la temperatura promedio anual
promedio_anual = np.mean(temperaturas_celsius)
print(f'promedio_anual: {promedio_anual}')

# Encontrar la temperatura máxima y mínima del año
temp_max = np.max(temperaturas_celsius)
temp_min = np.min(temperaturas_celsius)

print(f'temperatura máxima: {temp_max}')
print(f'temperatura minima: {temp_min}')

# valor del mes max y min
        # indice + 1
mes_max = np.argmax(temperaturas_celsius) + 1 # [15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17]
mes_min = np.argmin(temperaturas_celsius) + 1 # [15, 18, 22, 28, 32, 35, 38, 37, 33, 27, 21, 17]
print(f'mes_max: {mes_max}') # 7
print(f'mes_min: {mes_min}') # 1

# Convertir todas las temperaturas de Celsius a Fahrenheit (F = C × 9/5 + 32)
temperaturas_fahrenheit = temperaturas_celsius * 9/5 + 32
print(f'temperaturas_celsius: {temperaturas_celsius}')
print(f'temperaturas_fahrenheit: {temperaturas_fahrenheit}')

# Contar cuántos meses tuvieron temperatura superior a 25°C
meses_calidos = np.sum(temperaturas_celsius > 25)
print(f'meses_calidos: {meses_calidos}')

temp_meses_calidos = temperaturas_celsius[temperaturas_celsius > 25]
print(f'temp_meses_calidos: {temp_meses_calidos}')

=======
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
>>>>>>> 69ae7667ac6b4bde6a7ba9f3d5a5cb92e2443b41
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
<<<<<<< HEAD

trimestres = ["T1 (ene-mar)", "T2 (abr-jun)", "T3 (jul-sep)", "T4 (oct-dic)"]
# promedio por trimestre
for i in range(len(matriz_trimestres)):
    promedio_trimestre = np.mean(matriz_trimestres[i])
    print(f'{trimestres[i]} promedio: {promedio_trimestre:.2f}')
   
# promedio por trimestre    
for i in range(4):
    print(f"{trimestres[i]}: {matriz_trimestres[i]}")    
=======
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

>>>>>>> 69ae7667ac6b4bde6a7ba9f3d5a5cb92e2443b41
