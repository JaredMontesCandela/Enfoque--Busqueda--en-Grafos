import heapq  # Importamos heapq para usar una cola de prioridad

# Definimos una clase para representar un grafo con heurísticas
class GrafoConHeuristicas:
    def __init__(self):
        self.adyacencia = {}
        self.heuristicas = {}
    
    def agregar_vertice(self, vertice, heuristica=0):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []
            self.heuristicas[vertice] = heuristica
    
    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append(destino)

# Función de búsqueda voraz primero el mejor
def busqueda_voraz(grafo, inicio, objetivo):
    cola_prioridad = []  # Cola de prioridad para los nodos a explorar
    heapq.heappush(cola_prioridad, (grafo.heuristicas[inicio], inicio))
    visitados = set()  # Conjunto de nodos visitados
    
    while cola_prioridad:
        # Sacamos el nodo con menor valor de h(n), que es la heurística del nodo
        (heuristica_nodo, vertice_actual) = heapq.heappop(cola_prioridad)
        
        if vertice_actual == objetivo:  # Si el nodo actual es el objetivo, retornamos True
            return True
        
        if vertice_actual in visitados:  # Si ya hemos visitado este nodo, continuamos con el siguiente
            continue
        
        visitados.add(vertice_actual)  # Marcamos como visitado
        
        # Exploramos los vecinos del nodo actual
        for vecino in grafo.adyacencia[vertice_actual]:
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (grafo.heuristicas[vecino], vecino))
    
    return False  # Si no encontramos el objetivo

# Ejemplo de uso:
g = GrafoConHeuristicas()
# Agregamos vértices con sus respectivas heurísticas (distancia estimada al objetivo)
g.agregar_vertice('A', heuristica=3)
g.agregar_vertice('B', heuristica=2)
g.agregar_vertice('C', heuristica=1)
g.agregar_vertice('D', heuristica=0)  # El objetivo tiene una heurística de 0

# Agregamos aristas sin costos porque la búsqueda voraz no los considera
g.agregar_arista('A', 'B')
g.agregar_arista('A', 'C')
g.agregar_arista('B', 'D')
g.agregar_arista('C', 'D')

# Realizamos la búsqueda voraz desde 'A' hasta 'D'
encontrado = busqueda_voraz(g, 'A', 'D')
print(f"Objetivo {'encontrado' if encontrado else 'no encontrado'}.")
