# Problem Statement: Number Guessing Game
# The computer selects a random number between 1 and 100. The player tries to guess it until correct.
# Time Complexity: O(N) in worst case (N = range of numbers)
# Space Complexity: O(1)

import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Example run
# number_guessing_game()
