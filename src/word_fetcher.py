import heapq
from game_data import GameData
from words import WordWrapper

class WordFetcher:
    def __init__(self):
        self.guessable_words = WordWrapper().guessable_words
        heapq.heapify(self.guessable_words)

    def _validate_word(self, word: str, gamedata: GameData):
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
        return True

    def fetch_words(self, gamedata: GameData):
        found = []
        while len(self.guessable_words) > 0:
            word = heapq.heappop(self.guessable_words)
            if self._validate_word(word, gamedata):
                heapq.heappush(found, word)
        self.guessable_words = found
        return self.guessable_words

"""
 __________________________________________
/ We would get much faster fetching if we   \ 
\ had a better data struct for words        /
 -------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||  
"""""""""""""""""""""""""""""""""""""""""""""


