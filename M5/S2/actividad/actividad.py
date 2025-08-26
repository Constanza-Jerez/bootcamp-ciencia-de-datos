# 1. experimento aleatorio y deterministico
# a) Medir altura de una persona
    # Deterministico: Seleccion de una persona especifica
    # Aleatorio: Selección de persona al azar, la altura es incierta.
# b) Lanzar un dado de seis caras.
    # Aleatorio: El resultado no se puede predecir, puede salir cualquier número
    
# 2. Construcción del espacio muestral
# S = {C,S}
# S = {CC,CS,SC,SS}

# 3. Idenficación de eventos aleatorios
    # considerando el experimiento de lanzar un dado de seis caras:
        # a) escribe el evento de obtener un número par
            # A = {2, 4, 6}
        # b) escribe el evento de obtener un número menor que 3
            # B = {1, 2}
            
# 4. cálculo de probabilidad de un evento
# calculo de probabilidad de obtener un número par al lanzar un dado de seis caras.
# P = numero_resultados_favorables / numero_total_resultados_posibles
# eventos favorables = {2, 4, 6}
# numero total resultados  = {1, 2, 3, 4, 5, 6}
numero_resultados_favorables = 3
numero_total_resultados_posibles = 6
P = 3 / 6

# 5. arbol de probabilidades
# experimento de lanzar una moneda dos veces
'''
C(0.5) X(O.5) = 1 probabilidad
CC(0.5) CX(0.5)
XC(0.5) XX(0.5)
'''