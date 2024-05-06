import random

# Definir el entorno del agente
num_states = 10
num_actions = 2
num_episodes = 1000

# Inicializar una matriz de valores de acción aleatorios
action_values = [[random.random() for _ in range(num_actions)] for _ in range(num_states)]

# Parámetros de aprendizaje
epsilon = 0.1  # Probabilidad de exploración
learning_rate = 0.1
discount_factor = 0.9

# Función para seleccionar una acción utilizando una política ε-greedy
def epsilon_greedy_policy(state, action_values, epsilon):
    if random.random() < epsilon:
        # Exploración: seleccionar una acción aleatoria
        action = random.randint(0, num_actions - 1)
    else:
        # Explotación: seleccionar la acción con el mayor valor de acción
        action = max(range(num_actions), key=lambda a: action_values[state][a])
    return action

# Función para realizar el aprendizaje por refuerzo activo
def active_reinforcement_learning(action_values, epsilon, learning_rate, discount_factor, num_episodes):
    for _ in range(num_episodes):
        # Seleccionar un estado aleatorio
        state = random.randint(0, num_states - 1)
        # Seleccionar una acción utilizando la política ε-greedy
        action = epsilon_greedy_policy(state, action_values, epsilon)
        # Obtener la recompensa correspondiente al estado y acción
        reward = random.random()  # En este ejemplo, la recompensa es aleatoria
        # Actualizar el valor de acción utilizando la regla de actualización Q-learning
        next_state = random.randint(0, num_states - 1)  # Simular transición a un próximo estado aleatorio
        best_next_action = max(range(num_actions), key=lambda a: action_values[next_state][a])
        td_target = reward + discount_factor * action_values[next_state][best_next_action]
        td_error = td_target - action_values[state][action]
        action_values[state][action] += learning_rate * td_error
    return action_values

# Ejecutar el aprendizaje por refuerzo activo
action_values = active_reinforcement_learning(action_values, epsilon, learning_rate, discount_factor, num_episodes)

# Imprimir los valores de acción finales aprendidos por el agente
print("Valores de acción finales aprendidos por el agente:")
for state in range(num_states):
    print("Estado {}: {}".format(state, action_values[state]))
