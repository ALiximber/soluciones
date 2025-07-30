import os, hashlib

def hash_archivo(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def encontrar_duplicados(carpeta):
    hashes = {}
    for raiz, _, archivos in os.walk(carpeta):
        for a in archivos:
            ruta = os.path.join(raiz, a)
            h = hash_archivo(ruta)
            if h in hashes:
                print(f"Duplicado encontrado: {ruta} y {hashes[h]}")
            else:
                hashes[h] = ruta

encontrar_duplicados(".")
