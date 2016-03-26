# experimental initial version of spanish command line game
# author: Thomas Johnson

import csv
import numpy
import time


# frequency list representing state of game
game_list = []


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


def populate_list(guess_lang, total_word_num):
    with open('full_list.txt', newline='', encoding='utf-8') as span_file:
        reader = csv.reader(span_file, delimiter='\t')
        for row_num, row in enumerate(reader):
            if row_num > total_word_num:
                return
            else:
                if guess_lang == 's':
                    game_list.append((row[2], row[1]))
                else:
                    game_list.append((row[1], row[2]))


def main():
    guess_lang, total_word_num = initial_prompt()
    populate_list(guess_lang, total_word_num)
    for i in range(0, len(game_list)):
        print(game_list[i])


if __name__ == '__main__':
    main()

