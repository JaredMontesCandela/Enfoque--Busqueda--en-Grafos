import random

"""
definimos un entorno de cuadrícula con un tamaño específico y una celda 
objetivo. Luego, implementamos el método de iteración de política para encontrar la política
óptima que indica la acción óptima a tomar en cada estado para alcanzar la meta.
"""

# Definir el tamaño de la cuadrícula y la posición de la meta
tamaño_cuadricula = (4, 4)
meta = (3, 3)
num_acciones = 4  # Arriba, abajo, izquierda, derecha

# Inicializar la función de valor de estado y la política
funcion_valor_estado = [[0] * tamaño_cuadricula[1] for _ in range(tamaño_cuadricula[0])]
politica = [[0] * tamaño_cuadricula[1] for _ in range(tamaño_cuadricula[0])]

# Función para realizar una acción en el entorno de cuadrícula
def tomar_accion(estado, accion):
    if accion == 0:  # Arriba
        return max(0, estado[0] - 1), estado[1]
    elif accion == 1:  # Abajo
        return min(tamaño_cuadricula[0] - 1, estado[0] + 1), estado[1]
    elif accion == 2:  # Izquierda
        return estado[0], max(0, estado[1] - 1)
    elif accion == 3:  # Derecha
        return estado[0], min(tamaño_cuadricula[1] - 1, estado[1] + 1)

# Función para realizar la búsqueda de política
def busqueda_de_politica(funcion_valor_estado, politica, meta, num_acciones, max_iteraciones=100):
    for _ in range(max_iteraciones):
        # Evaluación de política: calcular la función de valor de estado para la política actual
        for i in range(tamaño_cuadricula[0]):
            for j in range(tamaño_cuadricula[1]):
                if (i, j) == meta:
                    funcion_valor_estado[i][j] = 0  # Valor de la meta
                else:
                    accion = politica[i][j]
                    siguiente_estado = tomar_accion((i, j), accion)
                    recompensa = -1  # Recompensa por movimiento
                    funcion_valor_estado[i][j] = recompensa + funcion_valor_estado[siguiente_estado[0]][siguiente_estado[1]]

        # Mejora de política: actualizar la política basada en la función de valor de estado actualizada
        for i in range(tamaño_cuadricula[0]):
            for j in range(tamaño_cuadricula[1]):
                if (i, j) != meta:
                    valores_accion = []
                    for accion in range(num_acciones):
                        siguiente_estado = tomar_accion((i, j), accion)
                        valores_accion.append(funcion_valor_estado[siguiente_estado[0]][siguiente_estado[1]])
                    mejor_accion = valores_accion.index(max(valores_accion))
                    politica[i][j] = mejor_accion

    return politica

# Ejecutar la búsqueda de política
politica = busqueda_de_politica(funcion_valor_estado, politica, meta, num_acciones)

# Imprimir la política resultante
print("Política óptima:")
for fila in politica:
    print(fila)
