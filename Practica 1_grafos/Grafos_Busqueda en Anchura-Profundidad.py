from collections import deque

# Definimos el grafo basado en la nueva imagen
graph = {
    'A': [('B', 6), ('C', 3), ('D', 9)],
    'B': [('F', 6), ('D', 12)],
    'C': [('F', 9)],
    'D': [('F', 3), ('E', 3)],
    'E': [('G', 3)],
    'F': [('G', 3), ('H', 3)],
    'G': [('H', 3)],
    'H': []
}
"""
podemos asignar el noda A como nuestro inico y el nodo H como nuestro objetivo, donde cada punto es una ciudad
y cada vertice en un camino con diferente kilometraje y el objetivo es buscar la ruta mas corta
"""

# Función BFS para encontrar el camino de A a H
def bfs(start, goal):
    # Cola para mantener los caminos
    queue = deque([[start]])
    
    # Conjunto para los nodos ya visitados
    visited = set()

    while queue:
        # Obtener el primer camino en la cola
        path = queue.popleft()
        node = path[-1]

        # Si hemos llegado al objetivo, devolvemos el camino
        if node == goal:
            return path

        # Si el nodo no ha sido visitado
        if node not in visited:
            visited.add(node)

            # Expandir los vecinos
            for (neighbor, weight) in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

# Ejecutar BFS de A a H
path = bfs('A', 'H')

if path:
    print("Camino encontrado:", " -> ".join(path))
else:
    print("No se encontró un camino.")
