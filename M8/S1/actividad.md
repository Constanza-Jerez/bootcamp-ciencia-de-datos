# 1. PARTE 1

### p1: 
 - Sistema de capas, con procesamiento en cada una de ellas, con entrnamiento secuencial, se activan mediante el peso o relevancia de cada una, el sesgo permite desplazar la función de activación

### p2: 
- **Perceptrón:** Unidad básica de una red neuronal artificial.
- **Capas:** Entrada, ocultas y salida. Cada capa procesa la información y la transmite a la siguiente.
- **Función de activación:** Introduce no linealidad. Ejemplos: Sigmoide, ReLU, Tangente hiperbólica, Softmax.
- **Pesos y sesgos:** Los pesos determinan la importancia de cada conexión y los sesgos permiten desplazar la función de activación.

# 2. PARTE 2

### p3:
- Los atributos del cliente pueden influir en la predicción, no tenemos datos estructurados o secuenciales.

### p4:
- Dependiendo los datos de entrada, supongamos 5 atributos, tendriamos 5 nodos por atributos del cliente
- capaz ocultas, 1-2,  con 8-16 neuronas
- función de activación ReLu
- capa de salida, 1 neurona con función sigmoide para predición probabilidad de compra

```
Capa de Entrada: Tantas neuronas como características tengamos. Si hay 10 datos por cliente, serán 10 neuronas.
Capas Ocultas: Comenzar con dos capas ocultas. La primera, más ancha (ej. 32 neuronas), para captar patrones generales, y la segunda, más pequeña (ej. 16 neuronas), para refinar esos patrones.
Funciones de Activación:
En capas ocultas: ReLU. Es como un interruptor eficiente que ayuda a la red a aprender rápido.
En la capa de salida: Sigmoid. Transforma el resultado final en una probabilidad (un número entre 0 y 1), que es exactamente lo que necesitamos.
```
``` python
# Así se vería en código (Python/Keras):
# Suponiendo 10 características de entrada
model = keras.Sequential([
    # 1ra Capa Oculta con función de activación ReLU
    keras.layers.Dense(32, activation='relu', input_shape=(10,)),
    
    # 2da Capa Oculta con función de activación ReLU
    keras.layers.Dense(16, activation='relu'),
    
    # Capa de Salida con función Sigmoid para probabilidad
    keras.layers.Dense(1, activation='sigmoid')
])
```


# 3. PARTE 3

### p5:
- - **Loss function:** Mide el error entre la predicción y el valor real, servirá para el analisis, ya que al ajustar el peso para cada neurona mediante la medición de error, ajusta la calidad de salida del modelo

### p6:
- - **Forward pass:** Los datos pasan por las capas, se aplican pesos, sesgos y funciones de activación, y se obtiene la predicción.
- **Backpropagation:** El error se retropropaga y los pesos se ajustan para minimizar la función de pérdida.

# 4. PARTE 4

### p7:
- Exactitud (accuracy): proporción de predicciones correctas sobre el total.
- classification_report: muestra precisión, recall y F1-score por clase.
- Matriz de confusión: muestra los aciertos y errores por clase.
- Balanced Accuracy: útil si las clases están desbalanceadas.
- Cohen Kappa: mide el acuerdo entre predicción y verdad, corrigiendo el azar.
- Matthews Correlation Coefficient: métrica robusta para clasificación multiclase.
- Log Loss: penaliza las predicciones menos seguras, útil para modelos probabilísticos.
- ROC CURVE
- AUC ROC CURVE

### p8:
- Ajustar el número de capas/neuronas
- Cambiar la función de activación
- Ajustar hiperparametros o parametros del entrenamiento(tasa o frecuencia de entrenamiento, regularización, iteraciones...)
- Cambiar función de perdida
- Verificar y mejorar tratamiento de datos

# 5. PARTE 5

#### p9: