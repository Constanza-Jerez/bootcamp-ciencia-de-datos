- **Variables Aleatorias**:
    - **Discretas**: Toman un número finito o infinitamente numerable de valores distintos (ejemplo: número de caras al lanzar una moneda).
    - **Continuas**: Pueden tomar cualquier valor dentro de un intervalo (ejemplo: tiempo de espera).

- **Distribución de Probabilidad**:
    - Describe cómo se distribuyen las probabilidades.
    - **Discretas**: Se usa la función de probabilidad \( P(X = x) \).
    - **Continuas**: Se utiliza la función de densidad de probabilidad (FDP) para calcular la probabilidad en un intervalo.
    - Son esenciales para predecir resultados y modelar fenómenos inciertos.

- **Función de Distribución Acumulada (CDF)**:
    - \( F(x) = P(X \leq x) \): Indica la probabilidad de que una variable aleatoria tome un valor menor o igual a un valor específico.
    - Es monótonamente creciente.
    - Para variables continuas, es una función suave.

- **Distribuciones Discretas Comunes**:
    - **Uniforme Discreta**: Misma probabilidad para todos los resultados.
    - **Bernoulli**: Experimentos con dos resultados.
    - **Binomial**: Número de éxitos en \( n \) repeticiones.
    - **Poisson**: Número de eventos en un intervalo.

- **Distribuciones Continuas Importantes**:
    - **Uniforme Continua**: Misma densidad en un intervalo.
    - **Normal**: Forma de campana y simétrica, la más importante.
    - **Exponencial**: Modela el tiempo entre eventos.
    - Otras: **Chi-Cuadrado**, **t-Student**, **F de Fisher** (usadas en pruebas de hipótesis).

- **Elección de una Distribución**:
    - Considerar si los datos son discretos o continuos.
    - Analizar el contexto del problema (ejemplo: Binomial para éxito/fracaso, Normal para datos con tendencia central).
    - Realizar pruebas de bondad de ajuste y visualización de datos.

- **Distribución Normal**:
    - Forma de campana; media, mediana y moda coinciden.
    - Sigue la **Regla 68-95-99.7** para la dispersión de datos alrededor de la media.
    - Para calcular probabilidades, se **estandariza** el valor usando \( Z = \frac{X - \mu}{\sigma} \) y se consulta una tabla Z.