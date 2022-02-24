
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
