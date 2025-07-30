import numpy as np 
import pandas as pd 
import yfinance as yf 
import matplotlib.pyplot as plt 
import tensorflow as tf from tensorflow 
import keras from tensorflow.keras.models 
import Sequential from tensorflow.keras.layers 
import LSTM, Dense, Dropout from sklearn.preprocessing 
import MinMaxScaler 
import time

Función para descargar datos con reintentos

def obtener_datos(ticker, start_date, end_date): intentos = 5  # Intentar 5 veces si hay bloqueo for intento in range(intentos): try: df = yf.download(ticker, start=start_date, end=end_date, progress=False) if not df.empty: return df  # Si los datos se descargaron, regresarlos except Exception as e: print(f"Error al descargar datos: {e}")

print(f"Reintentando en 30 segundos... ({intento + 1}/{intentos})")
    time.sleep(30)  # Esperar antes de reintentar

raise Exception("No se pudieron descargar los datos después de varios intentos.")

Descargar datos de Bitcoin

start_date = '2010-01-01' end_date = '2025-03-01' btc_data = obtener_datos('BTC-USD', start_date, end_date)

print("Datos descargados correctamente:") print(btc_data.head())

Preprocesamiento de datos

scaler = MinMaxScaler(feature_range=(0, 1)) btc_data_scaled = scaler.fit_transform(btc_data[['Close']])

Crear secuencias de datos para entrenamiento

def create_sequences(data, seq_length): sequences = [] labels = [] for i in range(len(data) - seq_length): sequences.append(data[i:i+seq_length]) labels.append(data[i+seq_length]) return np.array(sequences), np.array(labels)

seq_length = 60  # Usaremos 60 días como ventana de predicción X, y = create_sequences(btc_data_scaled, seq_length)

Dividir en entrenamiento y prueba

train_size = int(len(X) * 0.8) X_train, X_test = X[:train_size], X[train_size:] y_train, y_test = y[:train_size], y[train_size:]

Construcción del modelo LSTM

model = Sequential([ LSTM(100, return_sequences=True, input_shape=(seq_length, 1)), Dropout(0.2), LSTM(100, return_sequences=True), Dropout(0.2), LSTM(100), Dropout(0.2), Dense(1) ])

model.compile(optimizer='adam', loss='mean_squared_error')

Entrenamiento del modelo

history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

Predicciones

predictions = model.predict(X_test) predictions = scaler.inverse_transform(predictions) y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

Visualización de predicciones solo un mes después de la última fecha disponible

future_days = 30 plt.figure(figsize=(12, 6)) plt.plot(range(len(y_test_actual), len(y_test_actual) + future_days), predictions[-future_days:], label='Predicción') plt.legend() plt.title('Predicción del precio de Bitcoin para el próximo mes') plt.show()

