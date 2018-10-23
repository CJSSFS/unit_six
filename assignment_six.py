import random


def get_word():
    word = ["Harry", "Ron", "Hermione", "Ginny", "Fred", "Neville", "Draco"]
    my_word = random.choice(word)
    return my_word

def play():
    play1 = input("Would you like to play Squeal of Fortune?")
    if play1 == "y" or play1 == "yes":
        return True
    else:
        return False


def main():
    answer = get_word()
    letter = input("Please guess a letter:")
    word = []
    for x in range(len(answer)):
        word.append("_")


main()







