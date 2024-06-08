"""Number guessing game in which user selects a range. Computer then generates number in that range
User must guess the number within minimum number of guesses"""

import random
import math


def display_menu():
    print("*" * 32)
    print("Welcome to Number Guessing Game!")
    print("*" * 32)
    print(" " * 8, "A.) Play")
    print(" " * 8, "B.) Rules")
    print(" " * 8, "C.) Exit")
    print("*" * 32)


def display_rules():
    print("*" * 32)
    print(" " * 10, "Rules")
    print("*" * 32)
    print("* User selects a range from A to B, where A and B are positive integers.")
    print("* Computer will select a random number between A and B.")
    print("* User has to guess that number in the minimum number of guesses.")


if __name__ == '__main__':
    guessCount = 0  # keeps track of current guess
    guessed = False  # state of player's guess

    while True:
        display_menu()

        choice = input("Enter your choice: ")
        # play game
        if choice.upper() == 'A':
            guessed = False  # reset guess state to false
            guessCount = 0  # reset guesses made

            while True:
                # prompt user for range of numbers for guessing
                guessRange = input("Enter range (A-B): ").split("-")

                # make sure input by user are two numbers and are integers and that lower range isn't higher than upper
                if (len(guessRange) == 2 and int(guessRange[0].isdigit()) and int(guessRange[1].isdigit())
                        and int(guessRange[0]) < int(guessRange[1])):
                    lowerRange, upperRange = int(guessRange[0]), int(guessRange[1])
                    chances = round(math.log(upperRange - lowerRange + 1, 2))  # max number of guesses has
                    print(f"\nYou've only {chances} chances to guess the integer!\n")

                    # generate random number for user to guess
                    numberToGuess = random.randint(lowerRange, upperRange)

                    while not guessed:
                        # prompt user to guess a number
                        try:
                            # if number of guesses surpasses max number of guesses
                            if guessCount >= chances:
                                print("\nBetter luck next time!")
                                guessed = True

                            else:
                                guess = int(input("Enter guess: "))
                                guessCount += 1

                                # correctly guesses
                                if guess == numberToGuess:
                                    print("\nCorrect guess")
                                    print(f'Total Number of Guesses: {guessCount}')  # display amount of guesses
                                    guessed = True

                                # if number is too high
                                elif guess > numberToGuess:
                                    print("\nTry Again! You guessed too high")
                                # if number is too low
                                elif guess < numberToGuess:
                                    print("\nTry Again! You guessed too low")
                        except ValueError:
                            print("\nInvalid input")

                    break
                else:
                    print("Please enter a valid range.")
        # display rules
        elif choice.upper() == 'B':
            display_rules()
        # exit game
        elif choice.upper() == "C":
            break
        # account for incorrect user input
        else:
            print("Invalid choice. Please try again.")
