# Importamos la clase deque para poder utilizar colas en nuestro algoritmo
from collections import deque

# Definimos una clase para representar un grafo
class Grafo:
    # El constructor inicializa el diccionario de adyacencia que usaremos para almacenar los vértices y sus vecinos
    def __init__(self):
        self.adyacencia = {}
    
    # Método para agregar un vértice al grafo. Si el vértice no existe, lo añade al diccionario.
    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []
    
    # Método para agregar una arista al grafo. Esto conecta dos vértices en ambas direcciones (bidireccional).
    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append(destino)
        self.adyacencia[destino].append(origen)

# Función de búsqueda genérica en grafos
def busqueda_en_grafos(grafo, inicio, objetivo):
    # Utilizamos una cola para mantener un registro de los vértices que debemos visitar
    cola = deque([inicio])
    # Un conjunto para llevar un registro de los vértices que ya hemos visitado
    visitados = set([inicio])
    
    # Continuamos la búsqueda mientras haya vértices en la cola
    while cola:
        vertice = cola.popleft()  # Sacamos el primer vértice de la cola
        if vertice == objetivo:  # Comprobamos si hemos alcanzado nuestro objetivo
            print(f"Objetivo {objetivo} encontrado.")
            return True
        
        print(f"Visitando: {vertice}")  # Imprimimos el vértice que estamos visitando
        # Revisamos los vecinos del vértice actual
        for vecino in grafo.adyacencia[vertice]:
            if vecino not in visitados:  # Si no ha sido visitado, lo agregamos a la cola y al conjunto de visitados
                visitados.add(vecino)
                cola.append(vecino)
    
    print("Objetivo no encontrado.")  # Si salimos del bucle sin encontrar el objetivo, significa que no está en el grafo
    return False

# Ejemplo de uso:
# Creamos un nuevo grafo y agregamos vértices y aristas entre ellos
g = Grafo()
g.agregar_arista('A', 'B')
g.agregar_arista('A', 'C')
g.agregar_arista('B', 'D')
g.agregar_arista('C', 'D')
g.agregar_arista('D', 'E')

# Realizamos la búsqueda en el grafo desde el vértice 'A' hasta encontrar el vértice 'E'
busqueda_en_grafos(g, 'A', 'E')
