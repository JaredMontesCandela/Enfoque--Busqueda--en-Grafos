import random

# Definir la matriz de pagos del juego de piedra, papel o tijera
# La matriz representa los resultados para el jugador 1 (filas) y el jugador 2 (columnas)
# 0 representa empate, 1 representa victoria para el jugador 1, -1 representa victoria para el jugador 2
payoff_matrix = [
    [0, -1, 1],  # Piedra vs Piedra, Piedra vs Papel, Piedra vs Tijera
    [1, 0, -1],  # Papel vs Piedra, Papel vs Papel, Papel vs Tijera
    [-1, 1, 0]   # Tijera vs Piedra, Tijera vs Papel, Tijera vs Tijera
]

# Función para simular una ronda del juego de piedra, papel o tijera
def play_round():
    # Jugador 1 y Jugador 2 eligen una de las tres opciones (0: Piedra, 1: Papel, 2: Tijera)
    choice_player1 = random.randint(0, 2)
    choice_player2 = random.randint(0, 2)

    # Determinar el resultado de la ronda
    result = payoff_matrix[choice_player1][choice_player2]

    # Imprimir las elecciones y el resultado de la ronda
    print("Jugador 1 elige {}, Jugador 2 elige {}".format(["Piedra", "Papel", "Tijera"][choice_player1], ["Piedra", "Papel", "Tijera"][choice_player2]))
    if result == 0:
        print("Empate en esta ronda")
    elif result == 1:
        print("Jugador 1 gana esta ronda")
    else:
        print("Jugador 2 gana esta ronda")

    return result

# Función para jugar al mejor de tres rondas
def play_game():
    score_player1 = 0
    score_player2 = 0
    rounds = 0

    while score_player1 < 2 and score_player2 < 2:
        rounds += 1
        print("\nRonda {}".format(rounds))
        result = play_round()
        if result == 1:
            score_player1 += 1
        elif result == -1:
            score_player2 += 1

    # Determinar al ganador del juego
    if score_player1 > score_player2:
        print("\n¡Jugador 1 gana el juego {} - {}!".format(score_player1, score_player2))
    elif score_player2 > score_player1:
        print("\n¡Jugador 2 gana el juego {} - {}!".format(score_player2, score_player1))
    else:
        print("\n¡Empate! El juego termina {} - {}.".format(score_player1, score_player2))

# Jugar al juego de piedra, papel o tijera
play_game()
