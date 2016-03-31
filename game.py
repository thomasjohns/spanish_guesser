# experimental initial version of spanish command line game
# author: Thomas Johnson


import csv
import numpy
import time
import random


# frequency list representing state of game
game_list = []
# dictionary keeping track of the number of correct guesses in a row for
# each word
gc_dict = {}
# keep track of the total number of correct guesses the user has made
words_completed = 0


def initial_prompt():
    """
    Welcome user to new game and get information about the number of words
    to play with and the language to guess in. Return the language to guess
    in as a string ('s' for Spanish or 'e' for English) and the total words
    to play with (int).
    """
    print("\nWelcome to Spanish Guesser!\n")
    # time.sleep(1)
    print("How many words would you like to play with?\n")
    # time.sleep(1)
    total_word_num = input("Enter a number between 1 and 2000 and press enter: ")
    print("\nWould you like to guess Spanish words from English words? (type s)")
    print("Or English words from Spanish words? (type e)\n")
    # time.sleep(1)
    guess_lang = input("Please type s or e: ")
    return guess_lang, int(total_word_num)


def populate_game_list(guess_lang, total_word_num):
    """
    Populate global list of Spanish English pairs of words. The number
    of pairs is specified by the player (total_word_num) and the order
    of the pairs (guess_lang) is either 's' or 'e'.

    Game list of length 5 if 's' is given:
    [('from', 'de'),
     ('what', 'que'),
     ('do not', 'no'),
     ('to', 'a'),
     ('the', 'la')]

    Game list of length 5 if 'e' is given:
    [('de', 'from'),
     ('que', 'what'),
     ('no', 'do not'),
     ('a', 'to'),
     ('la', 'the')]
    """
    with open('full_list.txt', newline='', encoding='utf-8') as span_file:
        reader = csv.reader(span_file, delimiter='\t')
        for row_num, row in enumerate(reader):
            if row_num >= total_word_num:
                return
            else:
                if guess_lang == 's':
                    # (English, Spanish)
                    game_list.append((row[2], row[1]))
                else:
                    # (Spanish, English)
                    game_list.append((row[1], row[2]))


def initialize_guess_count_dict():
    """
    Set the number of correct guesses in a row to 0 for each word in the
    guess count dictionary.
    """
    for pair in game_list:
        gc_dict[pair[1]] = 0


def get_index(used_index=None):
    """
    Return an index to select a Spanish English pair from the game list.
    The index is chosen randomly from an exponential distribution following
    the formula:

    (2/N)*exp(-2*x/N)

    rounded down to the nearest integer, where N is the length of the game
    list.

    The optional input parameter (used_index) will assure that the returned
    index is not the same as used_index.
    """
    index = int(numpy.random.exponential(scale=len(game_list)/2))
    if index > len(game_list) - 1:
        index = len(game_list) - 1
    if used_index is None or index != used_index:
        return index
    elif index == 0:
        return 1
    else:
        return index - 1


def play_round():
    """
    Play one round of the game i.e. let the player try to translate
    a word.
    """
    global words_completed
    correct_index = get_index()
    indices_list = []
    indices_list.append(correct_index)
    for i in range(0, min(len(game_list), 3)):
        indices_list.append(get_index(correct_index))
    print('\nTranslate: {0}\n'.format(game_list[correct_index][0]))
    random.shuffle(indices_list)
    letters = ['a', 'b', 'c', 'd']
    for i, index in enumerate(indices_list):
        print('{0}: {1}'.format(letters[i], game_list[index][1]))
    letter = input('\nType a, b, c, or d: ')
    if letter not in letters:
        letter = 'a'
    guess = game_list[indices_list[letters.index(letter)]][1] 
    correct_guess = game_list[correct_index][1]
    if guess == correct_guess:
        print('\nCorrect!!!\n')
        if gc_dict[guess] == 0:
            gc_dict[guess] = 1
        else:
            del game_list[correct_index]
            words_completed += 1
    else:
        print('\nIncorrect')
        print('The correct translation was ({0}).\n'.format(correct_guess))


def main():
    guess_lang, total_word_num = initial_prompt()
    populate_game_list(guess_lang, total_word_num)
    total_words = total_word_num
    initialize_guess_count_dict()
    while len(game_list) > 1:
        play_round()
        print('{0} out of {1} words completed\n'.format(words_completed,
                                                        total_words))
    print('\nYOU WIN!\n')
    print('The last word was ({0}), which '.format(game_list[0][0]) +
          'translates to ({1}).'.format(game_list[0][1]))


if __name__ == '__main__':
    main()

