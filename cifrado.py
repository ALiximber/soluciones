
def cifrar(texto, clave):
    return ''.join(chr(ord(c)+clave) for c in texto)

def descifrar(texto, clave):
    return ''.join(chr(ord(c)-clave) for c in texto)

op = input("Cifrar o Descifrar (c/d): ")
t = input("Texto: ")
k = int(input("Clave (int): "))
print(cifrar(t,k) if op == 'c' else descifrar(t,k))
