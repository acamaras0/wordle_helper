import unittest
from word_fetcher import WordFetcher
from game_data import GameData
from words import WordWrapper

class TestWordFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = WordFetcher()
        self.gamedata = GameData()

    def test_fetch_words_returns_all_words_if_no_data(self):
        all_words = WordWrapper().guessable_words
        all_words.sort()
        fetched_words = self.fetcher.fetch_words(self.gamedata)
        fetched_words.sort()
        self.assertEqual(fetched_words, all_words)

    def test_fetch_words_does_not_return_words_with_gray_letters(self):
        self.gamedata.letters["gray"] = ['a', 'c', 'm', 'z', 'd']
        fetched_as_string = self.fetcher.fetch_words(self.gamedata)
        "".join(fetched_as_string)
        result = True
        for letter in self.gamedata.letters["gray"]:
            if letter in fetched_as_string:
                result = False
        self.assertEqual(result, True)

    def test_fetch_words_returns_only_words_with_green_letters_in_correct_places(self):
        self.gamedata.letters["green"] = {1: 'n', 4: 'b'}
        fetched = self.fetcher.fetch_words(self.gamedata)
        result = True
        for word in fetched:
            for i, letter in enumerate(word, 1):
                if i in self.gamedata.letters["green"] and letter != self.gamedata.letters["green"][i]:
                    result = False
        self.assertEqual(result, True)

    #def test_fetch_words_does_not_return_any_word_with_non_green_letter_on_green_letter_indes(self):

    def test_fetch_words_returns_only_words_with_all_the_yellow_letters(self):
        self.gamedata.letters["yellow"][2] = ['s', 'q']
        self.gamedata.letters["yellow"][4] = ['q']
        self.gamedata.letters["yellow"][5] = ['q', 'x', 's']
        fetched = self.fetcher.fetch_words(self.gamedata)
        result = True
        for word in fetched:
            for letter in "sqxs":
                if letter not in word:
                    result = False
        self.assertEqual(result, True)

    def test_fetch_words_does_not_return_any_yellow_letters_in_their_found_positions(self):
        self.gamedata.letters["yellow"][1] = ['a', 'm']
        self.gamedata.letters["yellow"][3] = ['p']
        self.gamedata.letters["yellow"][4] = ['s', 'p', 't']
        fetched = self.fetcher.fetch_words(self.gamedata)
        result = True
        for word in fetched:
            for key in [1, 3, 4]:
                for letter in self.gamedata.letters["yellow"][key]:
                    if word[key - 1] == letter:
                        result = False
        self.assertEqual(result, True)

    #def test_fetch_words_returns_words_with_at_least_given_counts_of_letters(self):


############################_validate_word######################################3

    def test_validate_word_returns_false_for_word_with_green_letter_not_appearing(self):
        self.gamedata.letters["green"][1] = "b"
        self.assertEqual(self.fetcher._validate_word("green", self.gamedata), False)

    def test_validate_word_returns_false_for_word_with_green_letter_in_wrong_spot(self):
        self.gamedata.letters["green"][1] = "b"
        self.assertEqual(self.fetcher._validate_word("dbbbb", self.gamedata), False)

    def test_validate_word_returns_false_for_word_with_not_all_yellow_letters(self):
        self.gamedata.letters["yellow"][2] = ['s', 'q']
        self.gamedata.letters["yellow"][4] = ['q']
        self.gamedata.letters["yellow"][5] = ['q', 'x', 's']
        self.assertEqual(self.fetcher._validate_word("qaxmi", self.gamedata), False)
