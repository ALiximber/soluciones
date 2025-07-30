def busqueda_binaria(arr, objetivo):
    izq, der = 0, len(arr)-1
    while izq <= der:
        mid = (izq + der) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1
