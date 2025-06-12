# ACTIVIDAD SESIÓN LA LIBRERÍA PANDAS
# Eres un analista de datos en un club de fútbol que busca mejorar el rendimiento de los jugadores. 
# Te han proporcionado un archivo con datos sobre los futbolistas del equipo, incluyendo 
# su nombre, posición, edad, goles y asistencias en la última temporada. 
# Tu tarea es analizar estos datos usando Pandas para responder preguntas clave.

# INSTRUCCIONES:
# 1. Importa la librería Pandas y crea un DataFrame con los siguientes datos: (1 punto).
import pandas as pd

# Jugador Posición Edad Goles Asistencias
# -|   Nombre Jugador   |    Posición   |   Edad   |   Goles  | Asistencias |
# -|--------------------|---------------|----------|----------|-------------|
# 0| Lionel Messi       | Delantero     |    35    |    20    |      10     |
# 1| Cristiano Ronaldo  | Delantero     |    38    |    18    |       5     |
# 2| Kevin De Bruyne    | Mediocampista |    31    |    8     |      15     |
# 3| Kylian Mbapp       | Delantero     |    24    |    25    |      12     |
# 4| Luka Modric        | Mediocampista |    37    |    3     |       8     |

# Pista: Usa pd.DataFrame() para crear la tabla.
data = {
    'Nombre Jugador': ['Lionel Messi','Cristiano Ronaldo',
                       'Kevin De Bruyne','Kylian Mbapp','Luka Modric'],
    'Posicion':['Delantero', 'Delantero', 'Mediocampista','Delantero', 'Mediocampista'],
    'Edad':[35,38,31,24,37],
    'Goles':[20,18,8,25,3],
    'Asistencias':[10,5,15,12,8]
}
df = pd.DataFrame(data)
print(df)
print('----------------------------------------------------------------------------')

# 2. Selecciona una columna y muestra los nombres de todos los jugadores (1 punto).
nombre_jugadores = df['Nombre Jugador']
print(nombre_jugadores)
print('----------------------------------------------------------------------------')

# 3. Filtra jugadores con más de 10 goles y muestra solo su nombre y cantidad de goles (1 punto).
jugadores_10_goles = df[df['Goles']>10][['Nombre Jugador','Goles']]
print(jugadores_10_goles)
print('----------------------------------------------------------------------------')

# 4. Agrega una nueva columna al DataFrame llamada Puntos, donde cada jugador obtiene
# Puntos = (Goles * 4) + (Asistencias * 2) (1 punto).
df['Puntos'] = (df['Goles']*4) + (df['Asistencias']*2)
print((df[['Nombre Jugador','Posicion','Edad','Goles','Asistencias','Puntos']]))
print('----------------------------------------------------------------------------')

# 5. Calcula el promedio de goles de todos los jugadores (1 punto).
promedio_goles = df['Goles'].mean()
print(f'Promedio de Goles: {promedio_goles}')
print('----------------------------------------------------------------------------')

# 6. Obtén el máximo y mínimo de asistencias en el equipo (1 punto).
minimo_asistencias = (df['Asistencias'].min())
maximo_asistencias = (df['Asistencias'].max())
print(f'Mínimo de Asistencias: {minimo_asistencias}')
print(f'Máximo de Asistencias: {maximo_asistencias}')
print('----------------------------------------------------------------------------')

# 7. Cuenta cuántos jugadores hay por posición (Delantero, Mediocampista) (1 punto).
jugadores_por_posicion = df['Posicion'].value_counts()
print(f'N° de jugadores por {jugadores_por_posicion}')
print('----------------------------------------------------------------------------')

# 8. Ordena el DataFrame en función de los goles en orden descendente (1 punto).
df_descendente = df.sort_values('Goles')
print(f'Dataframe orden descendente {df_descendente}')
print('----------------------------------------------------------------------------')

# 9. Aplica describe() para obtener estadísticas generales del DataFrame (1 punto).
data_descriptiva = df.describe()
print(f'Data descriptiva: {data_descriptiva}')
print('----------------------------------------------------------------------------')

# 10. Usa value_counts() para contar cuántos jugadores hay en cada posición (1 punto).
jugadores_por_posicion = df['Posicion'].value_counts()
print(f'N° de jugadores por {jugadores_por_posicion}')
print('----------------------------------------------------------------------------')


# INSTRUCCIONES ADICIONALES:
# • Puntos totales = 10.
# • Comprimir el archivo completo en formato .zip o .rar.
# • Sube el archivo a la plataforma