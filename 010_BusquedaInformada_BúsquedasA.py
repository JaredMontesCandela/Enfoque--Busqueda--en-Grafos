import heapq  # Importamos la librería heapq para usar una cola de prioridad

# Definimos una clase Nodo para representar cada nodo en el grafo
class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado  # El estado actual del nodo
        self.padre = padre  # El nodo padre en el camino
        self.costo = costo  # El costo para llegar a este nodo desde el inicio
        self.heuristica = heuristica  # La heurística estimada hasta el objetivo
        self.f_costo = self.costo + self.heuristica  # La suma de costo y heurística

    def __lt__(self, otro):
        # Define cómo se comparan dos nodos (necesario para la cola de prioridad)
        return self.f_costo < otro.f_costo

# Función del algoritmo A*
def a_estrella(grafo, inicio, objetivo, heuristica):
    nodo_inicial = Nodo(inicio, None, 0, heuristica(inicio))  # Creamos el nodo inicial
    frontera = []  # La frontera donde almacenamos los nodos a explorar
    heapq.heappush(frontera, nodo_inicial)  # Añadimos el nodo inicial a la frontera
    explorados = set()  # Conjunto de estados ya explorados

    while frontera:
        nodo_actual = heapq.heappop(frontera)  # Obtenemos el nodo con menor f_costo
        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)  # Reconstruimos el camino si llegamos al objetivo

        explorados.add(nodo_actual.estado)  # Marcamos como explorado

        for vecino in grafo[nodo_actual.estado]:
            nuevo_costo = nodo_actual.costo + grafo[nodo_actual.estado][vecino]  # Calculamos el nuevo costo
            nuevo_nodo = Nodo(vecino, nodo_actual, nuevo_costo, heuristica(vecino))  # Creamos un nuevo nodo

            if vecino not in explorados and nuevo_nodo not in frontera:
                heapq.heappush(frontera, nuevo_nodo)  # Añadimos a la frontera si no ha sido explorado
            elif nuevo_nodo in frontera:
                indice_existente = frontera.index(nuevo_nodo)
                if nuevo_costo < frontera[indice_existente].costo:
                    frontera[indice_existente] = nuevo_nodo  # Actualizamos el nodo en la frontera si es mejor
                    heapq.heapify(frontera)

    return None  # Retornamos None si no encontramos un camino

# Función para reconstruir el camino desde el nodo final hasta el inicio
def reconstruir_camino(nodo_final):
    camino = []
    while nodo_final:
        camino.append(nodo_final.estado)  # Añadimos el estado al camino
        nodo_final = nodo_final.padre  # Movemos al padre para continuar reconstruyendo
    return camino[::-1]  # Retornamos el camino en orden correcto (inicio a fin)

# Ejemplo de uso del algoritmo A*
grafo_ejemplo = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 4},
    'C': {'D': 2},
    'D': {}
}

# Función heurística simple que siempre devuelve cero (debería ser reemplazada por una real)
def heuristica_simple(nodo):
    return 0

# Ejecutamos la búsqueda A* y mostramos el resultado
camino_encontrado = a_estrella(grafo_ejemplo, 'A', 'D', heuristica_simple)
print("Camino encontrado:", camino_encontrado)
