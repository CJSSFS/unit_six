# Chad Scott
# 10/29/18
# This program is a Wheel Of Fortune game that has the user guess letters and gets them to guess the correct word


import random


def play():
    play1 = input("Would you like to play Squeal of Fortune?")
    if play1 == "y" or play1 == "yes":
        return True
    else:
        return False


def get_word():
    """
    This function gets a random word from a list of words and displays it in blanks when the program is run
    :return:
    """
    my_file = open("wordfile.txt", "r")
    word = my_file.readlines()
    my_file.close()
    my_word = random.choice(word)
    my_word = my_word[:-1]
    return my_word


def main():
    answer = get_word()
    word = []
    attempts = 6
    letters_guessed = []
    for x in range(len(answer)):
        word.append("_")
    print(word)
    while True:
        if attempts == 0 or "_" not in word:
            break
        print("You have",  attempts,  "remaining")
        letter = input("Please guess a letter:")
        letters_guessed.append(letter)
        if letter in answer:
            for x in range(len(answer)):
                if letter == answer[x]:
                    word[x] = letter
        else:
            attempts = attempts - 1
            print("That letter is not in the word")
        print(word)
        print("Letters Guessed", letters_guessed)
    if attempts == 0:
        print("You lose :( Try again")
        print(answer)
    else:
        print("You solved it!!!")


main()







