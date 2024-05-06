# Definición del problema CSP
# En este ejemplo, consideramos un problema de asignación de colores a un mapa
# con ciertas restricciones, donde cada región debe tener un color diferente
# a sus vecinos.

# Representación del mapa como un grafo, donde las regiones son nodos
# y las conexiones entre regiones son aristas.
mapa = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Colores disponibles
colores = ['Rojo', 'kaki', 'Azul']

# Función para verificar si una asignación es válida
def es_valida(asignacion, region, color):
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Algoritmo de comprobación hacia delante (forward checking)
def forward_checking(asignacion, dominios):
    if len(asignacion) == len(mapa):
        return asignacion

    regiones_sin_color = [region for region in mapa if region not in asignacion]
    region = regiones_sin_color[0]

    for color in dominios[region]:
        if es_valida(asignacion, region, color):
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[region] = color

            nuevo_dominio = {r: d.copy() for r, d in dominios.items()}
            for vecino in mapa[region]:
                if color in nuevo_dominio[vecino]:
                    nuevo_dominio[vecino].remove(color)

            resultado = forward_checking(nueva_asignacion, nuevo_dominio)
            if resultado is not None:
                return resultado
    return None

# Resolución del problema CSP con forward checking
dominios = {region: colores.copy() for region in mapa}
solucion = forward_checking({}, dominios)

# Resultado
if solucion is not None:
    print("Asignación de colores:")
    for region, color in solucion.items():
        print(f"{region}: {color}")
else:
    print("No se encontró solución.")
