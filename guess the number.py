import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)

    print("This is a number guessing game")
    print("Guess a number between 1 and 100")

    attempts = 0
    guessed = False

    while not guessed:
        player_guess = input("Enter your guess: ")

        if player_guess.isdigit():
            player_guess = int(player_guess)
            attempts += 1

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()