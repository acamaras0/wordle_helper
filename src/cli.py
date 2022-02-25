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
        assessment = self.wordle.give_assessment(guess)
        if len(assessment["green"]) == 5:
            return True
        print(assessment)
        return False

    def play(self):
        count = 6
        mode = None

        while mode not in ["AI", "me"]:
            mode = input("Would you like to play the game yourself or let AI decide?(me/AI)")
        if mode == "AI":
            print("Well too bad, because that isn't implemented yet")
        print("\n")
        congratulations = {
            5: "Hey, that's suspiciously good... how did you know....?",
            4: "WHOA! AMAZING! YOU ARE ASTONISHINGLY GOOOOOOOOOOOOOOOOD at this",
            3: "Way better than average, congratulations!!!!!",
            2: "You're pretty good at this!",
            1: "Cutting close, but victory is a victory...",
        }

        victory = False
        while count > 0 and not victory:
            victory = self.ask_for_guess()
            if victory:
                print(congratulations[count])
                break
            self.get_wordle_result()
            print("\n")
            count -= 1


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


