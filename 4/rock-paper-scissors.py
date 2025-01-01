import random

choices = ["rock", "paper", "scissors"]
player_score = 0
cpu_score = 0
PLAYER_CHOICE = 0
CPU_CHOICE = 0

def cpu_choice():
    return choices[(random.randint(1, 3)) - 1]

def player_choice():
    try:
        PLAYER_CHOICE = int(input("Choose:\n1: Rock\n2: Paper\n3: Scissors\n0: Quit.\n"))
    except ValueError:
        print("Please choose using the numbers provided...\n")
        player_choice()
    else:
        if PLAYER_CHOICE not in range(0,4):
            print("Please choose a valid option...")
            player_choice()
        elif PLAYER_CHOICE == 0:
            print(f"\nThank you for playing!\nThe final score was {player_score} to {cpu_score}.")
            if player_score > cpu_score:
                print("You Win!")
            elif player_score < cpu_score:
                print("You Lose. Better Luck Next Time!")
            else:
                print("You Tied!")
            quit()
        else:
            PLAYER_CHOICE = choices[(int(PLAYER_CHOICE)) - 1]
            return PLAYER_CHOICE
    
def game_logic(PLAYER_CHOICE, CPU_CHOICE):

    if PLAYER_CHOICE == CPU_CHOICE:
        return("Tie!")
    elif PLAYER_CHOICE == "rock" and CPU_CHOICE == "paper" or PLAYER_CHOICE == "paper" and CPU_CHOICE == "scissors" or PLAYER_CHOICE == "scissors" and CPU_CHOICE == "rock":
        global cpu_score
        cpu_score+=1
        return "CPU Won!"
    else:
        global player_score
        player_score+=1
        return "Player Won!"

def game_loop():
    print(f"Player Score: {player_score}\t\tCPU Score: {cpu_score}\n")
    global PLAYER_CHOICE
    PLAYER_CHOICE = player_choice()
    global CPU_CHOICE
    CPU_CHOICE = cpu_choice()
    print(game_logic(PLAYER_CHOICE, CPU_CHOICE))
    game_loop()
    
def main():
    print("Rock, Paper, Scissors! Terminal Edition")
    game_loop()
    
if __name__ == "__main__":
    main()