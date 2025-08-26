import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
from matplotlib import pyplot as plt

# Cargar el dataset desde OpenML
data = fetch_openml(name="diabetes", version=1, as_frame=True)
df = data.frame

# Ver las primeras filas del dataset
print(df.head())


# Separar características (X) y variable objetivo (y) según las columnas reales
# El dataset tiene columnas: preg, plas, pres, skin, insu, mass, pedi, age, class
# La variable objetivo es 'class', las características son el resto
X = df.drop(columns=["class"])
y = (df["class"] == "tested_positive").astype(int)  # 1=diabetes, 0=no diabetes


# Dividir en conjuntos de entrenamiento (80%) y prueba (20%)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos para mejorar el rendimiento del modelo
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Definir la estructura del modelo
modelo = Sequential([
Dense(16, activation='relu', input_shape=(x_train.shape[1],)),
Dropout(0.3),
Dense(8, activation='relu'),
Dense(1, activation='sigmoid') # Capa de salida para clasificación binaria

])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Ver resumen del modelo
modelo.summary()

# Entrenar el modelo
historial = modelo.fit(x_train, y_train, epochs=50, batch_size=16, validation_data=(x_test, y_test))

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = modelo.evaluate(x_test, y_test)
print(f"Precisión del modelo en datos de prueba: {accuracy:.4f}")

# Crear datos de un nuevo paciente (simulación)
nuevo_paciente = np.array([[2, 120, 70, 32, 85, 25.5, 0.67, 45]])
nuevo_paciente = scaler.transform(nuevo_paciente) # Aplicar la misma normalización

# Hacer la predicción
probabilidad = modelo.predict(nuevo_paciente)[0][0]
print(f"Probabilidad de tener diabetes: {probabilidad :.2%}")

# Gráfica de la pérdida
plt.plot(historial.history['loss'], label='Pérdida en entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida en validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

# Gráfica de la precisión
plt.plot(historial.history['accuracy'], label='Precisión en entrenamiento')
plt.plot(historial.history['val_accuracy'], label='Precisión en validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend ()
plt.show()