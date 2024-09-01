# Definir la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

# Valor a buscar
valor_buscado = 5

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    fila, columna = resultado
    print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna})")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz")

# Imprimir la matriz para referencia
print("\nMatriz:")
for fila in matriz:
    print(fila)