#-----------------GET THE IMPORT-----------------#
import random

#-----------------FUNCTION THAT CHECK THE INPUT-----------------#
def check_input(var_name):
    while True:
        try:
            number = int(input(f"Enter the {var_name}: "))
            return number
        except:
            continue
    
#-----------------GET THE LOWERBOUND AND UPPERBOUND-----------------#
def get_lowerbound():
    lowerbound = check_input("lowerbound")
    return lowerbound

#-----------------GET THE UPPERBOUND AND UPPERBOUND-----------------#
def get_upperbound():
    upperbound = check_input("upperbound")
    return upperbound



#-----------------GET THE RANDOM NUMBER-----------------#
def random_generator():
    random_number = random.randint(get_lowerbound(),get_upperbound())
    return random_number

def game():
    guess_counter = 0
    random_number = random_generator()
    while guess_counter <= 7:

        guess_counter = guess_counter+1
        
        guess_number = check_input("guess number")

        
        
        if guess_number == random_number:
            print(f"The number is {guess_number} and you found it right!! in {guess_counter} attempts")
            break

        elif guess_counter == 7 and guess_number != random_number:
            print(f"Oops sorry, the number is {random_number} better luck next time")
            break

        elif guess_number > random_number:
            print("Your guess is high")

        elif guess_number < random_number:
            print("Your guess is low")
    
game()    


