# Definición de las opciones de trabajo con sus respectivos salarios y niveles de satisfacción
opciones_trabajo = [
    {"nombre": "Trabajo A", "salario": 3000, "satisfaccion": 8},
    {"nombre": "Trabajo B", "salario": 4000, "satisfaccion": 7},
    {"nombre": "Trabajo C", "salario": 5000, "satisfaccion": 6}
]

# Función de utilidad que calcula la utilidad total para cada opción de trabajo
def calcular_utilidad(opcion):
    return opcion["salario"] + opcion["satisfaccion"]

# Función para encontrar la mejor opción de trabajo basada en la utilidad
def encontrar_mejor_opcion(opciones):
    mejor_opcion = None
    mejor_utilidad = float("-inf")
    for opcion in opciones:
        utilidad = calcular_utilidad(opcion)
        if utilidad > mejor_utilidad:
            mejor_opcion = opcion
            mejor_utilidad = utilidad
    return mejor_opcion

# Ejemplo de uso: encontrar la mejor opción de trabajo
mejor_opcion_trabajo = encontrar_mejor_opcion(opciones_trabajo)

# Resultado
if mejor_opcion_trabajo:
    print("La mejor opción de trabajo es:", mejor_opcion_trabajo["nombre"])
    print("Salario:", mejor_opcion_trabajo["salario"])
    print("Nivel de satisfacción:", mejor_opcion_trabajo["satisfaccion"])
    print("Utilidad total:", calcular_utilidad(mejor_opcion_trabajo))
else:
    print("No se encontró la mejor opción de trabajo.")
