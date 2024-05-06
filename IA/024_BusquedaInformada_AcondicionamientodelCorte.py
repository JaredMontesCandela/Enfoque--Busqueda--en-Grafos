# Definir una función para la multiplicación de matrices
def matriz_mult(A, B):
    # Verificar si las matrices son compatibles para la multiplicación
    if len(A[0]) != len(B):
        print("No se pueden multiplicar las matrices: dimensiones incompatibles")
        return None
    
    # Inicializar una lista vacía para almacenar el resultado de la multiplicación
    result = []
    
    # Iterar sobre cada fila de la primera matriz
    for i in range(len(A)):
        # Inicializar una lista vacía para almacenar la fila resultante
        fila_resultado = []
        # Iterar sobre cada columna de la segunda matriz
        for j in range(len(B[0])):
            # Inicializar la suma para el elemento (i, j) de la matriz resultante
            suma = 0
            # Iterar sobre los elementos de la fila i de la primera matriz y la columna j de la segunda matriz
            for k in range(len(B)):
                # Calcular el producto de los elementos correspondientes y sumarlos a la suma
                suma += A[i][k] * B[k][j]
            # Agregar el resultado de la suma a la fila resultante
            fila_resultado.append(suma)
        # Agregar la fila resultante a la matriz resultante
        result.append(fila_resultado)
    
    # Devolver la matriz resultante
    return result

# Ejemplo de uso de la función de multiplicación de matrices
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

resultado = matriz_mult(A, B)
if resultado:
    # Imprimir la matriz resultante si se calcula con éxito
    print("Resultado de la multiplicación de matrices:")
    for fila in resultado:
        print(fila)
