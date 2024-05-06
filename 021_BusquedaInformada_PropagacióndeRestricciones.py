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
colores = ['Rojo', 'Verde', 'Azul']

# Función para verificar si una asignación es válida
def es_valida(asignacion, region, color):
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Función de propagación de restricciones AC-3
def ac3(grafo, dominios):
    cola = [(Xi, Xj) for Xi in grafo for Xj in grafo[Xi]]
    while cola:
        Xi, Xj = cola.pop(0)
        if revisar_arco(grafo, dominios, Xi, Xj):
            for Xk in grafo[Xi]:
                if Xk != Xj:
                    cola.append((Xk, Xi))
    return dominios

# Función para revisar el arco (Xi, Xj) y reducir el dominio de Xi si es necesario
def revisar_arco(grafo, dominios, Xi, Xj):
    revisado = False
    for x in dominios[Xi]:
        if not any(es_valida({Xi: x}, Xj, y) for y in dominios[Xj]):
            dominios[Xi].remove(x)
            revisado = True
    return revisado

# Resolución del problema CSP con propagación de restricciones
dominios = {region: colores.copy() for region in mapa}
dominios = ac3(mapa, dominios)

# Resultado
if all(dominios[region] for region in dominios):
    print("Asignación de colores:")
    for region, color in dominios.items():
        print(f"{region}: {color[0]}")
else:
    print("No se encontró solución.")
