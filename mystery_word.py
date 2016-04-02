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


def generate_mystery_word(difficulty):
    """Pass user selected difficulty and generates the mystery word"""

    if difficulty == 'e':
        return generate_random_word(list_easy_words(create_list_all_words()))

    elif difficulty == 'n':
        return generate_random_word(list_normal_words(create_list_all_words()))

    elif difficulty == 'h':
        return generate_random_word(list_hard_words(create_list_all_words()))


def guess_letter(correct_guesses, incorrect_guesses):
    """Prompts user for a letter to guess"""

    letters = "abcdefghijklmnopqrstuvwxyz"
    while True:

        guess_attempt = input("Guess a letter: ").lower().strip()

        if len(guess_attempt) >= 2 or guess_attempt == "":
            print("Looks like that's not a single letter. Try again.")
            continue

        elif guess_attempt in correct_guesses or guess_attempt in incorrect_guesses:
            print("Looks like you've already guessed that letter. Try again.")
            continue

        elif guess_attempt not in letters:
            print("Looks like you didn't guess a letter. Don't guess numbers or special characters.")
            continue

        else:
            return guess_attempt

def display_visual_guesses(mystery_word):

    for letter in mystery_word:
        if letter in correct_guesses:
            print(letter, end="")
        else:
            print("_", end="")



def main():

    max_number_guesses = 8
    correct_guesses = []
    incorrect_guesses = []

    print("Welcome to Mystery Word Game!")
    print("You're allowed 8 chances to guess all of the letters in the mystery word.")

    mystery_word = generate_mystery_word(choose_difficulty())

    print("Your mystery word has {} letters.\n".format(len(mystery_word)))

    while True:

        # display_visual_guesses(mystery_word)

        while len(incorrect_guesses) < max_number_guesses and len(correct_guesses) != len(list(mystery_word)):

            # print("_ " * len(mystery_word))
            for letter in mystery_word:
                if letter in correct_guesses:
                    print(letter, " ", end="")
                else:
                    print("_ ", end="")

            print("\n")

            letter_guessed = guess_letter(correct_guesses, incorrect_guesses)

            if letter_guessed in mystery_word:
                correct_guesses.append(letter_guessed)
                if len(correct_guesses) == len(list(mystery_word)):
                    print("Congrats! You won! The mystery word was {}.".format(mystery_word))
            else:
                incorrect_guesses.append(letter_guessed)

            print("\nIncorrect Guesses: {} out of {}\n".format(len(incorrect_guesses), max_number_guesses))
            # display_visual_guesses(mystery_word, letter_guessed)





        else:
            print("You're out of guesses!. Your mystery word was {}.".format(mystery_word))

        play_again = input("Do you want to play Mystery Word again? [y/N] \n")

        if play_again.lower().strip() == "y":
            main()

        else:
            sys.exit()




if __name__ == '__main__':
    main()
