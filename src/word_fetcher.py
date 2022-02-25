import heapq
from game_data import GameData
from words import WordWrapper

class WordFetcher:
    def __init__(self):
        self.guessable_words = WordWrapper().guessable_words
        heapq.heapify(self.guessable_words)

    def _validate_word(self, word: str, gamedata: GameData):
        """Checks if a word is still a valid guess

        Args:
            word (str): the word to be checked
            gamedata (GameData): Information game has given about letters

        Returns:
            bool: True if word can be used, otherwise False
        """
        letter_data = gamedata.letters
        for key, value in enumerate(word, 1):
            if key in letter_data["green"] and value != letter_data["green"][key]:
                return False
            if value in letter_data["yellow"][key]:
                return False
            if value in letter_data["gray"]:
                return False
        for key, value in gamedata.min_letter_counts.items():
            if word.count(key) < value:
                return False
        for list in letter_data["yellow"].values():
            for letter in list:
                if letter not in word:
                    return False
        return True

    def fetch_words(self, gamedata: GameData):
        found = []
        while len(self.guessable_words) > 0:
            word = heapq.heappop(self.guessable_words)
            if self._validate_word(word, gamedata):
                heapq.heappush(found, word)
        self.guessable_words = found
        return self.guessable_words

    def fetch_words_no_change(self, gamedata: GameData):
        found = []
        store = []
        while len(self.guessable_words) > 0:
            word = heapq.heappop(self.guessable_words)
            if self._validate_word(word, gamedata):
                heapq.heappush(found, word)
            heapq.heappush(store, word)
        self.guessable_words = store
        return found
