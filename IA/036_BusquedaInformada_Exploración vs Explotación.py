import random

"""
Supongamos que estás en un casino y quieres encontrar la mejor máquina tragamonedas para 
maximizar tus ganancias. Hay tres máquinas tragamonedas disponibles, pero no sabes cuál es la 
mejor. Decides usar una estrategia de exploración vs. explotación para decidir en cuál jugar.
"""



# Definir las ganancias promedio de cada máquina tragamonedas (en dólares)
slot_machine_rewards = [10, 5, 8]

# Función para simular jugar en una máquina tragamonedas
def play_slot_machine(machine_index):
    return random.normalvariate(slot_machine_rewards[machine_index], 1)

# Parámetros de la política ε-greedy
epsilon = 0.2  # Probabilidad de exploración

# Función para seleccionar una máquina tragamonedas utilizando una política ε-greedy
def epsilon_greedy_policy():
    if random.random() < epsilon:
        # Exploración: seleccionar una máquina tragamonedas aleatoria
        return random.randint(0, len(slot_machine_rewards) - 1)
    else:
        # Explotación: seleccionar la máquina tragamonedas con las ganancias promedio más altas
        return max(range(len(slot_machine_rewards)), key=lambda i: slot_machine_rewards[i])

# Simular jugar en las máquinas tragamonedas
num_plays = 1000
total_reward = 0
plays_per_machine = [0] * len(slot_machine_rewards)
for _ in range(num_plays):
    selected_machine = epsilon_greedy_policy()
    reward = play_slot_machine(selected_machine)
    total_reward += reward
    plays_per_machine[selected_machine] += 1

# Calcular el promedio de ganancias por juego
average_reward_per_play = total_reward / num_plays

# Imprimir resultados
print("Promedio de ganancias por juego: ${:.2f}".format(average_reward_per_play))
print("Número de juegos por máquina tragamonedas:")
for i, plays in enumerate(plays_per_machine):
    print("Máquina tragamonedas {}: {}".format(i+1, plays))
