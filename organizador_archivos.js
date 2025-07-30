import os
import shutil
import argparse

def organizar_por_extension(carpeta):
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta):
            ext = archivo.split('.')[-1].lower()
            destino = os.path.join(carpeta, ext)
            os.makedirs(destino, exist_ok=True)
            shutil.move(ruta, os.path.join(destino, archivo))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', required=True, help='Ruta de carpeta a organizar')
    args = parser.parse_args()
    organizar_por_extension(args.src)
