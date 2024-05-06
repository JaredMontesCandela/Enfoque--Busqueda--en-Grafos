import random

# Definir el entorno del agente
num_states = 4
num_actions = 2

# Inicializar la matriz de transición con probabilidades aleatorias
transition_matrix = []
for _ in range(num_actions):
    action_matrix = []
    for _ in range(num_states):
        state_probs = [random.random() for _ in range(num_states)]
        total_probability = sum(state_probs)
        if total_probability == 0:
            # Si la suma total de las probabilidades es cero, asignamos probabilidades uniformes
            action_matrix.append([1 / num_states] * num_states)
        else:
            action_matrix.append([prob / total_probability for prob in state_probs])
    transition_matrix.append(action_matrix)

# Verificar que las probabilidades sumen 1 en cada fila
for action in range(num_actions):
    for state in range(num_states):
        assert round(sum(transition_matrix[action][state]), 5) == 1, "Probabilities do not sum to 1"

print("Matriz de transición corregida con probabilidades normalizadas correctamente.")
