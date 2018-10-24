import random


def play():
    play1 = input("Would you like to play Squeal of Fortune?")
    if play1 == "y" or play1 == "yes":
        return True
    else:
        return False


def get_word():
    word = ["harry", "ron", "hermione", "ginny", "fred", "neville", "draco"]
    my_word = random.choice(word)
    return my_word


def main():
    get_word()
    answer = get_word()
    word = []
    for x in range(len(answer)):
        word.append("_")
    print(word)
    while True:
        letter = input("Please guess a letter:")
        for x in range(len(answer)):
            if letter == answer[x]:
                word[x] = letter
        print(word)

        if answer == word:
            print("You solved it!!!")



main()







