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

# Ejemplo de uso: Lugares cotidianos
g = Grafo()

# Agregar conexiones entre lugares cotidianos
g.agregar_arista("Casa", "Trabajo")
g.agregar_arista("Casa", "Supermercado")
g.agregar_arista("Trabajo", "Gimnasio")
g.agregar_arista("Trabajo", "Parque")
g.agregar_arista("Supermercado", "Parque")
g.agregar_arista("Parque", "Casa")
g.agregar_arista("Gimnasio", "Casa")

print("Recorrido BFS comenzando desde 'Casa':")
g.bfs("Casa")

"""
Este recorrido muestra que, desde tu casa, puedes ir al trabajo o al supermercado, y luego explorar el gimnasio y el parque.
"""