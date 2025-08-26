import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

# Cargar el dataset Iris
data = load_iris()
X = data.data # Características (largo y ancho de los sépalos y pétalos)
y = data.target # Clases (Setosa, Versicolor, Virginica)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convertir las etiquetas a formato "one-hot" (para clasificación multiclase)
y_train = to_categorical(y_train, 3)
y_test = to_categorical(y_test, 3)

# Crear el modelo de la red neuronal
model = Sequential()

# Capa de entrada (4 características de entrada)
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))

# Capa oculta
model.add(Dense(32, activation='relu'))

# Capa de salida (3 neuronas, una para cada clase)
model.add(Dense(3, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[EarlyStopping(monitor='val_loss', patience=10)])

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {accuracy*100 :.2f}%")

# Graficar la precisión y la pérdida durante el entrenamiento
plt.plot(history.history['accuracy'], label='Precision en entrenamiento')
plt.plot(history.history['val_accuracy' ], label='Precision en validacion' )
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Pérdida en entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida en validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

# Realizar predicciones sobre el conjunto de prueba
predictions = model.predict(X_test)

# Mostrar las clases predichas y las clases reales
for i in range(10):
    print(f"Real: {np.argmax(y_test[i])}, Predicción: {np.argmax(predictions[i])}")