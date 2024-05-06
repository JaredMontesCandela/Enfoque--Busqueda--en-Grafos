import heapq
import random

# Función de evaluación: esta función evalúa qué tan buena es una solución
# en el contexto del problema. Debe devolver un valor numérico que represente
# la calidad de la solución.
def evaluar(solucion):
    # En este ejemplo simple, la función de evaluación devuelve la suma de los valores
    return sum(solucion)

# Función para generar una solución aleatoria
def generar_solucion(n):
    # Generamos una lista de n números aleatorios entre 0 y 100
    return [random.randint(0, 100) for _ in range(n)]

# Función para generar vecinos de una solución dada
def generar_vecinos(solucion):
    vecinos = []
    for _ in range(5):  # Generamos 5 vecinos en cada iteración
        indice = random.randint(0, len(solucion) - 1)  # Seleccionamos un índice aleatorio
        vecino = solucion[:]  # Creamos una copia de la solución actual
        vecino[indice] += random.choice([-1, 1])  # Modificamos el valor en el índice seleccionado
        vecinos.append(vecino)
    return vecinos

# Algoritmo de búsqueda online beam search
def online_beam_search(n, k, max_iter):
    # Inicializamos el conjunto de soluciones con una solución aleatoria
    soluciones = [generar_solucion(n) for _ in range(k)]

    for _ in range(max_iter):
        nuevos_soluciones = []
        for solucion in soluciones:
            # Generamos k vecinos para cada solución
            vecinos = generar_vecinos(solucion)
            # Evaluamos los vecinos y los añadimos al conjunto de soluciones
            nuevos_soluciones.extend(vecinos)

        # Ordenamos las soluciones según su evaluación
        soluciones = heapq.nlargest(k, nuevos_soluciones, key=evaluar)

    # Seleccionamos la mejor solución
    mejor_solucion = max(soluciones, key=evaluar)
    mejor_puntaje = evaluar(mejor_solucion)

    return mejor_solucion, mejor_puntaje

# Parámetros
dimension_problema = 5  # Dimensión del problema, por ejemplo, número de variables
beam_width = 3  # Ancho del haz
iteraciones_maximas = 1000  # Número máximo de iteraciones

# Ejecución del algoritmo
mejor_solucion, mejor_puntaje = online_beam_search(dimension_problema, beam_width, iteraciones_maximas)

# Resultados
print("La mejor solución encontrada es:", mejor_solucion)
print("Con un puntaje de evaluación de:", mejor_puntaje)
