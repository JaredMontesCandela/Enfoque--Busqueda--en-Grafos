class Grafo:
    def __init__(self, vertices):
        # Creamos un diccionario para almacenar las listas de adyacencia
        self.grafo = {}
        for v in range(vertices):
            self.grafo[v] = []

    def agregar_arista(self, u, v):
        # Agregamos una arista al grafo no dirigido
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def idfs(self, v, profundidad_maxima):
        stack = [(v, 0)]  # Pila para rastrear nodos y su profundidad
        visitado = set()  # Conjunto para evitar bucles infinitos

        while stack:
            nodo, profundidad = stack.pop()

            if nodo not in visitado:
                print(f"Nodo visitado: {nodo} (Profundidad: {profundidad})")
                visitado.add(nodo)

                if profundidad < profundidad_maxima:
                    for vecino in self.grafo[nodo]:
                        stack.append((vecino, profundidad + 1))

# Ejemplo de uso
if __name__ == "__main__":
    g = Grafo(6)
    g.agregar_arista(0, 1)
    g.agregar_arista(0, 2)
    g.agregar_arista(1, 3)
    g.agregar_arista(1, 4)
    g.agregar_arista(2, 4)
    g.agregar_arista(3, 4)
    g.agregar_arista(3, 5)

    profundidad_maxima = 2
    print(f"Búsqueda en profundidad iterativa (profundidad máxima: {profundidad_maxima}):")
    g.idfs(0, profundidad_maxima)
