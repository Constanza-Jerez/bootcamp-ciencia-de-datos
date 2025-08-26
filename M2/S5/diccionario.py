#ordenados por clave y valor
#diccionarios, es una coleccion de elementos
#declaracion con llaves {} o con la funcion dict()

estudiantes = {
    #clave:valor
    "Fulanito":25,
    "Maria": 22,
    "Jose": 40,
    "Marta": 30
}

print(estudiantes) #{'Fulanito': 25, 'Maria': 22, 'Jose': 40, 'Marta': 30}

#acceder al valor de una clave
# nombre_diccionario["clave"]
print(estudiantes["Fulanito"]) #25

#remover clave de un dicccionario
del estudiantes["Fulanito"]
print(estudiantes) #{'Maria': 22, 'Jose': 40, 'Marta': 30}

#agregar elementos mediante la clave
estudiantes['Fulanito'] = [25]

#obtener todas las claves de un dicccionario
claves = estudiantes.keys() 
print(claves) #dict_keys(['Maria', 'Jose', 'Marta'])

#obtener todos los valores
valores = estudiantes.values()
print(valores) #dict_values([22, 40, 30])

#borrar un diccionario
estudiantes.clear()
print(estudiantes)

mi_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}
 
 
print(mi_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
 
# Acceder a un valor por su clave
print(mi_dict["a"])  # 1
 
# Agregar un nuevo par clave-valor
mi_dict["f"] = 6
print(mi_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
 
# Eliminar un par clave-valor
del mi_dict["b"]
print(mi_dict)  # {'a': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
 
# Verificar si una clave existe
print("c" in mi_dict)  # True
 
# Obtener todas las claves
print(mi_dict.keys())  # dict_keys(['a', 'c', 'd', 'e', 'f'])
 
# Obtener todos los valores
print(mi_dict.values())  # dict_values([1, 3, 4, 5, 6])
 
# Obtener todos los pares clave-valor
print(mi_dict.items())  # dict_items([('a', 1), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])
 
# Limpiar el diccionario
mi_dict.clear()
print(mi_dict)  # {}
 
# Crear un nuevo diccionario
nuevo_dict = dict(a=1, b=2, c=3)
print(nuevo_dict)  # {'a': 1, 'b': 2, 'c': 3}
 
# Actualizar un diccionario con otro
mi_dict.update(nuevo_dict)
print(mi_dict)  # {'a': 1, 'b': 2, 'c': 3}
 
# Obtener el valor por defecto de una clave
print(mi_dict.get("d", "No existe"))  # No existe
 
# Obtener el valor por defecto de una clave existente
print(mi_dict.get("a", "No existe"))  # 1
 
# Copiar un diccionario
copia_dict = mi_dict.copy()
print(copia_dict)  # {'a': 1, 'b': 2, 'c': 3}
 
# Verificar si un valor existe
print(2 in mi_dict.values())  # True
 
# Iterar sobre un diccionario
for clave, valor in mi_dict.items():
    print(f"Clave: {clave}, Valor: {valor}") # {'a': 1, 'b': 2, 'c': 3}
 
# Crear un diccionario con comprensión de diccionarios
comprehension_dict = {x: x**2 for x in range(5)}
print(comprehension_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
 
# Crear un diccionario a partir de dos listas
keys = ['a', 'b', 'c']
values = [1, 2, 3]
list_to_dict = dict(zip(keys, values))
print(list_to_dict)  # {'a': 1, 'b': 2, 'c': 3}
 
# Crear un diccionario con valores por defecto
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
 
# Acceder a un valor por clave con valor por defecto
print(default_dict['c'])  # 0 (valor por defecto, ya que 'c' no existe)
 
# Crear un diccionario anidado
nested_dict = {
    'a': {
        'x': 1, 
        'y': 2
        },
    'b': {'x': 3, 'y': 4}
}