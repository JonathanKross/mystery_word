import random
import sys


def create_list_all_words(path='/usr/share/dict/words'):
    """
    Returns list of all the words in agruement path.
    Path or input must contain words set to individual lines.
    """

    with open(path, 'r') as file:

        all_words = []

        for word in file:
            all_words.append(word.strip())

        return all_words


def list_easy_words(all_words):
    """Returns list of words only containing 4-6 characters."""

    list_easy_words = []

    for word in all_words:

        if len(word) >= 4 and len(word) <= 6:
            list_easy_words.append(word)

    return list_easy_words


def list_normal_words(all_words):
    """Returns list of words only containing 6-8 characters."""

    list_normal_words = []

    for word in all_words:

        if len(word) >= 6 and len(word) <= 8:
            list_normal_words.append(word)

    return list_normal_words


def list_hard_words(all_words):
    """Returns a list of words only containing 8+ characters."""

    list_hard_words = []

    for word in all_words:

        if len(word) >= 8:
            list_hard_words.append(word)

    return list_hard_words


def generate_random_word(all_words):
    """Returns a random word from inputted words list."""

    return random.choice(all_words)

def choose_difficulty():
    """Prompts user to select easy, normal, or hard mode."""

    return input("What mode to you want to play in? Easy[e], Normal[n], or Hard[h]: ").lower().strip()


def guess_letter():
    """Prompts user to for a letter to guess"""

    return input("Guess a letter. ").lower().strip()



def main():
    print("Welcome to Mystery Word Game!")
    print("You're allowed 8 chances to guess all of the letters in the mystery word.")

    difficulty = choose_difficulty()

    if difficulty == 'e':
        mystery_word = generate_random_word(list_easy_words(create_list_all_words()))

    elif difficulty == 'n':
        mystery_word = generate_random_word(list_normal_words(create_list_all_words()))

    elif difficulty == 'h':
        mystery_word = generate_random_word(list_hard_words(create_list_all_words()))

    print(mystery_word)
    # while True:
    #
    #     letter_ guess = guess_letter()
    #
    #
    #
    #
    #     play_again = input("Do you want to play Mystery Word again? [y/N] \n")
    #     if play_again.lower().strip() == "y"
    #         main()
    #     else:
    #         sys.exit()

if __name__ == '__main__':
    main()
