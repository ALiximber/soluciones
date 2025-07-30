

import scapy.all as scapy from sklearn.ensemble import IsolationForest import pandas as pd import numpy as np import threading import time import joblib import os

Ruta del modelo entrenado (se carga si ya existe)

MODEL_PATH = "ids_model.pkl"

Lista para almacenar datos de red

packet_data = []

Características a extraer de cada paquete

def extract_features(packet): return { "packet_length": len(packet), "src_port": packet[scapy.TCP].sport if packet.haslayer(scapy.TCP) else 0, "dst_port": packet[scapy.TCP].dport if packet.haslayer(scapy.TCP) else 0, "proto": packet.proto if hasattr(packet, 'proto') else 0 }

Función para guardar logs

def log_event(event): with open("ids_log.txt", "a") as f: f.write(f"{time.ctime()} - {event}\n")

Función que se ejecuta al capturar paquetes

def process_packet(packet): try: if packet.haslayer(scapy.IP): feat = extract_features(packet) feat_df = pd.DataFrame([feat]) prediction = model.predict(feat_df)[0]

if prediction == -1:
            msg = f"[ALERTA] Posible tráfico malicioso desde {packet[scapy.IP].src}"
            print(msg)
            log_event(msg)
except Exception as e:
    print("[ERROR]", e)

Entrenamiento básico si no existe el modelo

if not os.path.exists(MODEL_PATH): print("[INFO] Entrenando modelo IDS...") # Dataset sintético simple para ejemplo normal_data = pd.DataFrame({ "packet_length": np.random.normal(150, 50, 1000), "src_port": np.random.randint(1000, 50000, 1000), "dst_port": np.random.randint(20, 10000, 1000), "proto": np.random.choice([6, 17], 1000)  # TCP, UDP })

clf = IsolationForest(contamination=0.05)
clf.fit(normal_data)
joblib.dump(clf, MODEL_PATH)
print("[INFO] Modelo entrenado y guardado.")

Cargar modelo entrenado

model = joblib.load(MODEL_PATH) print("[INFO] Modelo IDS cargado correctamente.")

Iniciar sniffing

print("[INFO] Capturando tráfico de red (presiona Ctrl+C para detener)...") try: scapy.sniff(prn=process_packet, store=0) except KeyboardInterrupt: print("\n[INFO] Detección finalizada.")

