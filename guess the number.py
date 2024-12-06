import random


def guess_the_number(): # makes a function
    number_to_guess = random.randint(1, 100) # makes a number the user has to guess

    print("This is a number guessing game") # tells the user what the game is
    print("Guess a number between 1 and 100") # instructions for the game

    attempts = 0 # keeps track of the amount of attempts
    guessed = False

    while not guessed:
        player_guess = input("Enter your guess: ") # prompts the user to guess the number

        if player_guess.isdigit(): # if function to make sure the code mentions when the user guesses the correct code
            player_guess = int(player_guess) # adds a guess every time the user guesses
            attempts += 1

            if player_guess < number_to_guess: # checks if the user guess is lower than the random number
                print("Too low! Try again.")
            elif player_guess > number_to_guess: # checks if the user guess is higher than the random number
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.") # tells the user how many guesses they took
        else:
            print("Please enter a valid number.") # if the user doesn't put in an integer, the computer will tell them to put in a real digit


if __name__ == "__main__":
    guess_the_number()