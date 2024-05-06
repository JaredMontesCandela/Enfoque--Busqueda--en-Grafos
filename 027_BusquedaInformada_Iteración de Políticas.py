import numpy as np

# Definir el laberinto (0 representa un espacio libre y 1 representa una pared)
maze = np.array([
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
])

# Definir una política inicial aleatoria
policy = np.random.choice(['N', 'S', 'E', 'W'], size=maze.shape)

# Función para iterar la política y encontrar la política óptima
def policy_iteration(maze, policy):
    num_iterations = 100  # Número máximo de iteraciones
    discount_factor = 0.9  # Factor de descuento para futuras recompensas

    for i in range(num_iterations):
        new_policy = np.copy(policy)  # Copiar la política actual
        for row in range(maze.shape[0]):
            for col in range(maze.shape[1]):
                if maze[row, col] == 1:  # Ignorar las paredes
                    continue
                # Calcular las posibles recompensas para cada acción
                rewards = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
                if row > 0 and maze[row - 1, col] == 0:
                    rewards['N'] = 1 + discount_factor * rewards.get(policy[row - 1, col], 0)
                if row < maze.shape[0] - 1 and maze[row + 1, col] == 0:
                    rewards['S'] = 1 + discount_factor * rewards.get(policy[row + 1, col], 0)
                if col > 0 and maze[row, col - 1] == 0:
                    rewards['W'] = 1 + discount_factor * rewards.get(policy[row, col - 1], 0)
                if col < maze.shape[1] - 1 and maze[row, col + 1] == 0:
                    rewards['E'] = 1 + discount_factor * rewards.get(policy[row, col + 1], 0)
                # Seleccionar la acción con la mayor recompensa
                new_policy[row, col] = max(rewards, key=rewards.get)
        if np.array_equal(new_policy, policy):  # Verificar si la política convergió
            break
        policy = new_policy  # Actualizar la política
    return policy

# Ejecutar la iteración de políticas
optimal_policy = policy_iteration(maze, policy)

# Imprimir la política óptima
print("Política óptima:")
print(optimal_policy)
