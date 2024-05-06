
import numpy as np

# Definir el MDP (Matriz de Transición de Estados y Matriz de Recompensas)
transition_matrix = np.array([
    [[0.8, 0.1, 0.1], [0.2, 0.6, 0.2], [0.1, 0.1, 0.8]],  # Acción A
    [[0.7, 0.2, 0.1], [0.1, 0.8, 0.1], [0.3, 0.3, 0.4]]   # Acción B
])
reward_matrix = np.array([
    [[5, 2, 1], [0, 0, 0], [0, 0, 10]],  # Acción A
    [[10, 0, -1], [0, 0, 0], [-1, 0, 0]]  # Acción B
])

# Parámetros del MDP
num_states = 3
num_actions = 2
discount_factor = 0.9
num_iterations = 100

# Inicializar una política aleatoria
policy = np.random.randint(0, num_actions, size=num_states)

# Función para realizar la iteración de políticas en un MDP
def policy_iteration_mdp(transition_matrix, reward_matrix, policy):
    for _ in range(num_iterations):
        new_policy = np.copy(policy)  # Copiar la política actual
        for state in range(num_states):
            action = policy[state]  # Obtener la acción actual para el estado
            # Calcular el valor esperado de cada acción en el estado actual
            expected_values = np.sum(transition_matrix[action][state] * (reward_matrix[action][state] + discount_factor * np.dot(transition_matrix[action][state], reward_matrix[action].T)))

            # Seleccionar la acción con el mayor valor esperado
            new_policy[state] = np.argmax(expected_values)
        if np.array_equal(new_policy, policy):  # Verificar si la política convergió
            break
        policy = new_policy  # Actualizar la política
    return policy

# Ejecutar la iteración de políticas en el MDP
optimal_policy = policy_iteration_mdp(transition_matrix, reward_matrix, policy)

# Imprimir la política óptima
print("Política óptima:")
print(optimal_policy)
