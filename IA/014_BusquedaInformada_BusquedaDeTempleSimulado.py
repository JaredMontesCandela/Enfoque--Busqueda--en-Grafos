import random
import math

def temple_simulado(funcion_objetivo, rango_inicial, temperatura_inicial, iteraciones):
    solucion_actual = random.uniform(*rango_inicial)
    mejor_solucion = solucion_actual
    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones):
        solucion_vecina = random.uniform(*rango_inicial)

        delta_energia = funcion_objetivo(solucion_vecina) - funcion_objetivo(solucion_actual)
        probabilidad_aceptacion = math.exp(-delta_energia / temperatura_actual)

        if delta_energia < 0 or random.random() < probabilidad_aceptacion:
            solucion_actual = solucion_vecina

        if funcion_objetivo(solucion_actual) < funcion_objetivo(mejor_solucion):
            mejor_solucion = solucion_actual

        temperatura_actual *= 0.95

    return mejor_solucion

# Ejemplo de uso
def funcion_ejemplo(x):
    return -(x**2) + 10 * x + 25

if __name__ == "__main__":
    rango_inicial = (0, 31)
    temperatura_inicial = 100.0
    iteraciones = 1000

    mejor_solucion_encontrada = temple_simulado(funcion_ejemplo, rango_inicial, temperatura_inicial, iteraciones)
    print("Mejor solución encontrada:", mejor_solucion_encontrada)
