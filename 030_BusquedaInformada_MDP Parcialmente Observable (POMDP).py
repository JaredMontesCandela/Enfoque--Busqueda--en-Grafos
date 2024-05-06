import numpy as np

# Definir la matriz de transición de estados, matriz de observación y matriz de recompensas
transition_matrix = np.array([
    [[0.7, 0.3], [0.3, 0.7]],  # Acción A
    [[0.4, 0.6], [0.6, 0.4]]   # Acción B
])
observation_matrix = np.array([
    [[0.9, 0.1], [0.2, 0.8]],  # Acción A
    [[0.5, 0.5], [0.1, 0.9]]   # Acción B
])
reward_matrix = np.array([
    [[5, 2], [0, 0]],  # Acción A
    [[10, 0], [-1, 0]]  # Acción B
])

# Parámetros del POMDP
num_states = 2
num_actions = 2
num_observations = 2
discount_factor = 0.9
num_iterations = 100

# Inicializar una política aleatoria
policy = np.random.randint(0, num_actions, size=num_states)

# Función para realizar la iteración de políticas en un POMDP
def policy_iteration_pomdp(transition_matrix, observation_matrix, reward_matrix, policy):
    for _ in range(num_iterations):
        new_policy = np.copy(policy)  # Copiar la política actual
        for state in range(num_states):
            action = policy[state]  # Obtener la acción actual para el estado
            # Calcular los valores esperados de cada acción en el estado actual
            expected_values = []
            for observation in range(num_observations):
                # Calcular el valor esperado para la observación actual
                expected_value = np.sum(transition_matrix[action][:, state] * observation_matrix[action][observation, state] * (reward_matrix[action][observation, state] + discount_factor * reward_matrix[action][:, state]))
                expected_values.append(expected_value)
            # Seleccionar la observación con el mayor valor esperado
            new_policy[state] = np.argmax(expected_values)
        if np.array_equal(new_policy, policy):  # Verificar si la política convergió
            print("Se encontró una política óptima.")
            break
        policy = new_policy  # Actualizar la política
    return policy

# Ejecutar la iteración de políticas en el POMDP
optimal_policy = policy_iteration_pomdp(transition_matrix, observation_matrix, reward_matrix, policy)

# Imprimir la política óptima
print("Política óptima:")
print(optimal_policy)
