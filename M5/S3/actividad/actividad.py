# 1. variables aleatorias y sus tipos
'''Asignación de valor número en un experimento aleatorio
puede tomar el valor de discreta o continua'''

# a) El número de llamadas que recibe un centro de atención en una hora.
    # Discreta (0,1,2,3...)
# b) La estatura de los estudiantes en un salón de clases.
    # Continua (valor real en un rango)
# c) La cantidad de autos que pasan por un peaje en 10 minutos.
    # Discreta (0,1,2,3...)
# d) La temperatura en una ciudad durante el día.
    # Continua (valor real en un rango)
    
# 2. Distribución discreta: binomial
'''
Un estudiante presenta un examen de opción múltiple con 5 preguntas, donde cada una tiene 4 opciones y solo una es correcta. Si responde al azar, ¿cuál es la probabilidad de que acierte exactamente 3 respuestas? (Usa la distribución binomial).
'''
from scipy.stats import binom

n = 5 # cantidad
p = 1/4 # probabilidad
k = 3 # aciertos

# pmf(k, n, p, loc=0)
probabilidad_3_aciertos = binom.pmf(k, n, p)
print(f'Probabilidad de acertar 3 respuestas: {probabilidad_3_aciertos}')

# 3. Distribución continua: Normal
# La palabra clave location () especifica el valor medio. La palabra clave scale () especifica la desviación estándar. loc scale
# cdf(x, loc=0, escala=1) Función de distribución acumulativa.
from scipy.stats import norm
'''
La estatura de los estudiantes en una universidad sigue una distribución normal con media de 1.70 m y desviación estándar de 0.08 m.
•
Calcula la probabilidad de que un estudiante seleccionado al azar tenga una estatura entre 1.65 m y 1.75 m. (Usa la distribución normal estándar).
'''
media = 1.70
std = 0.08

x_1 = 1.75
x_2 = 1.65

# cdf(x, loc=0, escala=1)
probabilidad_entre_rango = norm.cdf(x_1, loc=media, scale=std) - norm.cdf(x_2, loc=media, scale=std)
print(f'Probabilidad de estatura entre 1.65m y 1.75m: {probabilidad_entre_rango}')

# 4. Elección de distribuciones
# • Relaciona las siguientes situaciones con la distribución de probabilidad más adecuada y justifica tu respuesta:
# a) La cantidad de clientes que llegan a un restaurante por hora.
    # poisson: Modela el número de eventos en un intervalo de tiempo o espacio.
# b) El tiempo que tarda en descargarse un archivo desde internet.
    # exponencial: Modela el tiempo entre eventos en un proceso de poisson
# c) El número de piezas defectuosas en una producción de 1000 artículos.
    # binomial: Describe el número de exitos en n repeticiones (1000 articulos)