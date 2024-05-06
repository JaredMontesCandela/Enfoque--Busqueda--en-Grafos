class Grafo(object):
    def __init__(self, adyacencia):
        # Inicializamos el grafo con la lista de adyacencia
        self.ady = adyacencia
        self._init_grafo(-1)

    def _init_grafo(self, inicio):
        # Inicializamos las estructuras de datos necesarias para la búsqueda
        self.encontrado = [False for n in self.ady]
        self.procesado = [False for n in self.ady]
        self.padre = [-1 for n in self.ady]
        self.inicio = inicio

    def profundidad(self, inicio):
        """Realiza una búsqueda en profundidad desde el nodo de inicio a todo el grafo."""
        self._init_grafo(inicio)
        q = [inicio]
        self.encontrado[inicio] = True

        while q:
            v = q.pop()
            self.procesado[v] = True

            for vecino in self.ady[v]:
                if not self.encontrado[vecino]:
                    q.append(vecino)
                    self.encontrado[vecino] = True
                    self.padre[vecino] = v

    def construir_camino(self, destino):
        """Devuelve el camino entre los vértices de inicio y destino."""
        if self.padre[destino] == -1 or self.inicio == -1:
            return None

        camino = [destino]
        p = destino
        while p != self.inicio:
            camino.append(self.padre[p])
            p = self.padre[p]

        return camino

# Ejemplo de uso:
adyacencia = [
    [1, 3, 4],
    [0, 2, 3, 4],
    [1, 4],
    [0, 1],
    [0, 1, 2]
]

inicio = 3
destino = 2
g = Grafo(adyacencia)
g.profundidad(inicio)
camino = g.construir_camino(destino)

print(f"Camino desde {inicio} hasta {destino}: {camino}")
