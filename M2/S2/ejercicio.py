'''
Escribe un programa en Python que permita al usuario ingresar su nombre y su edad. Luego, el programa debe imprimir un mensaje indicando cuántos años tendrá el usuario en 5 años.
Ejemplo de entrada y salida:
Si el usuario ingresa nombre = "Jose" y edad = 25, el programa debe mostrar:
 
Hola Jose, en 5 años tendrás 30 años.
'''
# ingreso de datos
nombre = 'Jose'
edad = 25

# acumulacion, calculo de edad futura
edad_futura = edad + 5

# impresion de datos o salida
# print('Hola' + ' ' + nombre +  ' ' + 'en 5 años tendras' + ' ' + edad_futura + ' ' + 'años')
print(f'Hola {nombre}, en 5 años tendrás {edad_futura} años.')

print('-----------------------------------------------------')

# ingreso de datos
nombre = input('Ingresa tu nombre: ') # ingresa string
edad = int(input('Ingresa la edad: ')) # ingresa string y se entrega el string inmediatamente al metodo int
futuro = input('Ingrese los años futuros para calcular la edad: ') # ingresa string
futuro = int(futuro) # entrega valor a metodo int y lo convierte acumulando en la variable

# acumulacion, calculo de edad futura
edad_futura = edad + futuro

# impresion de datos o salida
print(f'Hola {nombre}, en {futuro} años tendrás {edad_futura} años.')

print('-----------------------------------------------------')

# ingreso de datos
try: # intenta ejecutar el siguiente código
    nombre = input('Ingresa tu nombre: ') # ingresa string
    edad = int(input('Ingresa la edad: ')) # ingresa string y se entrega el string inmediatamente al metodo int
    futuro = input('Ingrese los años futuros para calcular la edad: ') # ingresa string
    futuro = int(futuro) # entrega valor a metodo int y lo convierte acumulando en la variable

    # acumulacion, calculo de edad futura
    edad_futura = edad + futuro

    # impresion de datos o salida
    print(f'Hola {nombre}, en {futuro} años tendrás {edad_futura} años.')
except Exception as e: # ocurre un error, se captura y se realiza alguna ejecución
    print(e) # imprimir el error en consola
    print(f'Usuario ha ingresado un valor erroneo')
        