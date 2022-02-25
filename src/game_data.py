
class GameData:
    def __init__(self):
        self.letters = {}
        self.letters["green"] = {}
        self.letters["yellow"] = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.letters["gray"] = []
        self.min_letter_counts = {}

    def recheck_min_counts(self, new_letters: dict):
        for key, value in new_letters.items():
            if key in self.min_letter_counts:
                self.min_letter_counts[key] = max(self.min_letter_counts[key], value)
            else:
                self.min_letter_counts[key] = value

    def pipe_in_result_data(self, word, assessment):
        checked = []
        good_letters = {}
        for color in assessment:
            for i in assessment[color]:
                letter = word[i - 1]
                self.letters[color][i] = letter
                checked.append(i)
                if letter not in good_letters:
                    good_letters[word[i-1]] = 1
                else:
                    good_letters[word[i-1]] += 1
        for key, value in enumerate(word, 1):
            if key not in checked:
                self.letters["gray"].append(value)
        self.recheck_min_counts(good_letters)
