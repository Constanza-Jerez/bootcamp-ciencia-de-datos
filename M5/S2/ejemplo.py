"""
Actividad: Probabilidad y Experimentos Aleatorios - Ejemplo 2
Módulo 5 - Sesión 2

REQUERIMIENTOS:

1. Distinguir entre experimento aleatorio y determinístico
   a) Medir la temperatura de una ciudad a las 12:00 pm.
   b) Encender una lámpara con un interruptor.

2. Construcción del espacio muestral
   - Escribe el espacio muestral para el experimento de lanzar dos dados de seis caras.

3. Identificación de eventos aleatorios
   a) Evento de obtener una suma igual a 7 al lanzar dos dados.
   b) Evento de obtener al menos un 6 al lanzar dos dados.

4. Cálculo de probabilidad de un evento
   - Calcula la probabilidad de obtener una suma igual a 7 al lanzar dos dados.

5. Árbol de probabilidades
   - Dibuja un árbol de probabilidades para el experimento de lanzar una moneda tres veces.
"""

# 1. Distinguir entre experimento aleatorio y determinístico
#    a) Medir la temperatura de una ciudad a las 12:00 pm.
# aleatorio: Puede variar la temperatura cada día

#    b) Encender una lámpara con un interruptor.
# deterministico: si el interruptor funciona, encenderá la lampara

#--------------------------------------------------------------------------------------------
# 2. Construcción del espacio muestral
#    - Escribe el espacio muestral para el experimento de lanzar dos dados de seis caras.
'''
    S = {1,2,3,4,5,6}
    S = {1.1, 1.2, 1.3, 1.4, 1.5, 1.6}
        {2.1, 2.2, 2.3, 2.4, 2.5, 2.6}
        {3.1, 3.2, 3.3, 3.4, 3.5, 3.6}
        {4.1, 4.2, 4.3, 4.4, 4.5, 4.6}
        {5.1, 5.2, 5.3, 5.4, 5.5, 5.6}
        {6.1, 6.2, 6.3, 6.4, 6.5, 6.6}
'''
# hay 36 resultados posibles

#--------------------------------------------------------------------------------------------
# 3. Identificación de eventos aleatorios
#    a) Evento de obtener una suma igual a 7 al lanzar dos dados.
'''
    S = {1,2,3,4,5,6}
    S = {1.1, 1.2, 1.3, 1.4, 1.5, x1.6}
        {2.1, 2.2, 2.3, 2.4, x2.5, 2.6}
        {3.1, 3.2, 3.3, x3.4, 3.5, 3.6}
        {4.1, 4.2, x4.3, 4.4, 4.5, 4.6}
        {5.1, x5.2, 5.3, 5.4, 5.5, 5.6}
        {x6.1, 6.2, 6.3, 6.4, 6.5, 6.6}
'''
# A = {6.1, 5.2, 4.3, 3.4, 2.5, 1.6}

#    b) Evento de obtener al menos un 6 al lanzar dos dados.
'''
    S = {1,2,3,4,5,6}
    S = {1.1,   1.2,  1.3,  1.4,  1.5, x1.6}
        {2.1,   2.2,  2.3,  2.4,  2.5, x2.6}
        {3.1,   3.2,  3.3,  3.4,  3.5, x3.6}
        {4.1,   4.2,  4.3,  4.4,  4.5, x4.6}
        {5.1,   5.2,  5.3,  5.4,  5.5, x5.6}
        {x6.1, x6.2, x6.3, x6.4, x6.5, x6.6} 
'''
#--------------------------------------------------------------------------------------------
# 4. Cálculo de probabilidad de un evento
#    - Calcula la probabilidad de obtener una suma igual a 7 al lanzar dos dados.
numero_eventos_favorables = {6.1, 5.2, 4.3, 3.4, 2.5, 1.6} = 6
numero_eventos_posibles = 36
P = numero_eventos_favorables / numero_eventos_posibles
P = numero_eventos_favorables / numero_eventos_posibles

# 5. Árbol de probabilidades
#    - Dibuja un árbol de probabilidades para el experimento de lanzar una moneda tres veces.

# Árbol de probabilidad (lanzamiento de moneda 3 veces):
# Inicio (P=1.0)
# ├── C (P=0.5)
# │   ├── C (P=0.25)
# │   │   ├── C (P=0.125) → (C, C, C)
# │   │   └── X (P=0.125) → (C, C, X)
# │   └── X (P=0.25)
# │       ├── C (P=0.125) → (C, X, C)
# │       └── X (P=0.125) → (C, X, X)
# └── X (P=0.5)
#     ├── C (P=0.25)
#     │   ├── C (P=0.125) → (X, C, C)
#     │   └── X (P=0.125) → (X, C, X)
#     └── X (P=0.25)
#         ├── C (P=0.125) → (X, X, C)
#         └── X (P=0.125) → (X, X, X)