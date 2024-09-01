def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenar_fila(matriz, fila):
    matriz[fila] = bubble_sort(matriz[fila])
    return matriz

# Definir la matriz
matriz = [
    [9, 2, 7],
    [6, 1, 8],
    [5, 4, 3]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (0-indexed)
fila_a_ordenar = 1

# Ordenar la fila especificada
matriz_ordenada = ordenar_fila(matriz.copy(), fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
for fila in matriz_ordenada:
    print(fila)