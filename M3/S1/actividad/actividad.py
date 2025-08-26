# 1. Importar la librería NumPy.
import numpy as np

# 2. Crear un vector de 10 elementos con valores del 1 al 10 utilizando arange.
# •Muestra el vector generado.
vector_original = np.arange(1,11)
print(f'vector_original: {vector_original}') # [ 1  2  3  4  5  6  7  8  9 10]

# 3. Generar una matriz de 3x3 con valores aleatorios entre 0 y 1 usando random.rand.
# • Muestra la matriz en pantalla.
matriz_aleatoria = np.random.rand(3,3)
print(f'matriz_aleatoria: {matriz_aleatoria}')

# 4. Crear una matriz identidad de tamaño 4x4 utilizando eye.
# • Muestra la matriz identidad.
matriz_identidad = np.eye(4)
print(f'matriz_identidad: {matriz_identidad}')

matriz_aleatoria = np.random.randint(0, 2, (3,3))
print(f'matriz_aleatoria: {matriz_aleatoria}')

# 5. Redimensionar el vector creado en el punto 2 en una matriz de 2x5 usando .reshape.
# • Muestra la nueva matriz.
vector_redimensionado = vector_original.reshape(2,5)
print(f'Matriz redimensionada: {vector_redimensionado}')

# 6. Seleccionar los elementos mayores a 5 del vector original y mostrarlo.
# • Utiliza indexación condicional.
vector_indexado = vector_original[vector_original > 5]
print(f'vector_indexado: {vector_indexado}')

# 7. Realizar una operación matemática entre arreglos.
# • Crea dos arreglos de tamaño 5 con arange() y súmalos.
# • Muestra el resultado.
vector_1 = np.arange(1,6) # [1,2,3,4,5]
vector_2 = np.arange(6,11)# [6,7,8,9,10]
print(f'suma {vector_1 + vector_2}')

# 8. Aplicar una función matemática a un arreglo.
# • Calcula la raíz cuadrada de los elementos del vector original.
# • Muestra el resultado.
raiz_cuadrada = np.sqrt(vector_original)
print(f'raiz cuadrada vector_original: {raiz_cuadrada}')