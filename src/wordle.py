from random import choice
from words import WordWrapper

class Wordle:
    def __init__(self, word=None):
        if not word:
            self.word = choice(WordWrapper().guessable_words)
        else:
            self.word = word

    def _get_index_assessment(self, input_word: str):
        assessment = {"green": [], "yellow": []}
        used = []
        for key, letter in enumerate(input_word):#all greens have to be checked first
            if self.word[key] == letter:
                assessment["green"].append(key)
        for key, letter in enumerate(input_word):
            for key2, letter2 in enumerate(self.word):
                if letter2 == letter and key2 not in assessment["green"] and key not in assessment["green"] and key2 not in used:
                    assessment["yellow"].append(key)
                    used.append(key2)
        return assessment

    def give_assessment(self, input_word: str):
        """ (change this to not be give -> confusing)

        Args:
            input_word (str): _description_

        Returns:
            _type_: _description_
        """
        assessment = self._get_index_assessment(input_word)
        for color in assessment:
            assessment[color] = [i + 1 for i in assessment[color]]
        return assessment
