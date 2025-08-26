'''
Calcula el promedio de las tres notas, para diferentes estudiantes, realizar el ingreso desde la consola o terminal, obtener el promedio por cada estudiante y evaluar mediante condiciones los resultados.
Utilizar listas para agregar resultados

1. Solicita al usuario que ingrese el nombre y la calificación de un estudiante. Evalúa si la calificación es aprobatoria (nota mayor o igual a 60) usando una condición if else. Imprime si el estudiante ha aprobado o no.
2. Usa un bucle while para permitir la entrada de datos de varios estudiantes, hasta que el usuario decida salir.
3. Dentro del bucle while, solicita las calificaciones de tres materias diferentes para cada estudiante (por ejemplo, Matemáticas, Ciencias e Inglés). Calcula el promedio de las tres notas.
4. Usa una estructura if elif else para evaluar el promedio obtenido y asignar un comentario: “Excelente” si el promedio es 90 o más, “Bueno” si el promedio está entre 75 y 89, y “Necesita mejorar” si es menos de 75.
5. Implementa un bucle for para mostrar el nombre y los comentarios de todos los estudiantes ingresados.
6. Usa una expresión ternaria para agregar una nota adicional en los comentarios si el estudiante tiene un promedio de 100 “¡Puntuación perfecta!”.
'''
# inicializar lista vacia para acumular estudiantes y sus comentarios
# [('Fulanito', '¡Puntuación perfecta!'), (nombre, comentario), ('Jose Feliciano', 'Excelente')]
estudiantes = [] # lista se declara con corchetes o funcion list

# Blucle o ciclo while para ingresar los datos de cada estudiante
while True:
    # Ingresar nombre de estudiante
    nombre = input('Ingrese el nombre del estudiante o "Salir" para terminar: ')
    # Evaluar nombre del estudiante u opción para salir 
    if nombre.lower() == 'salir':
        break # si escribe salir, el bucle o ciclo while termina
    
    # Solicitar las calificaciones de tres materias diferentes para cada estudiante (por ejemplo, Matemáticas, Ciencias e Inglés).
    matematica = int(input(f'Ingrese la calificación para matematicas de {nombre}: '))
    ciencia = int(input(f'Ingrese la calificación para ciencias de {nombre}: '))
    ingles = int(input(f'Ingrese la calificación para ingles de {nombre}: '))
    
    # Calcular promedio de las calificaciones
    promedio = (matematica + ciencia + ingles) / 3 # promedio por estudiante
    
    # Evaluar el promedio obtenido y asignar un comentario
    if promedio >= 6:
        comentario = 'Excelente'
    elif 4 <= promedio < 6: # promedio >= 4 or promedio < 6 
        comentario = 'Bueno'
    else:
        comentario = 'Necesita mejorar' 
    
    # Expresión ternaria para agregar una nota adicional en los comentarios si el estudiante tiene un promedio de 100 “¡Puntuación perfecta!”
    # comentario = comentario + valor
    comentario += '¡Puntuación perfecta!' if promedio == 7 else ''

    # Almacenar estudiantes en la lista vacia creada al comienzo, nombre y comentario
    estudiantes.append((nombre, comentario))

# Bucle o ciclo for para mostrar el nombre y los comentarios de todos los estudiantes ingresados
print('\nResultados:')
print(estudiantes)

# for iterador in [estructura_iterar]
for nombre, comentario in estudiantes: # [('Fulanito', '¡Puntuación perfecta!'), (nombre, comentario), ('Jose Feliciano', 'Excelente')]
    print(f'{nombre} : {comentario}')
 
 