import random

# Definir la estructura de la red bayesiana dinámica
# En este ejemplo, consideramos un DBN con dos variables ocultas y dos variables observadas
num_hidden_states = 2
num_observed_states = 2

# Definir la matriz de transición de estados ocultos
transition_matrix_hidden = [
    [0.7, 0.3],  # Transición de estado oculto 0 a estado oculto 0 y estado oculto 0 a estado oculto 1
    [0.4, 0.6]   # Transición de estado oculto 1 a estado oculto 0 y estado oculto 1 a estado oculto 1
]

# Definir la matriz de transición de estados observados condicionales a los estados ocultos
transition_matrix_observed = [
    [[0.9, 0.1], [0.2, 0.8]],  # Transición de estado observado 0 a estado observado 0 y estado observado 0 a estado observado 1 para cada estado oculto
    [[0.5, 0.5], [0.1, 0.9]]   # Transición de estado observado 1 a estado observado 0 y estado observado 1 a estado observado 1 para cada estado oculto
]

# Parámetros de la simulación
num_time_steps = 5  # Número de pasos de tiempo

# Función para simular la dinámica de la DBN
def simulate_dbn(num_time_steps, transition_matrix_hidden, transition_matrix_observed):
    # Inicializar la secuencia de estados ocultos y observados
    hidden_states_sequence = [random.randint(0, num_hidden_states - 1)]  # Inicializar con un estado oculto aleatorio
    observed_states_sequence = []

    # Simular la dinámica de la DBN
    for _ in range(num_time_steps):
        # Generar el siguiente estado oculto
        next_hidden_state = random.choices(range(num_hidden_states), weights=transition_matrix_hidden[hidden_states_sequence[-1]])[0]

        # Generar el siguiente estado observado condicional al estado oculto
        next_observed_state = random.choices(range(num_observed_states), weights=transition_matrix_observed[next_hidden_state][hidden_states_sequence[-1]])[0]

        # Agregar los estados a las secuencias
        hidden_states_sequence.append(next_hidden_state)
        observed_states_sequence.append(next_observed_state)

    return hidden_states_sequence, observed_states_sequence

# Ejecutar la simulación de la DBN
hidden_states, observed_states = simulate_dbn(num_time_steps, transition_matrix_hidden, transition_matrix_observed)

# Imprimir los resultados de la simulación
print("Secuencia de estados ocultos:")
print(hidden_states)
print("Secuencia de estados observados:")
print(observed_states)
