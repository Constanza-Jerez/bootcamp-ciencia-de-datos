# Formulación de Hipótesis y Diseño de un Experimento
#
# Objetivo: Aprender a formular una hipótesis sobre un problema de interés y diseñar un experimento para probarla.
# Cada sección incluye explicación y ejemplo.

# 1. Identificar un Problema de Interés
# Ejemplo: ¿Dormir más horas mejora el rendimiento académico de los estudiantes universitarios?
problema = "¿Dormir más horas mejora el rendimiento académico de los estudiantes universitarios?"
print(f"Problema de interés: {problema}")

# 2. Formular una Hipótesis
# Hipótesis nula (H0): No hay diferencia en el rendimiento académico entre estudiantes que duermen más y los que duermen menos.
# Hipótesis alternativa (H1): Los estudiantes que duermen más horas tienen mejor rendimiento académico.
print("Hipótesis nula (H0): No hay diferencia en el rendimiento académico entre estudiantes que duermen más y los que duermen menos.")
print("Hipótesis alternativa (H1): Los estudiantes que duermen más horas tienen mejor rendimiento académico.")

# 3. Definir las Variables
# Variable independiente: Horas de sueño por noche
# Variable dependiente: Calificación promedio
print("Variable independiente: Horas de sueño por noche")
print("Variable dependiente: Calificación promedio")

# 4. Diseñar el Experimento
# - Seleccionar una muestra de estudiantes universitarios.
# - Medir cuántas horas duermen por noche durante un mes.
# - Registrar sus calificaciones promedio al final del periodo.
# - Dividir a los estudiantes en dos grupos: los que duermen >= 7 horas y los que duermen < 7 horas.
print("Diseño del experimento: Se selecciona una muestra de estudiantes, se mide su sueño y calificaciones, y se comparan los grupos de sueño alto y bajo.")

# 5. Realizar el Análisis de Datos (Simulación)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
n = 100
horas_sueno = np.random.normal(7, 1.5, n)
calificacion = 70 + 3 * (horas_sueno >= 7) + np.random.normal(0, 5, n)
df = pd.DataFrame({'Horas_Sueno': horas_sueno, 'Calificacion': calificacion})

# Comparar promedios de ambos grupos
grupo_alto = df[df['Horas_Sueno'] >= 7]['Calificacion']
grupo_bajo = df[df['Horas_Sueno'] < 7]['Calificacion']
print(f"Promedio calificación (>=7h): {grupo_alto.mean():.2f}")
print(f"Promedio calificación (<7h): {grupo_bajo.mean():.2f}")

# Prueba estadística: t-test para diferencia de medias
from scipy.stats import ttest_ind
stat, p = ttest_ind(grupo_alto, grupo_bajo, equal_var=False)
print(f"t-statistic: {stat:.2f}, p-value: {p:.4f}")

# 6. Interpretar los Resultados
if p < 0.05:
    print("Resultado: Se rechaza la hipótesis nula. Hay evidencia de que dormir más horas mejora el rendimiento académico.")
else:
    print("Resultado: No se rechaza la hipótesis nula. No hay evidencia suficiente de diferencia.")

# 7. Concluir y Comunicar los Hallazgos
print("Conclusión: El análisis sugiere que los estudiantes que duermen más de 7 horas tienden a tener mejores calificaciones, aunque siempre se debe considerar el tamaño de la muestra y otros factores externos.")

plt.figure()
plt.scatter(df['Horas_Sueno'], df['Calificacion'], color='purple', alpha=0.7)
plt.title('Diagrama de Dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()