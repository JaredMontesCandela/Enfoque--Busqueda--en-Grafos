# Supongamos que tenemos un grafo y queremos estimar la distancia al objetivo desde cada nodo
heuristicas = {
    'A': 4,  # Heurística para el nodo A
    'B': 3,  # Heurística para el nodo B
    'C': 2,  # Heurística para el nodo C
    'D': 1,  # Heurística para el nodo D
    'E': 0   # Heurística para el nodo objetivo E
}

# Función que devuelve la heurística de un nodo
def obtener_heuristica(nodo):
    return heuristicas.get(nodo, float('inf'))  # Devuelve infinito si el nodo no tiene heurística

# Ejemplo de cómo usar la función de heurística
nodo_actual = 'A'
print(f"La heurística del nodo {nodo_actual} es: {obtener_heuristica(nodo_actual)}")

# Supongamos que estamos en el nodo A y queremos decidir si ir al nodo B o C
nodo_b = 'B'
nodo_c = 'C'

# Comparamos las heurísticas para tomar una decisión
if obtener_heuristica(nodo_b) < obtener_heuristica(nodo_c):
    print(f"Es más prometedor ir al nodo {nodo_b} que al nodo {nodo_c} basándonos en la heurística.")
else:
    print(f"Es más prometedor ir al nodo {nodo_c} que al nodo {nodo_b} basándonos en la heurística.")
