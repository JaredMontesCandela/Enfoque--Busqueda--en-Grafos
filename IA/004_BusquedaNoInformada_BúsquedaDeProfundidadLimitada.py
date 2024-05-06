# Definimos una clase para representar el grafo
class Grafo:
    def __init__(self, vertices):
        # Creamos un diccionario para almacenar las listas de adyacencia
        self.grafo = {}
        for v in range(vertices):
            self.grafo[v] = []

    # Función para agregar una arista al grafo
    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    # Función de búsqueda en profundidad limitada (DLS)
    def dls(self, v, visitado, profundidad_max):
        # Marcamos el nodo actual como visitado
        visitado[v] = True
        print(f"Nodo visitado: {v}")

        # Si aún no se ha alcanzado la profundidad máxima, exploramos los vecinos
        if profundidad_max > 0:
            for vecino in self.grafo[v]:
                if not visitado[vecino]:
                    print(f"Explorando vecino: {vecino}")
                    self.dls(vecino, visitado, profundidad_max - 1)

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

    # Inicializamos la lista de nodos visitados
    visitado = [False] * 6

    # Profundidad máxima permitida (ajústala según tus necesidades)
    profundidad_maxima = 2

    # Llamamos a la función DLS desde el nodo 0
    print(f"Búsqueda en profundidad limitada (profundidad máxima: {profundidad_maxima}):")
    g.dls(0, visitado, profundidad_maxima)