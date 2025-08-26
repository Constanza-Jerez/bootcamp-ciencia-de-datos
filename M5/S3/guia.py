# -*- coding: utf-8 -*-
"""
Variables Aleatorias y Distribuciones
"""

# 1. Variables Aleatorias Discretas
# - Toman valores contables (ej: número de caras al lanzar monedas, número de clientes, productos defectuosos).
# - No existen valores intermedios entre dos resultados consecutivos.
ejemplo_discreta = [0, 1, 2, 3]  # Número de caras al lanzar una moneda tres veces

# 2. Variables Aleatorias Continuas
# - Pueden tomar cualquier valor dentro de un intervalo (ej: tiempo de espera, altura, temperatura, distancia).
# - Hay infinitos valores posibles entre dos puntos.
ejemplo_continua = "Altura de estudiantes (ej: 1.65m, 1.725m, ... cualquier valor en un rango)"

# 3. Distribución de Probabilidad
# - Discretas: función de masa de probabilidad (PMF), asigna una probabilidad a cada valor posible.
#   Propiedades: 0 ≤ P(X=χ) ≤ 1 y la suma de todas las probabilidades es 1.
#   Ejemplo: Dado justo, cada cara tiene probabilidad 1/6.
valores_dado = [1, 2, 3, 4, 5, 6]
probabilidad_cada_cara = 1 / 6

# - Continuas: función de densidad de probabilidad (FDP), la probabilidad de un valor exacto es 0,
#   se calcula la probabilidad en intervalos.
#   Ejemplo: Altura de adultos, probabilidad de estar entre 160 y 180 cm.

# 4. Distribución Acumulada de Probabilidad (CDF)
# - F(x) = P(X ≤ x): probabilidad acumulada hasta un valor x.
# - Es monótonamente creciente, inicia en 0 y termina en 1.
# - Para discretas: tiene saltos; para continuas: es suave.

# 5. Distribuciones Discretas y Continuas
# - Uniforme discreta: todos los resultados tienen la misma probabilidad (ej: dado).
# - Bernoulli: dos resultados posibles (éxito/fracaso).
# - Binomial: número de éxitos en n ensayos independientes.
# - Poisson: número de eventos en un intervalo de tiempo/espacio.
# - Uniforme continua: todos los valores en un intervalo tienen la misma densidad.
# - Normal: forma de campana, simétrica, usada en fenómenos naturales.
# - Exponencial: tiempo entre eventos en procesos de Poisson.
# - Chi-cuadrado, t-Student, F de Fisher: usadas en inferencia y pruebas estadísticas.

# 6. Elección de Distribución
# - Depende de si los datos son discretos (conteos) o continuos (mediciones).
# - Considera el contexto del problema y realiza pruebas de bondad de ajuste.
# - Visualiza los datos (histogramas, QQ-plots) y estima parámetros si es posible.

# 7. Distribución Normal
# - Forma de campana, simétrica.
# - Media, mediana y moda coinciden.
# - Regla 68-95-99.7: 68% de los datos en ±1σ, 95% en ±2σ, 99.7% en ±3σ.
# - Función de densidad: f(x) = (1/(σ√2π))·e^(-(x-μ)²/(2σ²))
# - Para calcular probabilidades, se estandariza (Z-score) y se consulta la tabla Z.