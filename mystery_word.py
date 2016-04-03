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
            all_words.append(word.strip().upper())

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


def generate_random_word(list_of_words):
    """Returns a random word from inputted words list."""

    return random.choice(list_of_words)


def choose_difficulty():
    """Prompts user to select easy, normal, or hard mode."""

    while True:

        difficulty = input("What mode to you want to play?\nEasy[e], Normal[n], or Hard[h]: ").lower().strip()

        if difficulty not in 'enh' or difficulty == "":
            print("\nType 'e' for Easy, 'n' for Normal, 'h' for Hard.\n")
            continue

        else:
            return difficulty

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

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:

        guess_attempt = input("Guess a letter: ").upper().strip()

        if len(guess_attempt) >= 2 or guess_attempt == "":
            print("Looks like that's not a single letter. Try again.\n")

        elif guess_attempt in correct_guesses or guess_attempt in incorrect_guesses:
            print("Looks like you've already guessed that letter. Try again.\n")

        elif guess_attempt not in alphabet:
            print("Looks like you didn't guess a letter. Don't guess numbers or special characters.\n")

        else:
            return guess_attempt


def display_visual_guesses(mystery_word, correct_guesses):
#found how to not print a newline on every print statement here:
#https://stackoverflow.com/questions/493386/how-to-print-in-python-without-newline-or-space
    # visual = ""
    for letter in mystery_word:

        if letter in correct_guesses:
            print(letter.upper(), end=" ")
            # visual += letter

        else:
            print("_", end=" ")
            # visual += "_"

    # return visual


def update_guess_lists(letter_guessed, mystery_word, correct_guesses, incorrect_guesses):

    if letter_guessed in mystery_word:
        correct_guesses.append(letter_guessed)

    else:
        incorrect_guesses.append(letter_guessed)


def is_word_complete(mystery_word, correct_guesses):

    game_won = False
    for letter in mystery_word:
        if letter not in correct_guesses:
            game_won = False
            break
        elif letter in correct_guesses:
            game_won = True
            continue
    if game_won == True:
        print("Congrats! You won! The mystery word was {}.".format(mystery_word))
        play_again()


def play_again():

    play_again = input("Do you want to play Mystery Word again? [y/N] \n")

    if play_again.lower().strip() == "y":
        main()

    else:
        sys.exit()


def main():

    max_number_guesses = 8
    correct_guesses = []
    incorrect_guesses = []

    print("Welcome to Mystery Word Game!")
    print("You're allowed 8 chances to guess all of the letters in the mystery word.")

    mystery_word = generate_mystery_word(choose_difficulty())

    print("\nYour mystery word has {} letters.\n".format(len(mystery_word)))

    while len(incorrect_guesses) < max_number_guesses and len(correct_guesses) != len(list(mystery_word)):

        display_visual_guesses(mystery_word, correct_guesses)

        print()

        letter_guessed = guess_letter(correct_guesses, incorrect_guesses)
        update_guess_lists(letter_guessed, mystery_word, correct_guesses, incorrect_guesses)
        is_word_complete(mystery_word, correct_guesses)

        print("\nIncorrect Guesses: {} out of {}\n".format(len(incorrect_guesses), max_number_guesses))

    else:
        print("You're out of guesses!. Your mystery word was {}.".format(mystery_word))

    play_again()


if __name__ == '__main__':
    main()
