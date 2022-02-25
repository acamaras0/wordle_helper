from heapq import heappop, heappush
from random import choice
from copy import copy
from word_fetcher import WordFetcher
from game_data import GameData
from wordle import Wordle

class HelpFull:
    """Class to rank words into heap by usefullness
    """
    def __init__(self, fetcher: WordFetcher):
        self.fetcher = fetcher
        self.helpfuls = 0
        self.wordle = Wordle()

    def _skim_input(self, wordlist):
        skimmed = []
        for i in range(10):
            skimmed.append(choice(wordlist))
        return skimmed

    def _get_helpfullness_for_case(self, guess: str, true_word: str):
        gamedata = GameData()
        self.wordle.word = true_word
        assessment = self.wordle.give_assessment(guess)
        gamedata.pipe_in_result_data(guess, assessment)
        self.helpfuls += 1
        if self.helpfuls > 5500:
            print(f"{self.helpfuls=}")
            exit()
        thing = len(self.fetcher.fetch_words_no_change(gamedata))
        print(thing)
        return thing

    def _assign_word_helpfullness(self, guess: str):
        helpfullness = []
        sampling = self._skim_input(self.fetcher.guessable_words)
        for word in sampling:
            helpfullness.append(self._get_helpfullness_for_case(guess, word))
        return sum(helpfullness) / len(helpfullness)

    def get_helpfullness_word_tuples(self):
        """Generates a list hashed by tuples into heapq in order of best guess

        Returns:
            list of tuples: Tuples of (usefullness, heapq) where low is better
        """
        words_by_helpfullness = []
        lista = self._skim_input(copy(self.fetcher.guessable_words))
        for word in lista:
            value = self._assign_word_helpfullness(word)
            heappush(words_by_helpfullness, (value, word))
        return words_by_helpfullness
