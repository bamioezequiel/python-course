import random

options = ["rock", "paper", "scissors"]
win_user = 0
win_computer = 0

def start_game(option_user, option_computer): 
    result = "Lose"
    if options[option_user] == "rock" and options[option_computer] == "scissors":
        result = "Win"
    elif options[option_user] == "scissors" and options[option_computer] == "paper":
        result = "Win"
    elif options[option_user] == "paper" and options[option_computer] == "rock":
        result = "Win"
    elif options[option_user] == "rock" and options[option_computer] == "rock":
        result = "Tie"
    elif options[option_user] == "paper" and options[option_computer] == "paper":
        result = "Tie"
    elif options[option_user] == "scissors" and options[option_computer] == "scissors":
        result = "Tie"
    return result

while True:
    print("\n===============================================\n")
    print(f"USER ({win_user}) - ({win_computer}) COMPUTER)\n")
    print("===============================================")

    option_user = int(input("Choise a option: [0] Rock [1] Paper [2] Scissors\n"))
    option_computer = random.randint(0, 2)

    result = start_game(option_user, option_computer)
    print(f"\nUser [{options[option_user]}] vs [{options[option_computer]}] Computer\n")

    if result == "Win" :
        print("User Win!!")
        win_user += 1
    elif result == "Lose" :
        print("Computer Win!!")
        win_computer += 1
    else:
        print("Tie!!")
