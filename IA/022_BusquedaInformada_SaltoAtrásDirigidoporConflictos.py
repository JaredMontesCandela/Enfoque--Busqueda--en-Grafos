# Implementación del algoritmo de Salto Atrás Dirigido por Conflictos (Conflict-Directed Backjumping, CDB)
# para resolver un problema de asignación de colores a un mapa.

# Definición del problema CSP (Asignación de colores a un mapa con ciertas restricciones)
mapa = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

colores = ['Rojo', 'Verde', 'Azul']

# Función para verificar si una asignación es válida
def es_valida(asignacion, region, color):
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Función de búsqueda con CDB
def cdb(asignacion):
    if len(asignacion) == len(mapa):
        return asignacion

    regiones_sin_color = [region for region in mapa if region not in asignacion]
    region = regiones_sin_color[0]
    for color in colores:
        if es_valida(asignacion, region, color):
            asignacion[region] = color
            resultado = cdb(asignacion)
            if resultado is not None:
                return resultado
            del asignacion[region]  # Retroceso si no lleva a una solución válida
    return None

# Resolución del problema CSP con CDB
solucion = cdb({})

# Resultado
if solucion is not None:
    print("Asignación de colores:")
    for region, color in solucion.items():
        print(f"{region}: {color}")
else:
    print("No se encontró solución.")

