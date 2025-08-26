'''
Realizar la ejecución de un menú utilizando el lenguaje Python, 
donde se le indiquen varias opciones a seleccionar por el usuario 
y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales.
'''
# importar libreria de expresiones regulares
import re

# iniciar el ciclo
opcion = '' # variable opcion se inicializa vacio
patron = re.compile('^[1-5]{1}$')
while opcion != '5': # mientras la opcion sea diferente a 5 el codigo se ejecuta
    # impresion de menu
    print('1. Opción 1')
    print('2. Opción 2')
    print('3. Opción 3')
    print('4. Opción 4')
    print('5. Salir del menú')
    opcion = input('Ingrese una opción: ') # muestra mensaje y pide al usuario ingresar una opción en la terminal
    
    if re.match(patron, opcion):
        if opcion == '1': # opcion es igual a 1?
            print('Ejecutando opción 1')
        elif opcion == '2': 
            print('Ejecutando opción 2')
        elif opcion == '3':
            print('Ejecutando opción 3')
        elif opcion == '4':
            print('Ejecutando opción 4')
        elif opcion == '5':
            print('Saliendo del menú')    
            # break
        else:
            print('Ha ingresado una opción invalida, por favor ingrese una opción')
    else:
        print('Ha ingresado un valor incorrecto, valide el ingreso')        



'''
# iniciar el ciclo
while True: # mientras sea True el ciclo continuara infinito o hasta que suceda un break
    # impresion de menu
    print('1. Opción 1')
    print('2. Opción 2')
    print('3. Opción 3')
    print('4. Opción 4')
    print('5. Salir del menú')
    opcion = input('Ingrese una opción: ') # muestra mensaje y pide al usuario ingresar una opción en la terminal
    
    if opcion == '1': # opcion es igual a 1?
        print('Ejecutando opción 1')
    elif opcion == '2': 
        print('Ejecutando opción 2')
    elif opcion == '3':
        print('Ejecutando opción 3')
    elif opcion == '4':
        print('Ejecutando opción 4')
    elif opcion == '5':
        print('Saliendo del menú')    
        break
    else:
        print('Ha ingresado una opción invalida, por favor ingrese una opción')
'''        