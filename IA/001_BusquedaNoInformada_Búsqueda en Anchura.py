from collections import defaultdict, deque

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    def bfs(self, inicio):
        visitado = set()
        cola = deque([inicio])

        while cola:
            nodo = cola.popleft()
            if nodo not in visitado:
                print(nodo, end=' ')
                visitado.add(nodo)
                for vecino in self.grafo[nodo]:
                    if vecino not in visitado:
                        cola.append(vecino)

# Ejemplo de uso
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 0)
g.agregar_arista(2, 3)
g.agregar_arista(3, 3)

print("Recorrido BFS comenzando desde el nodo 2:")
g.bfs(2)
