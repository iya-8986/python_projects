import random


while True:
    try:
        get_lowerbound = int(input("Enter the lowerbound: "))
        get_upperbound = int(input("Enter the upperbound: "))
        break
    except:
        continue

random_number = random.randint(get_lowerbound,get_upperbound)
guess_counter = 0
print(random_number)

while guess_counter <= 7:
    guess_counter = guess_counter+1
    while True:
        try:
            guess_number = int(input("Enter a number: "))
            break
        except:
            continue
    
    
    if guess_number == random_number:
        print(f"The number is {guess_number} and you found it right!! in {guess_counter} attempt")
        break

    elif guess_counter == 7 and guess_number != random_number:
        print(f"Oops sorry, the number is {random_number} better luck next time")
        break

    elif guess_number > random_number:
        print("Your guess is high")

    elif guess_number < random_number:
        print("Your guess is low")


    