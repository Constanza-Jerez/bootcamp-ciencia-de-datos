# --- 1: Introducción ---
# Título de la Sesión: Análisis Exploratorio de Datos
# Matplotlib: Biblioteca de Visualización de Datos en Python
# Matplotlib es una de las bibliotecas más populares en Python para la creación de gráficos y visualización de datos.
# Se utiliza principalmente para generar gráficos estáticos, animados e interactivos, facilitando la representación visual de datos numéricos para comprender patrones y tendencias.

# --- 2: Características Principales de Matplotlib ---
# 1. Versatilidad en la creación de gráficos:
#    Permite crear gráficos básicos como líneas, barras y dispersión, así como gráficos complejos como subgráficos, gráficos 3D y de contornos.
#    También soporta gráficos interactivos en combinación con otras librerías.
# 2. Personalización detallada:
#    Ofrece control sobre colores, estilos de líneas, tamaños de marcadores, etiquetas, títulos y escalas.
#    Esta flexibilidad permite adaptar los gráficos a necesidades específicas de visualización.
# 3. Compatibilidad con otros entornos:
#    Se integra fácilmente con otras librerías de Python como NumPy, Pandas y SciPy.
#    También funciona perfectamente con Jupyter Notebooks.

# --- 3: Importación y Componentes Principales ---
# Importación de la Librería:
# La convención común es importar el módulo pyplot como plt, que proporciona funciones para crear gráficos de alta calidad.
import matplotlib.pyplot as plt #

# Componentes de un Gráfico:
# - Figura (Figure): Contenedor principal que puede incluir uno o más gráficos.
# - Ejes (Axes): Área donde se dibuja el gráfico, incluyendo los ejes X e Y.
# - Ticks: Marcas en los ejes que indican unidades o valores.
# - Etiquetas (Labels): Texto que describe los ejes.
# - Leyenda (Legend): Explica los elementos del gráfico.
# - Título (Title): Describe el propósito del gráfico.

# --- 4: Enfoques para Crear Gráficos - Funciones Pyplot ---
# Este enfoque es sencillo y diseñado para crear gráficos rápidamente con funciones simples.
# Es ideal para visualizaciones rápidas sin necesidad de configurar detalles avanzados.

print("\n--- Ejemplo de Gráfico de Línea con Funciones Pyplot ---") # Marcador para la ejecución

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico de línea
plt.plot(x, y) #

# Agregar título y etiquetas a los ejes
plt.title('Gráfico de Línea') #
plt.xlabel('Eje X') #
plt.ylabel('Eje Y') #

# Mostrar el gráfico en la pantalla
plt.show() #

# Explicación del ejemplo Pyplot:
# La función **plt.plot(x, y)** crea una línea conectando los puntos definidos por las listas `x` e `y`.
# **plt.title()**, **plt.xlabel()**, y **plt.ylabel()** permiten añadir el título y las etiquetas a los ejes X e Y respectivamente.
# **plt.show()** muestra el gráfico en la pantalla.

# --- 5: Enfoques para Crear Gráficos - Modelo Orientado a Objetos ---
# Este modelo ofrece más **control y flexibilidad** trabajando directamente con objetos **Figure y Axes**.
# Permite un manejo más explícito de cada componente del gráfico.

print("\n--- Ejemplo de Gráfico de Línea con Modelo Orientado a Objetos (OO) ---") # Marcador para la ejecución

# Crear una figura y un conjunto de ejes (el lienzo y el área de dibujo)
fig, ax = plt.subplots() #

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Dibujar la línea en los ejes utilizando el objeto 'ax'
ax.plot(x, y) #

# Agregar título y etiquetas utilizando métodos del objeto Axes
ax.set_title('Gráfico de Línea') #
ax.set_xlabel('Eje X') #
ax.set_ylabel('Eje Y') #

# Mostrar el gráfico
plt.show() #

# Explicación del ejemplo OO:
# Se crea un objeto **Figure** (`fig`) y un conjunto de ejes **Axes** (`ax`) utilizando **plt.subplots()**.
# Los métodos del objeto `ax` (como **ax.set_title()**, **ax.set_xlabel()**, **ax.set_ylabel()**, y **ax.plot()**) se utilizan para agregar elementos como el título y las etiquetas de los ejes, así como para dibujar la línea.

# --- 6: Figuras, Subgráficos y Personalización (conceptos) ---
# Figuras y Subgráficos:
# Permiten crear múltiples gráficos en una sola figura usando **plt.subplots()**.
# Es útil para comparar diferentes visualizaciones en una sola vista.

# Opciones de Personalización adicionales:
# 1. Posición y Tamaño: Se puede ajustar el tamaño de la figura con el parámetro **figsize** y modificar el espacio entre subgráficos con **subplots_adjust()**, controlando la presentación visual.
# 2. Colores, Marcadores y Estilos: Permite la personalización mediante diferentes colores, tipos de marcadores y estilos de línea para crear gráficos visualmente atractivos y adecuados a las necesidades.
# 3. Ticks, Etiquetas y Leyendas: Permite la personalización de las marcas en los ejes (**Ticks**), las etiquetas de los ejes y las leyendas para mejorar la interpretación de los datos presentados.

# --- 7: Técnicas Avanzadas de Personalización ---
# 1. Fijando Límites:
#    Establecer límites para los ejes X e Y usando **set_xlim()** y **set_ylim()** permite controlar el rango de valores mostrados, enfocando la visualización en áreas específicas de interés.
# 2. Anotaciones y Dibujos:
#    Permite añadir anotaciones y formas como líneas, círculos o rectángulos para resaltar información importante.
#    La función **annotate()** permite colocar texto con flechas señalando puntos específicos en el gráfico.
# 3. Guardando Gráficos:
#    Los gráficos pueden guardarse en varios formatos de imagen (como PNG, PDF, SVG) usando la función **savefig()**.
#    Esto facilita su uso en informes o presentaciones.
#    Ejemplo de cómo guardar un gráfico: **plt.savefig('nombre_del_grafico.png')**.

# --- 8: Tipos de Gráficos en Análisis de Datos ---
# (Nota: La fuente original etiqueta esta sección como "Tipos de Variables en Análisis de Datos", pero el contenido describe tipos de gráficos ofrecidos por Matplotlib).
# Matplotlib ofrece una amplia variedad de tipos de gráficos para diferentes necesidades de visualización:
# - **Diagramas de línea** para mostrar tendencias temporales.
# - **Histogramas** para visualizar distribuciones de datos.
# - **Boxplots** para resumir estadísticas de conjuntos de datos.
# - **Diagramas de dispersión** (scatter plots) para identificar correlaciones entre variables.
# - **Gráficos de barras** para comparar datos categóricos.
# - **Diagramas de torta** (pie charts) para representar proporciones.

# --- Ejemplos de Tipos de Gráficos en Matplotlib ---
import numpy as np

# Ejemplo: Diagrama de Línea
x = np.arange(1, 11)
y = np.random.randint(10, 50, size=10)
plt.figure()
plt.plot(x, y, marker='o')
plt.title('Diagrama de Línea')
plt.xlabel('Día')
plt.ylabel('Valor')
plt.show()

# Ejemplo: Histograma
np.random.seed(0)
datos = np.random.normal(50, 10, 200)
plt.figure()
plt.hist(datos, bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de Distribución')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# Ejemplo: Boxplot
np.random.seed(1)
datos_box = [np.random.normal(40, 5, 100), np.random.normal(55, 8, 100)]
plt.figure()
plt.boxplot(datos_box, labels=['Grupo 1', 'Grupo 2'])
plt.title('Boxplot de Grupos')
plt.ylabel('Valor')
plt.show()

# Ejemplo: Diagrama de Dispersión (Scatter Plot)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)
plt.figure()
plt.scatter(x, y, color='purple', alpha=0.7)
plt.title('Diagrama de Dispersión')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()

# Ejemplo: Gráfico de Barras
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 12, 36]
plt.figure()
plt.bar(categorias, valores, color='orange')
plt.title('Gráfico de Barras')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.show()

# Ejemplo: Diagrama de Torta (Pie Chart)
etiquetas = ['Manzanas', 'Bananas', 'Peras', 'Uvas']
porcentajes = [30, 25, 25, 20]
plt.figure()
plt.pie(porcentajes, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta')
plt.axis('equal')
plt.show()

# --- 9: Ejemplo Gráfico de Líneas Personalizado ---
# Objetivo de la actividad: Crear un Gráfico de Líneas con Etiquetas Personalizadas y una Leyenda.
# Requerimientos detallados para esta actividad práctica:
# 1. Importar las Librerías necesarias.
# 2. Crear un Conjunto de Datos.
# 3. Crear el Gráfico de Líneas.
# 4. Personalizar las Etiquetas de los Ejes (X e Y).
# 5. Añadir un Título al gráfico.
# 6. Añadir una Leyenda para explicar los elementos del gráfico.
# 7. Personalizar la apariencia de la Línea (ej. color, estilo, grosor).
# 8. Ajustar los Ticks del Eje X (las marcas y etiquetas en el eje X).
# 9. Guardar el Gráfico en un archivo.
# El detalle completo de esta actividad se encuentra en la guía de estudio de la sesión.

# --- Ejemplo Gráfico de Líneas Personalizado ---

# 1. Importar las Librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# 2. Crear un Conjunto de Datos
# Simulamos datos de temperatura promedio mensual de una ciudad
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
temperatura_2023 = [22, 23, 25, 28, 30, 32, 33, 32, 30, 27, 24, 22]
temperatura_2024 = [21, 22, 24, 27, 29, 31, 32, 31, 29, 26, 23, 21]

# 3. Crear el Gráfico de Líneas
plt.figure(figsize=(10, 6))
plt.plot(meses, temperatura_2023, label='2023', color='red', linestyle='-', linewidth=2, marker='o')
plt.plot(meses, temperatura_2024, label='2024', color='blue', linestyle='--', linewidth=2, marker='s')

# 4. Personalizar las Etiquetas de los Ejes (X e Y)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Temperatura Promedio (°C)', fontsize=12)

# 5. Añadir un Título al gráfico
plt.title('Temperatura Promedio Mensual (2023 vs 2024)', fontsize=14)

# 6. Añadir una Leyenda para explicar los elementos del gráfico
plt.legend(title='Año', loc='upper right')

# 7. Personalizar la apariencia de la Línea (ya realizado en el paso 3)

# 8. Ajustar los Ticks del Eje X (rotar etiquetas para mejor visualización)
plt.xticks(meses, rotation=45)

# 9. Guardar el Gráfico en un archivo
plt.tight_layout()
plt.savefig('grafico_temperatura_mensual.png', dpi=120)

# Mostrar el gráfico en pantalla
plt.show()