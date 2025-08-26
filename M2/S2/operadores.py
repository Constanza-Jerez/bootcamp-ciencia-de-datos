# operadores aritmeticos
print(3 + 4) # 7
print(3 - 4) # -1
print(3 * 4) # 12
print(3 / 4) # 0.75
print(3 // 4)# 0
print(3 % 4) # 3

# jerarquia operadores aritmeticos
# parentesis
# potencia, raíz
# multiplación, división
# suma, resta
valor = 2 * 3 + (5 - 1) / 2
print(valor) # 8.0

# operador usando cadenas de caracteres o string
# concatenación
print('Hola' + ' ' + 'Python') # Hola Python
# print('Hola' + 5) # TypeError: can only concatenate str (not "int") to str
print('Hola' + str(5)) # Hola5

# operacion mixta
print('Hola' * (2 ** 3)) # HolaHolaHolaHolaHolaHolaHolaHola

# operadores de comparación
print(3 < 4) # True
print(3 > 4) # False
print(3 >= 4)# False , condición de borde
print(3 <= 4)# True  , condición de borde
print(3 == 4)# False
print(3 != 4)# True

# operadores de comparacion para cadenas de caracteres
print('-------------------------------------------')
cadena_1 = 'valor1'
cadena_2 = 'valor2'
# compara ascii
print(cadena_1 < cadena_2) # True
print(cadena_1 > cadena_2) # False
print(cadena_1 <= cadena_2)# True
print(cadena_1 >= cadena_2)# False
print(cadena_1 == cadena_2)# False
print(cadena_1 != cadena_2)# True
# compara cuenta de caracteres
print(len(cadena_1) > len(cadena_2)) # False
print(len(cadena_1))

# operadores and, or, not
print('-------------------------------------------')
print(3 > 4 and cadena_1 < cadena_2) # deben cumplirse las dos, si la primera no se cumple break
print(3 < 4 and cadena_1 < cadena_2) # se cumplen las dos, True
print(3 < 4 and cadena_1 > cadena_2) # se cumple la primera, no la segunda, False
print(3 < 4 or cadena_1 > cadena_2) # al menos una se cumple, True
print(3 > 4 or cadena_1 < cadena_2) # al menos una se cumple, True
print(not (3 > 4)) # negacion, cambia el resultado de la condición