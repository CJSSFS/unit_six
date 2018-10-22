import random


def play():
    play1 = input("Would you like to play Squeal of Fortune?")
    if play1 == "y" or play1 == "yes":
        return True
    else:
        return False


def letter():
    letter1 = input("Please guess a letter?")
