def longitud_max_subcadena(s):
    chars = set()
    izq = max_len = 0
    for der in range(len(s)):
        while s[der] in chars:
            chars.remove(s[izq])
            izq += 1
        chars.add(s[der])
        max_len = max(max_len, der - izq + 1)
    return max_len
