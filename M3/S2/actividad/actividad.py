import pandas as pd

SEPARACION = '-' * 50

# 1. creacion dataFrame
data = {
    'jugador': ['Lionel Messi', 'Cristiano Ronaldo', 'Kevin De Bruyne', 'Kylian Mbappé', 'Luka Modric'],
    'posicion': ['Delantero', 'Delantero', 'Mediocampista', 'Delantero', 'Mediocampista'],
    'edad': [35, 38, 31, 24, 37],
    'goles': [20,18,8,25,3],
    'asistencias': [10,5,15,12,8]
}

df = pd.DataFrame(data)

# 2. Selecciona una columna y muestra los nombres de todos los jugadores
print(df['jugador'])
print(SEPARACION)

# 3. Filtra jugadores con más de 10 goles y muestra solo su nombre y cantidad de goles.
jugadores_10_goles = df[df['goles'] > 10][['jugador','goles']]
print(jugadores_10_goles)
print(SEPARACION)

# 4. Agrega una nueva columna al DataFrame llamada Puntos, donde cada jugador obtiene Puntos = (Goles * 4) + (Asistencias * 2).
df['puntos'] = (df['goles'] * 4) + (df['asistencias'] * 2 )
print(f'data_frame:\n {df}')
print(SEPARACION)

# 5. Calcula el promedio de goles de todos los jugadores.
promedio_goles = df['goles'].mean()
print(promedio_goles)
print(SEPARACION)

# 6. Obtén el máximo y mínimo de asistencias en el equipo.
# 7. Cuenta cuántos jugadores hay por posición (Delantero, Mediocampista).
# 8. Ordena el DataFrame en función de los goles en orden descendente.

# 9. Aplica describe() para obtener estadísticas generales del DataFrame.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
print(df.describe(include='all'))
print(SEPARACION)

# 10. Usa value_counts() para contar cuántos jugadores hay en cada posición.