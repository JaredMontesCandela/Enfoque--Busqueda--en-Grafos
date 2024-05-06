import random

# Definir el entorno del agente
num_states = 6
num_actions = 2
num_episodes = 1000

# Inicializar la Q-table con valores aleatorios
q_table = [[random.random() for _ in range(num_actions)] for _ in range(num_states)]

# Parámetros de aprendizaje
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Probabilidad de exploración

# Función para seleccionar una acción utilizando una política ε-greedy
def epsilon_greedy_policy(state, q_table, epsilon):
    if random.random() < epsilon:
        # Exploración: seleccionar una acción aleatoria
        action = random.randint(0, num_actions - 1)
    else:
        # Explotación: seleccionar la acción con el mayor valor Q
        action = max(range(num_actions), key=lambda a: q_table[state][a])
    return action

# Función para realizar el aprendizaje por Q-learning
def q_learning(q_table, alpha, gamma, epsilon, num_episodes):
    for _ in range(num_episodes):
        # Inicializar el estado
        state = random.randint(0, num_states - 1)
        # Iterar hasta llegar al estado objetivo
        while True:
            # Seleccionar una acción utilizando la política ε-greedy
            action = epsilon_greedy_policy(state, q_table, epsilon)
            # Simular la acción y observar el próximo estado y la recompensa
            next_state = random.randint(0, num_states - 1)  # En este ejemplo, el próximo estado es aleatorio
            reward = random.random()  # En este ejemplo, la recompensa es aleatoria
            # Actualizar el valor Q utilizando la regla de Q-learning
            best_next_action = max(range(num_actions), key=lambda a: q_table[next_state][a])
            td_target = reward + gamma * q_table[next_state][best_next_action]
            td_error = td_target - q_table[state][action]
            q_table[state][action] += alpha * td_error
            # Actualizar el estado actual al próximo estado
            state = next_state
            # Salir del bucle si llegamos al estado objetivo
            if state == num_states - 1:
                break
    return q_table

# Ejecutar el aprendizaje por Q-learning
q_table = q_learning(q_table, alpha, gamma, epsilon, num_episodes)

# Imprimir la Q-table resultante
print("Q-table resultante:")
for state in range(num_states):
    print("Estado {}: {}".format(state, q_table[state]))
