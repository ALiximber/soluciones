import random
import string

def generar(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

if __name__ == '__main__':
    l = int(input("Longitud de contraseña: "))
    print(generar(l))
