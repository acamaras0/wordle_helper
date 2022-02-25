import unittest
from wordle import Wordle

class TestWordle(unittest.TestCase):
    def setUp(self):
        self.wordle = Wordle()
        self.mock_input = "dinga"
        self.mock_return = {"green": [], "yellow": []}

    def test_give_assessment_returns_dict_of_len_2(self):
        self.assertEqual(2, len(self.wordle.give_assessment(self.mock_input)))

    def test_give_assessment_returns_dict_with_key_green_val_list(self):
        self.assertIsInstance(self.wordle.give_assessment(self.mock_input)["green"], list)

    def test_give_assessment_returns_dict_with_key_green_val_list(self):
        self.assertIsInstance(self.wordle.give_assessment(self.mock_input)["yellow"], list)

    def test_give_assessment_returns_fully_gray(self):
        self.wordle.word = "lungs"
        self.assertEqual(self.mock_return, self.wordle.give_assessment("aaaaa"))

    def test_give_assessment_returns_all_yellows(self):
        self.wordle.word = "grime"
        self.mock_return["yellow"] = [1, 2, 3, 4, 5]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("rgeim"))

    def test_give_assessment_returns_all_green(self):
        self.wordle.word = "grime"
        self.mock_return["green"] = [1, 2, 3, 4, 5]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("grime"))

    def test_give_assessment_returns_one_yellow_with_multiple_matching_same_one(self):
        self.wordle.word = "girme"
        self.mock_return["yellow"] = [1]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("rrara"))

    def test_give_assessment_returns_only_one_green_even_if_letter_earlier(self):
        self.wordle.word = "grime"
        self.mock_return["green"] = [2]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("rrara"))

    def test_give_assessment_returns_just_green_1_when_first_green(self):
        self.wordle.word = "grime"
        self.mock_return["green"] = [1]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("ghost"))

    def test_give_assessment_returns_four_greens(self):
        self.wordle.word = "grime"
        self.mock_return["green"] = [2, 3, 4, 5]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("prime"))

    def test_give_assessment_returns_three_yellows_and_one_green(self):
        self.wordle.word = "grime"
        self.mock_return["green"] = [2]
        self.mock_return["yellow"] = [3, 4, 5]
        self.assertEqual(self.mock_return, self.wordle.give_assessment("prmei"))

    def test_assessment_does_not_have_same_indices_for_yellow_and_green(self):
        self.wordle.word = "sflis"
        self.mock_return["green"] = [1]
        self.mock_return["yellow"] = [4]
        self.assertEqual(self.wordle.give_assessment("sgnsg"), self.mock_return)
