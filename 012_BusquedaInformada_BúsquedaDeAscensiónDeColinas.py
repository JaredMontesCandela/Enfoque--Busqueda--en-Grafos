import random # Importamos el módulo random para poder generar números aleatorios, que usaremos para crear los vecinos.

# Supongamos que estamos resolviendo un problema simple de encontrar el máximo de una función cuadrática
# La función cuadrática será f(x) = -(x-3)^2 + 9, que tiene un máximo en x=3

# Definimos la función heurística como el valor negativo de la función cuadrática
def funcion_heuristica(x):
    return -(x-3)**2 + 9

# La función para generar sucesores crea dos vecinos cercanos al estado actual
def generar_sucesores(x):
    return [x - random.uniform(0, 1), x + random.uniform(0, 1)]

# Implementación del algoritmo de Búsqueda de Ascensión de Colinas
def ascension_de_colinas(estado_inicial, funcion_heuristica, generar_sucesores):
    estado_actual = estado_inicial
    while True:
        vecinos = generar_sucesores(estado_actual)
        mejor_vecino = max(vecinos, key=lambda x: funcion_heuristica(x))

        if funcion_heuristica(mejor_vecino) <= funcion_heuristica(estado_actual):
            # No se encontró un mejor vecino
            return estado_actual

        # Actualizamos el estado actual al mejor vecino encontrado
        estado_actual = mejor_vecino

# Estado inicial aleatorio entre 0 y 6
estado_inicial = random.uniform(0, 6)

# Ejecutamos la búsqueda y mostramos el resultado
resultado = ascension_de_colinas(estado_inicial, funcion_heuristica, generar_sucesores)
print("Estado inicial:", estado_inicial)
print("Resultado de la búsqueda:", resultado)
print("Valor heurístico del resultado:", funcion_heuristica(resultado))
