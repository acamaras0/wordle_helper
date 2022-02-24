import string
from game_data import GameData
from word_fetcher import WordFetcher
from wordle import Wordle

class WordleCli:
    def __init__(self, game_data: GameData):
        self.game_data = game_data
        self.wordle = Wordle()
        self.word_fetcher = WordFetcher()

    def _ask_for_position(self):
        position = 0
        while not 1 <= position <= 5:
            position = input(f"Position of letter (1-5): ")
            try:
                position = int(position)
            except TypeError:
                print("Usage: Give position of letter (between 1-5)")
            if not 1 <= position <= 5:
                print("Usage: Give position of letter (between 1-5)")
        return position

    def _ask_for_letters(self, letter_type: str, good_letters: dict):
        letter = ""
        while letter != '0':
            letter = input(f"{letter_type.capitalize()} letter: (0 for no more {letter_type} letters)")
            if letter not in string.ascii_letters + "0":
                print("Usage: Give one letter (or 0 for no more letters of this type)")
                continue
            if letter != "0":
                letter = letter.lower()
                if letter_type != "gray":
                    if letter in good_letters:
                        good_letters[letter] += 1
                    else:
                        good_letters[letter] = 1
                    position = self._ask_for_position()
                    if letter_type == "yellow":
                        self.game_data.letters[letter_type][position].append(letter)
                    else:
                        self.game_data.letters[letter_type][position] = letter
                else:
                    y_arrays = [] #this part should probably be refactored
                    for y_array in self.game_data.letters["yellow"].values():
                        y_arrays.append(y_array)
                    if letter not in y_arrays:
                        self.game_data.letters[letter_type].append(letter)
        return good_letters

    def get_wordle_result(self):
        good_letters = {}
        for letter_type in ["green", "yellow", "gray"]:
            good_letters = self._ask_for_letters(letter_type, good_letters)
        self.game_data.recheck_min_counts(good_letters)
        print(self.word_fetcher.fetch_words(self.game_data))

    def ask_for_guess(self):
        guess = input("Quess the 5 letter word:")
        print(self.wordle.give_assessment(guess))

"""
 ___________________________________________
/ It would be better if we had the asking    \ 
\ method call a method of game data to store /
 --------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||  
"""""""""""""""""""""""""""""""""""""""""""""


