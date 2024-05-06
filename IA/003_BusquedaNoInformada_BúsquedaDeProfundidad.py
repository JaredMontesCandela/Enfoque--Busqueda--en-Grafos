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

    # Función de búsqueda en profundidad (DFS)
    def dfs(self, v, visitado):
        # Marcamos el nodo actual como visitado
        visitado[v] = True
        print(f"Nodo visitado: {v}")

        # Recorremos los vecinos no visitados
        for vecino in self.grafo[v]:
            if not visitado[vecino]:
                print(f"Explorando vecino: {vecino}")
                self.dfs(vecino, visitado)

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

    # Llamamos a la función DFS desde el nodo 0
    g.dfs(0, visitado)
