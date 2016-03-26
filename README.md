# Spanish Guesser

A command line game to study the 2000 most frequently occuring spanish words.

Source for spanish frequency list: http://www.101languages.net/spanish/most-common-spanish-words/

__Usage__: Navigate to the spanish\_guesser directory and type: `python game1.py`.

__Dependencies__: [numpy](http://www.numpy.org/)

The game uses a frequency list of the most frequently occuring spanish words. As the game is played, new words are selected based on their frequency, where more frequently occuring words are more likely to be selected. This is done by drawing the next word from an [exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution).

If the player guesses a word correctly two times in a row, then that word is removed from the frequency list. Once the frequency list is empty, the player wins.
