import random

# Función de evaluación: esta función evalúa qué tan buena es una solución
# en el contexto del problema. Debe devolver un valor numérico que represente
# la calidad de la solución.
def evaluar(solucion):
    # En este ejemplo simple, la función de evaluación devuelve la suma de los valores
    return sum(solucion)

# Función para generar una población inicial aleatoria
def generar_poblacion(tam_poblacion, tam_genoma):
    return [[random.randint(0, 1) for _ in range(tam_genoma)] for _ in range(tam_poblacion)]

# Función de cruzamiento de un punto entre dos individuos
def cruzamiento(individuo1, individuo2):
    punto_cruzamiento = random.randint(1, len(individuo1) - 1)
    hijo1 = individuo1[:punto_cruzamiento] + individuo2[punto_cruzamiento:]
    hijo2 = individuo2[:punto_cruzamiento] + individuo1[punto_cruzamiento:]
    return hijo1, hijo2

# Función de mutación
def mutacion(individuo, tasa_mutacion):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i]  # Cambiar de 0 a 1 o de 1 a 0
    return individuo

# Algoritmo genético
def algoritmo_genetico(tam_poblacion, tam_genoma, tasa_mutacion, max_generaciones):
    poblacion = generar_poblacion(tam_poblacion, tam_genoma)

    for _ in range(max_generaciones):
        # Evaluación de la población
        evaluaciones = [(individuo, evaluar(individuo)) for individuo in poblacion]
        mejor_individuo, mejor_puntaje = max(evaluaciones, key=lambda x: x[1])

        # Selección de padres (torneo binario)
        padres = []
        for _ in range(tam_poblacion):
            torneo = random.sample(evaluaciones, 2)
            ganador = max(torneo, key=lambda x: x[1])[0]
            padres.append(ganador)

        # Cruzamiento y mutación
        descendencia = []
        for i in range(0, tam_poblacion, 2):
            hijo1, hijo2 = cruzamiento(padres[i], padres[i + 1])
            hijo1 = mutacion(hijo1, tasa_mutacion)
            hijo2 = mutacion(hijo2, tasa_mutacion)
            descendencia.extend([hijo1, hijo2])

        poblacion = descendencia

    return mejor_individuo, mejor_puntaje

# Parámetros
tam_poblacion = 100
tam_genoma = 10
tasa_mutacion = 0.1
max_generaciones = 1000

# Ejecución del algoritmo genético
mejor_solucion, mejor_puntaje = algoritmo_genetico(tam_poblacion, tam_genoma, tasa_mutacion, max_generaciones)

# Resultados
print("La mejor solución encontrada es:", mejor_solucion)
print("Con un puntaje de evaluación de:", mejor_puntaje)
