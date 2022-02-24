from random import choice
from words import WordWrapper

class Wordle:
    def __init__(self):
        self.word = choice(WordWrapper().guessable_words)

    def _get_index_assessment(self, input_word: str):
        assessment = {"green": [], "yellow": []}
        used = []
        for key, letter in enumerate(input_word):
            if self.word[key] == letter:
                assessment["green"].append(key)
                continue
            for key2, letter2 in enumerate(self.word):
                if letter2 == letter and key2 not in assessment["green"] and key2 not in used:
                    assessment["yellow"].append(key)
                    used.append(key2)
        return assessment

    def give_assessment(self, input_word: str):
        assessment = self._get_index_assessment(input_word)
        for color in assessment:
            assessment[color] = [i + 1 for i in assessment[color]]
        return assessment
