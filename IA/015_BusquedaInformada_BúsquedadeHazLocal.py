import random

# Función de evaluación: esta función evalúa qué tan buena es una solución
# en el contexto del problema. Debe devolver un valor numérico que represente
# la calidad de la solución.
def evaluar(solucion):
    # En este ejemplo simple, la función de evaluación devuelve la suma de los valores
    return sum(solucion)

# Función para generar una solución aleatoria inicial
def generar_solucion(n):
    # Generamos una lista de n números aleatorios entre 0 y 100
    return [random.randint(0, 100) for _ in range(n)]

# Función para encontrar la mejor solución local dado un punto inicial
def buscar_vecino(solucion):
    # Generamos una solución vecina haciendo un pequeño cambio en la solución actual
    indice = random.randint(0, len(solucion) - 1) # Seleccionamos un índice aleatorio
    vecino = solucion[:]  # Creamos una copia de la solución actual
    vecino[indice] += random.choice([-1, 1])  # Modificamos el valor en el índice seleccionado

    return vecino

# Algoritmo de búsqueda de haz local
def hill_climbing(n, max_iter):
    # Generamos una solución inicial aleatoria
    solucion_actual = generar_solucion(n)
    # Evaluamos la solución inicial
    mejor_puntaje = evaluar(solucion_actual)

    for _ in range(max_iter):
        # Generamos un vecino de la solución actual
        vecino = buscar_vecino(solucion_actual)
        # Evaluamos el vecino
        puntaje_vecino = evaluar(vecino)

        # Si el vecino es mejor que la solución actual, actualizamos
        # la solución actual y el mejor puntaje
        if puntaje_vecino > mejor_puntaje:
            solucion_actual = vecino
            mejor_puntaje = puntaje_vecino

    return solucion_actual, mejor_puntaje

# Parámetros
dimension_problema = 5  # Dimensión del problema, por ejemplo, número de variables
iteraciones_maximas = 1000  # Número máximo de iteraciones

# Ejecución del algoritmo
mejor_solucion, mejor_puntaje = hill_climbing(dimension_problema, iteraciones_maximas)

# Resultados
print("La mejor solución encontrada es:", mejor_solucion)
print("Con un puntaje de evaluación de:", mejor_puntaje)
