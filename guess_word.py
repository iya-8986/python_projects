import random



words =['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print(word)
turns = 12
guess = ""
while turns > 0:
    guess = input("Enter your guess: ")

    if guess == word:
        print("You win!")
        break
    elif guess != word:
        for char in word:
            if char in guess:
                print(char, end = " ")
            else:
                print("_", end=" " )
                turns -= 1



