import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append((v, peso))

    def bfs_costo_uniforme(self, inicio, destino):
        visitado = set()
        cola = [(0, inicio)]

        while cola:
            costo, nodo = heapq.heappop(cola)
            if nodo not in visitado:
                print(nodo, end=' ')
                visitado.add(nodo)
                if nodo == destino:
                    return
                for vecino, peso in self.grafo.get(nodo, []):
                    if vecino not in visitado:
                        heapq.heappush(cola, (costo + peso, vecino))

# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 4)
g.agregar_arista('A', 'C', 1)
g.agregar_arista('B', 'C', 2)
g.agregar_arista('B', 'D', 5)
g.agregar_arista('C', 'D', 8)
g.agregar_arista('C', 'E', 10)
g.agregar_arista('D', 'E', 2)
g.agregar_arista('D', 'Z', 6)
g.agregar_arista('E', 'Z', 2)

print("Recorrido BFS de costo uniforme desde A hasta Z:")
g.bfs_costo_uniforme('A', 'Z')
