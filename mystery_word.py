import random
import sys


def create_list_all_words(path='/usr/share/dict/words'):
    """Returns list of all the words in agruement path"""

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

    list_medium_words = []

    for word in all_words:

        if len(word) >= 6 and len(word) <= 8:
            list_medium_words.append(word)

    return list_medium_words


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


def main():
    pass

if __name__ == '__main__':
    main()
