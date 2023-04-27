"""
  Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
  El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
  gane cada punto del juego.
  
  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
  - Si quieres, puedes controlar errores en la entrada de datos.   
  - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""


scores = ["Love", 15, 30, 40, "Advantage", "Win"]
def calculate_scores(scores_games):
    p1 = 0
    p2 = 0

    print("P1 - P2")
    for game in scores_games:
        if game == "P1":
            if p1 == 3 and p2 == 4:
                p2 -= 1
            else: 
                p1 += 1
        else:
            if p2 == 3 and p1 == 4:
                p1 -= 1
            else:
                p2 += 1

        if p1 > 5 or p2 > 5: 
            return

        if((p1 == 3 or p2 == 3) and p1 == p2): 
            print("Deuce")   
        else:
            print(f"{scores[p1]} - {scores[p2]}")   

calculate_scores(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])
#calculate_scores(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P1", "P1"])
#calculate_scores(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"])
#calculate_scores(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1"])
