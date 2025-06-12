# 1. Importar la librería NumPy
import numpy as np

# 2. Crear un vector de 10 elementos con valores del 1 al 10 utilizando arange()
# • Muestra el vector generado.

vector = np.arange(1,11)
print(f'Vector: \n{vector}')

# 3. Generar una matriz de 3x3 con valores aleatorios entre 0 y 1 usando random.rand() 
# • Muestra la matriz en pantalla.

matriz_aleatoria = np.random.rand(3,3)
print(f'Matriz Aleatoria: \n{matriz_aleatoria}')

# 4. Crear una matriz identidad de tamaño 4x4 utilizando eye()
# • Muestra la matriz identidad.

matriz_identidad = np.eye(4)
print(f'Matriz Identidad: \n{matriz_identidad}')

matriz_identidad = np.random.randint(0, 2, (3,3))
print(f'Matriz Identidad: \n{matriz_identidad}')

# 5. Redimensionar el vector creado en el punto 2 en una matriz de 2x5 usando .reshape()
# • Muestra la nueva matriz.

vector = vector.reshape(2,5)
print(f'matriz_a: \n{vector}')

# 6. Seleccionar los elementos mayores a 5 del vector original y mostrarlos 
# • Utiliza indexación condicional.



# 7. Realizar una operación matemática entre arreglos 
# • Crea dos arreglos de tamaño 5 con arange() y súmalos.
# • Muestra el resultado.


# 8. Aplicar una función matemática a un arreglo 
# • Calcula la raíz cuadrada de los elementos del vector original.
# • Muestra el resultado

# raiz_cuadrada = np.sqrt(vector)
# print("\n8. Raíz cuadrada de los elementos del vector original:")
# print([f"{x:.2f}" for x in raiz_cuadrada])