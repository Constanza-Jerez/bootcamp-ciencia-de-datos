from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn. tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn. svm import SVC

# Cargar el conjunto de datos Iris
data = load_iris()
X = pd.DataFrame(data.data, columns=data. feature_names) # Caracteristicas
y = pd. Series (data. target) # Etiquetas

# Mostrar las primeras filas de los datos
print("Características (X):")
print(X.head())

print("\nEtiquetas (y):")
print(y.head())

# Información sobre el conjunto de datos
# print("\nInformación del conjunto de datos:")
# print(data.DESCR)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42)

print(f"\nTamaño del conjunto de entrenamiento: {X_train.shape}")
print(f"Tamaño del conjunto de prueba: {X_test.shape}")

# Crear y entrenar el modelo de regresión logística
modelo_lr = LogisticRegression(max_iter=200, random_state=42)
modelo_lr.fit(X_train, y_train)

# Predecir y evaluar
y_pred_lr = modelo_lr.predict(X_test)
print("\nExactitud de Regresion Logistica:", accuracy_score(y_test,
y_pred_lr))

# Crear y entrenar el modelo de árbol de decisión
modelo_dt = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo_dt.fit(X_train, y_train)

# Predecir y evaluar
y_pred_dt = modelo_dt.predict(X_test)
print("Exactitud de Arbol de Decision:", accuracy_score(y_test, y_pred_dt))

# Crear y entrenar el modelo de bosque aleatorio
modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

# Predecir y evaluar
y_pred_rf = modelo_rf.predict(X_test)

print("Exactitud de Bosque Aleatorio:", accuracy_score(y_test, y_pred_rf))

# Crear y entrenar el modelo SVM
modelo_svm = SVC(kernel="rbf", gamma="scale", random_state=42)
modelo_svm.fit(X_train, y_train)

# Predecir y evaluar
y_pred_svm = modelo_svm.predict(X_test)
print("Exactitud de SVM:", accuracy_score(y_test, y_pred_svm))

print("\nComparación de Exactitud:")
print(f"- Regresión Logística: {accuracy_score(y_test, y_pred_lr) : .4f}")
print(f"- Árbol de Decisión: {accuracy_score(y_test, y_pred_dt) : .4f}")
print(f"- Bosque Aleatorio: {accuracy_score(y_test, y_pred_rf) : .4f}")
print(f"- SVM: {accuracy_score(y_test, y_pred_svm) : .4f}")

# Implementación de la función sigmoidea
def sigmoidea(x):
    return 1 / (1 + np.exp(-x))

# Visualización de la función sigmoidea aplicada a la regresión logística
# Tomamos la salida lineal (decision function) del modelo logístico para el primer test
z = modelo_lr.decision_function(X_test)

plt.figure(figsize=(8, 4))
plt.plot(np.sort(z), sigmoidea(np.sort(z)), label='Sigmoidea aplicada a la salida del modelo', color='purple')
plt.title('Función Sigmoidea sobre la salida de Regresión Logística')
plt.xlabel('z (decision function)')
plt.ylabel('sigmoidea(z)')
plt.grid(True)
plt.legend()
plt.show()

# Visualización mejorada de la función sigmoidea aplicada a la regresión logística
# Visualización mejorada de la función sigmoidea aplicada a la regresión logística (solo clase 0)
z = modelo_lr.decision_function(X_test)
if z.ndim > 1:
    z = z[:, 0]  # Selecciona la salida para la clase 0

z_sorted = np.sort(z)
sig_sorted = sigmoidea(z_sorted)

plt.figure(figsize=(10, 5))
plt.plot(z_sorted, sig_sorted, label='Curva Sigmoidea', color='purple', linewidth=2)
plt.scatter(z, sigmoidea(z), c=(y_test == 0).astype(int), cmap='coolwarm', edgecolor='k', s=60, alpha=0.7, label='Clase 0 (azul=No, rojo=Sí)')
plt.axhline(0.5, color='red', linestyle='--', linewidth=1, label='Umbral de decisión (0.5)')
plt.title('Función Sigmoidea y Probabilidades de Regresión Logística (Iris, clase 0)')
plt.xlabel('z (decision function)')
plt.ylabel('sigmoidea(z) / Probabilidad')
plt.colorbar(label='¿Clase 0?')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Visualización mejorada para cualquier clase (ejemplo: clase 1)
clase = 1  # Cambia a 0, 1 o 2 según la clase que quieras visualizar

z = modelo_lr.decision_function(X_test)
if z.ndim > 1:
    z = z[:, clase]  # Selecciona la salida para la clase deseada

z_sorted = np.sort(z)
sig_sorted = sigmoidea(z_sorted)

plt.figure(figsize=(10, 5))
plt.plot(z_sorted, sig_sorted, label=f'Curva Sigmoidea (Clase {clase})', color='purple', linewidth=2)
plt.scatter(z, sigmoidea(z), c=(y_test == clase).astype(int), cmap='coolwarm', edgecolor='k', s=60, alpha=0.7, label=f'Clase {clase} (azul=No, rojo=Sí)')
plt.axhline(0.5, color='red', linestyle='--', linewidth=1, label='Umbral de decisión (0.5)')
plt.title(f'Función Sigmoidea y Probabilidades de Regresión Logística (Iris, clase {clase})')
plt.xlabel('z (decision function)')
plt.ylabel('sigmoidea(z) / Probabilidad')
plt.colorbar(label=f'¿Clase {clase}?')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Visualización de la función sigmoidea para todas las clases en un solo gráfico
z_all = modelo_lr.decision_function(X_test)
clases = np.unique(y_test)

plt.figure(figsize=(12, 6))
colors = ['blue', 'green', 'orange']
for idx, clase in enumerate(clases):
    z_clase = z_all[:, idx] if z_all.ndim > 1 else z_all
    z_sorted = np.sort(z_clase)
    sig_sorted = sigmoidea(z_sorted)
    plt.plot(z_sorted, sig_sorted, label=f'Curva Sigmoidea (Clase {clase})', color=colors[idx], linewidth=2)
    plt.scatter(z_clase, sigmoidea(z_clase), 
                c=(y_test == clase).astype(int), cmap='coolwarm', 
                edgecolor='k', s=60, alpha=0.5, 
                label=f'Puntos Clase {clase} (azul=No, rojo=Sí)')

plt.axhline(0.5, color='red', linestyle='--', linewidth=1, label='Umbral de decisión (0.5)')
plt.title('Funciones Sigmoideas y Probabilidades de Regresión Logística (Iris, todas las clases)')
plt.xlabel('z (decision function)')
plt.ylabel('sigmoidea(z) / Probabilidad')
plt.legend(loc='best')
plt.tight_layout()
plt.show()