import random


def check_input(var_name):
    while True:
        try:
            choice = int(input(f"Enter your {var_name}: "))
            return choice
        except:
            continue

def check_choice(play_choice):
    if play_choice == 1:
        return "Rock"
    elif play_choice == 2:
        return "Paper"
    elif play_choice == 3:
        return "Scissors"
    
def check_winner(play,comp):
    if play == comp:
        print("<== It's a tie! ==>\n")
    elif play == "Rock":
        if comp == "Scissors":
            print("<== Computer Wins! ==>\n")
        else:
            print("<== You Win! ==>\n")
    elif play == "Scissors":
        if comp == "Rock":
            print("<== Computer Wins! ==>\n")
        else:
            print("You Win!")
    elif play == "Paper":
        if comp == "Scissors":
            print("<== Computer Wins! ==>\n")
        else:
            print("<== You Win! ==>\n")

def yes_no():
    while True:
        try:
            answer = input("Do you want to play again? (Y/N): ")
            answer = answer.upper()
            if answer == "Y":
                return True
            elif answer == "N":
                return False
        except:
            continue     


print("Winning rules of the game ROCK PAPER SCISSORS are: \n"
      + "Rock Vs Papaer -> Paper wins \n"
      + "Rock Vs Scissors -> Rock wins \n"
      + "Paper Vs Scissors -> Scissors wins \n")
while True:
    print("1 - Rock \n2 - Paper \n3 - Scissors")
    player_choice = check_input("choice")
    player_choice = check_choice(player_choice)
    print(f"Player's choice is {player_choice}")

    print("Now it's Computer's Turn")
    computer_choice = random.randint(1,3)
    computer_choice = check_choice(computer_choice)
    print(f"Computer's Choice is {computer_choice}")

    print(f"{player_choice} VS {computer_choice}")
    check_winner(player_choice,computer_choice)

    play_again = yes_no()
    if play_again:
        continue
    else:
        print("Thank you for playing!")
        break







    