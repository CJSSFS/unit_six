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
        if letter in answer:
            for x in range(len(answer)):
                if letter == answer[x]:
                    word[x] = letter
        else:
            attempts = attempts - 1
            print("That letter is not in the word")
        print(word)
        print(letters_guessed)

        if answer == word:
            print("You solved it!!!")


main()







