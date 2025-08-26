import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 1. Conceptos básicos de distribución muestral
# • Explica con tus propias palabras qué es la distribución muestral y en qué se diferencia de la distribución de la población y la distribución de una muestra.
'''
Distribución muestral o media de una distribución poblacional
Se diferencia de la distribución de la población ya que busca es la media de una distribución muestral y la distribución poblacional es la toma completa de datos que puede tomar una variable o poblacion
Se diferencia de la distribución de una muestra en que la distribución de una muestra busca obtener algunos valores que puede tomar una variable.
'''

# 2. Ley de los grandes números
# • Se lanza una moneda equilibrada 10 veces y se obtiene cara en 7 de ellas.
# • Explica si este resultado contradice la ley de los grandes números.

'''
establece que, a medida que el tamaño de la muestra 'n' aumenta, la media muestral verline{X} se aproxima a la media poblacional u
'''

# 3. Teorema del límite central
# • Se sabe que el tiempo promedio de espera en una fila de banco sigue una distribución uniforme entre 5 y 15 minutos. Se toma una muestra aleatoria de 36 clientes.
# • Explica por qué el teorema del límite central es útil en este caso.
# • Calcula la media y la desviación estándar de la distribución muestral de la media.
minimo = 5
maximo = 15
n = 36 # clientes 

media_poblacional = (minimo + maximo) / 2
varianza_poblacional = ((maximo - minimo)** 2) / 12
desviacion_std_poblacional = np.sqrt(varianza_poblacional)
print(f'media poblacional: {media_poblacional}')
print(f'varianza poblacional: {varianza_poblacional}')
print(f'desviacion estandar poblacional: {desviacion_std_poblacional}')

# distribucion media muestral = media poblacional
media_muestral = media_poblacional
desviacion_muestral = desviacion_std_poblacional / np.sqrt(n)

print(f'distribución medio muestral: {media_muestral}')
print(f'desviación muestral: {desviacion_muestral}')

# grafico simulación teorema del límite central
medias_muestrales = [np.mean(np.random.uniform(minimo, maximo, n)) for _ in range(1000)]
plt.figure(figsize=(8,5))
sns.histplot(medias_muestrales, bins=20, color='blue', kde=True, edgecolor='black', stat='density')
plt.xlabel('Media Muestral')
plt.ylabel('Densidad')
plt.title(f'Distribución de Medias Muestrales (n={n}) de una Distribución normal')
plt.grid(True)
plt.show()

# 4. Cálculo de probabilidades con la distribución muestral
# • La duración de una llamada telefónica en una empresa sigue una distribución normal con una media de 8 minutos y una desviación estándar de 2 minutos. Se selecciona una muestra aleatoria de 25 llamadas.
# • Calcula la probabilidad de que el tiempo promedio de duración de la muestra sea menor a 7.5 minutos.

# Datos: duración de llamadas ~ N(8, 2), muestra de 25
mu = 8    # media poblacional
sigma = 2 # desviación estándar poblacional
n = 25    # tamaño de la muestra
x = 7.5   # valor para calcular la probabilidad
 
# Media y desviación estándar de la distribución muestral
mu_muestra = mu
sigma_muestra = sigma / np.sqrt(n)
 
# Z-score y cálculo de la probabilidad P(X̄ < 7.5)
z = (x - mu_muestra) / sigma_muestra
probabilidad = norm.cdf(z)
 
print(f"- Z-score: {z:.2f}")
print(f"- Probabilidad de que la media muestral sea menor a 7,5 minutos: {probabilidad:.4f}")

# Valores para graficar la PDF
x = np.linspace(mu - 4*sigma_muestra, mu + 4*sigma_muestra, 1000)
pdf = norm.pdf(x, loc=mu, scale=sigma_muestra)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f'N({mu}, {sigma_muestra}²)', color='blue')
plt.fill_between(x, pdf, where=(x <= 7.5),
                 alpha=0.3, color='blue', label=f'P(min_rango ≤ X ≤ {7.5}) ≈ {probabilidad:.4f}')
plt.title('Distribución Normal')
plt.xlabel('Tiempo (Minutos)')
plt.ylabel('Densidad')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Graficar histograma de medias muestrales
# plt.figure(figsize=(8, 5))
# sns.histplot(medias_muestrales, kde=True, stat="density", color="salmon", bins=40, edgecolor='black', label='Medias simuladas')

# Agregar la curva normal teórica para comparación
# from scipy.stats import norm
# medias_muestrales = [np.mean(np.random.uniform(2, 15, n)) for _ in range(1000)]
# x_vals = np.linspace(min(medias_muestrales), max(medias_muestrales), 1000)
# y_vals = norm.pdf(x_vals, loc=mu_muestra, scale=sigma_muestra)
# plt.plot(x_vals, y_vals, color='navy', linestyle='--', linewidth=2, label='Distribución Normal Teórica')
 
# plt.title("Distribución de las Medias Muestrales\n(TLC con muestras de U(5,15), n=36)")
# plt.xlabel("Media muestral")
# plt.ylabel("Densidad")
# plt.legend()
# plt.grid(True, axis='y')
# plt.show()