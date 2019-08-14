# Week 6 - Lab 6
# Backwards Guessing Game
# Created by: Robby Hurst
# Date: 08/13/2019
# Description: A game where the Computer guesses a random number and the user enters "Higher", "Lower" or "Correct"
#              The computer has 5 guesses to get it correct
# Added a function to start the game over


import random


def game():
    low = 0
    high = 100
    guess = 1
    random_number = random.randint(low, high)
    accepted_answers = {'Higher', 'Lower', 'Correct'}

    print("I'm going to guess a number between", low, "and", high, "within 5 guesses.")
    print("Please tell me if I am Higher, Lower or Correct.")
    print("Is", random_number, "the correct number?")

    response = input()

    while guess < 5:
        if response == "Higher":
            low = random_number + 1
            guess = guess + 1
            random_number = random.randint(low, high)
            print("Is", random_number, "the correct number?")
            response = input()
        elif response == "Lower":
            high = random_number - 1
            guess = guess + 1
            random_number = random.randint(low, high)
            print("Is", random_number, "the correct number?")
            response = input()
        elif response == "Correct":
            print("I guessed correctly and it took", guess, "guesses")
            play_again()
        elif response != ["Higher", "Lower", "Correct"]:
            print("Your answer is not Higher, Lower or Correct, please try again.")
            print("Is", random_number, "the correct number?")
            response = input()
    else:
        print("I didn't guess correctly within", guess, "guesses")
        play_again()


def play_again():
    while True:
        answer = input("Would you like to play again? (Y/N)")
        if answer == "Y":
            game()
        elif answer == "N":
            exit()
        else:
            print("I didn't recognize your answer, please try again.")


game()
