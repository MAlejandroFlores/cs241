import random
from random import randint

print("Welcome to the number guessing game!")
# ... other stuff here ...
seed = input("Enter random seed: \n")
random.seed(seed)
# ... possibly more stuff here ...
try_again = 'yes'
while try_again != 'no':
    num = randint(1, 50)
    guess_number = 0
    guess_tries = 0

    while num != guess_number:
        guess_tries += 1
        guess_number = int(input("Please enter a guess: "))
        if guess_number == num:
            print("Congratulations. You guessed it!")
            print("It took you " + str(guess_tries) + " guesses.")
            break
        else:
            if guess_number > num:
                print("Lower\n")
            else:
                print("Higher\n")
    try_again = input("Would you like to play again (yes/no)? ")

