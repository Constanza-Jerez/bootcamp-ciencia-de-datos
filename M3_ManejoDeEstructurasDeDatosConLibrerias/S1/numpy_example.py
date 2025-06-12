# numpy libreria para realizar calculos y tareas sobre listas o arreglos
# para instalar ejecutar en la terminal `pip install numpy`

import numpy as np

# vectores en numpy
vector = np.arange(1,11)
print(f'vector: {vector}')

vector_array = np.array([1,2,3,4,5,6,7,8,9,10,11])
print(f'vector_array: {vector_array}')

vector_array = vector_array * 2
print(f'vector_array: {vector_array}')

# matriz
matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(matriz)

# matriz transpuesta
print(f'matriz transpuesta: {matriz.T}')
'''
[[1 4 7]
 [2 5 8]
 [3 6 9]]
'''

# operaciones sobre matrices
print(f'suma {matriz + matriz.T}')
'''
[[ 2  6 10]
 [ 6 10 14]
 [10 14 18]]
'''

# matriz tridimensional
matriz_tridimensional = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])
print(matriz_tridimensional)
'''
[[[1 2]
  [3 4]]
 [[5 6]
  [7 8]]]
'''

# funciones predefinidas en numpy
# np.arange(inicio,fin,paso)
vector_arange = np.arange(1,11)
print(f'vector_arange: {vector_arange}')

# zeros and ones necesitan tuplas para declaracion
zeros = np.zeros((3,3))
print(zeros)
unos = np.ones((2,2))
print(unos)

# linspaces
# np.linspace(start,stop,count)
vestor_linspaces = np.linspace(1,11,5)
print(f'vector_linspaces: {vestor_linspaces}')

# matriz identidad
matriz_identidad = np.eye(4)
print(f'matriz identidad: {matriz_identidad}')
'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''

# matriz aleatoria
matriz_aleatoria = np.random.rand(3,3)
print(f'matriz_aleatoria: {matriz_aleatoria}')
'''
[[0.80920059 0.71467279 0.29192409]
 [0.47083726 0.49149896 0.9955846 ]
 [0.47083726 0.49149896 0.9955846 ]
 [0.42798138 0.77735967 0.43338524]]
'''

matriz_aleatoria = np.random.randint(1, 100, (3,3))
print(f'matriz_aleatoria: {matriz_aleatoria}')
'''
[[62  1 63]
 [96 53 71]
 [20 68  4]]
'''

# redimensión de matriz
matriz_a = np.arange(9)
print(f'matriz_a: {matriz_a}') # [0 1 2 3 4 5 6 7 8]

matriz_a = matriz_a.reshape(3,3)
print(f'matriz_a: {matriz_a}')
'''
 [[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
 