import random

# Definición del problema CSP (ejemplo)
variables = ['A', 'B', 'C']
dominios = {v: [1, 2, 3] for v in variables}
restricciones = [('A', 'B'), ('B', 'C')]  # Ejemplo de restricciones: A y B no pueden tener el mismo valor, B y C tampoco.

# Función para contar los conflictos
def contar_conflictos(asignacion):
    conflictos = 0
    for var1, var2 in restricciones:
        if asignacion[var1] == asignacion[var2]:
            conflictos += 1
    return conflictos

# Algoritmo de Búsqueda Local Mínimos-Conflictos
def minimos_conflictos(variables, dominios, restricciones, max_iter):
    # Inicialización aleatoria de la asignación
    asignacion = {var: random.choice(dominios[var]) for var in variables}
    for _ in range(max_iter):
        conflictos = contar_conflictos(asignacion)
        if conflictos == 0:  # Si no hay conflictos, se encontró una solución
            return asignacion
        # Selección aleatoria de una variable en conflicto
        var_conflicto = random.choice([var for var in variables if contar_conflictos({var: asignacion[var]}) > 0])
        # Selección del valor que minimiza los conflictos para la variable en conflicto
        valores_min_conflictos = []
        min_conflictos = float('inf')
        for valor in dominios[var_conflicto]:
            asignacion[var_conflicto] = valor
            conflictos = contar_conflictos(asignacion)
            if conflictos < min_conflictos:
                valores_min_conflictos = [valor]
                min_conflictos = conflictos
            elif conflictos == min_conflictos:
                valores_min_conflictos.append(valor)
        # Asignación aleatoria de uno de los valores que minimizan los conflictos
        asignacion[var_conflicto] = random.choice(valores_min_conflictos)
    return None  # No se encontró una solución en el número máximo de iteraciones

# Resolución del problema CSP con Búsqueda Local Mínimos-Conflictos
solucion = minimos_conflictos(variables, dominios, restricciones, max_iter=1000)

# Resultado
if solucion is not None:
    print("Asignación encontrada:")
    print(solucion)
else:
    print("No se encontró solución en el número máximo de iteraciones.")
