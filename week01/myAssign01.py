import random
from random import randint

print("Welcome to the number guessing game!")
# Ask for the seed
seed = input("Enter random seed: ")
#Create the random number based on the seed
random.seed(seed)

# Initiating the try again answer to enter a  loop 
try_again = 'yes'

while try_again != 'no':  
    # Init variable values    
    num = randint(1, 100)
    guess_number = 0
    guess_tries = 0

    #Enter loop if number is different than guessed input
    while num != guess_number:
        guess_tries += 1
        guess_number = int(input("\nPlease enter a guess: "))
        if guess_number == num:
            # Number guessed, exit the loop
            print("Congratulations. You guessed it!")
            print("It took you " + str(guess_tries) + " guesses.\n")
            break
        else:
            # Check if the guess number is lower or higher
            if guess_number > num:
                print("Lower")
            else:
                print("Higher")
    # Finished the game, ask if want to try again.
    try_again = input("Would you like to play again (yes/no)? ")

print ("Thank you. Goodbye.")

