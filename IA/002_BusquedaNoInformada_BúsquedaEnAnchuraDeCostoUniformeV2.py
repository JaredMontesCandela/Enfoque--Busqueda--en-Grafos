class Nodo:
    def __init__(self, estado, padre=None, costo=0):
        self.estado = estado  # El estado actual del nodo
        self.padre = padre    # El nodo padre de este nodo
        self.costo = costo    # El costo acumulado desde el nodo inicial hasta este nodo

"""
Definición de la clase Node

Aquí se define una clase llamada Node. Cada nodo representa un estado en el grafo de búsqueda.
El constructor -__init__- inicializa tres atributos:
-state: representa el estado actual del nodo (por ejemplo, un nombre de ciudad o una posición en un tablero).
-parent: es un puntero al nodo padre (el nodo del que se expandió este nodo).
-cost: almacena el costo acumulado desde el nodo inicial hasta este nodo.
"""  

# Definimos la función de búsqueda de costo uniforme
def busqueda_costo_uniforme(grafo, inicio, objetivo):
    # Inicializamos la lista de nodos por explorar con el nodo inicial
    abiertos = [Nodo(inicio)]
    # Inicializamos la lista de nodos ya explorados
    cerrados = []
    
   # Mientras haya nodos por explorar, continuamos la búsqueda
    while abiertos:
        # Elegimos el nodo con menor costo total acumulado
        nodo_actual = min(abiertos, key=lambda x: x.costo)
        # Removemos el nodo elegido de la lista de abiertos
        abiertos.remove(nodo_actual)
        # Agregamos el nodo actual a la lista de cerrados
        cerrados.append(nodo_actual)

        # Si el nodo actual es el objetivo, reconstruimos y devolvemos el camino encontrado
        if nodo_actual.estado == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            return camino[::-1]  # Devolvemos el camino en orden desde el inicio al objetivo

        # Si no es el objetivo, expandimos los hijos del nodo actual
        for hijo_estado, costo_arista in grafo[nodo_actual.estado].items():
            hijo_nodo = Nodo(hijo_estado, nodo_actual, nodo_actual.costo + costo_arista)
            # Solo agregamos el hijo si no está en abiertos ni en cerrados
            if hijo_nodo not in abiertos and hijo_nodo not in cerrados:
                abiertos.append(hijo_nodo)

    return None  # Si no encontramos un camino, devolvemos None

# Ejemplo de uso del algoritmo con un grafo definido y un inicio y objetivo dados
grafo = {
    'A': {'B': 3, 'C': 5},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 1},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 4},
    'G': {}
}

nodo_inicio = 'A'
nodo_objetivo = 'G'
resultado = busqueda_costo_uniforme(grafo, nodo_inicio, nodo_objetivo)
print("Camino óptimo:", resultado)

"""
Definición de la función uniform_cost_search

La función -uniform_cost_search- toma tres argumentos:
-graph: un diccionario que representa el grafo (donde las claves son los nodos y los valores son diccionarios que contienen los nodos vecinos y sus costos).
-start: el nodo de inicio.
-goal: el nodo objetivo al que queremos llegar.
Inicializa dos listas: -opened- (nodos abiertos) y -closed- (nodos cerrados).
El bucle while se ejecuta mientras haya nodos en la lista opened.
Se selecciona el nodo con el menor valor de costo -(current_node)- y se mueve de -opened a closed-.
Si -current_node- es igual al nodo objetivo -(goal)-, se construye el camino desde el estado inicial al estado final.
Para cada hijo del nodo seleccionado, se calcula el costo desde el nodo inicial hasta él.
Si el hijo no está en ninguna de las listas o está en -opened- pero con un costo mayor, se agrega a -opened-.
Finalmente, se devuelve el camino óptimo o None si no se encuentra.
"""