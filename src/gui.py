from tkinter import Tk, Frame, Entry, Button, Label, StringVar, Canvas, Text, constants
from heapq import heappop
from game_data import GameData
from word_fetcher import WordFetcher
from wordle import Wordle
from helpfullness import HelpFull

class WordleGui:
    def __init__(self, game_data: GameData):
        self.wordle = Wordle()
        self.game_data = game_data
        self.fetcher = WordFetcher()
        self.window = Tk()
        self.window.title("Eldrow")
        self.window.geometry("940x640")
        self.set_up_widgets()
        self.offset = 50
        self.guesses_left = 6

    def print_result(self, guess: str, colors: list):
        spacing = 30
        for i, letter in enumerate(guess):
            spacing += 40
            fill = colors[i]
            self.main_canvas.create_text(spacing, self.offset, text=letter.upper(), fill=fill, font=("Helvetica 32 bold"))
        self.offset += 50

    def get_result(self, guess: str):
        colors = ["gray", "gray", "gray", "gray", "gray"]
        assessment = self.wordle.give_assessment(guess)
        self.game_data.pipe_in_result_data(guess, assessment)
        for index in assessment["green"]:
            colors[index - 1] = "green"
        for index in assessment["yellow"]:
            colors[index - 1] = "yellow"
        self.guesses_left -= 1
        self.print_result(guess, colors)

    def submit(self, guess=None):#remember to clear hints when you guess a new word
        if guess == None:
            guess = self.guess.get()
        if len(guess) != 5:
            print("Wrong lenght of guess") # change so that button is only active when self.guess is lenght 5
        elif self.guesses_left < 1:
            print("No more guesses left!")
        else:
            self.get_result(guess)

    def get_helpfullness_list(self):
        helpfulness = HelpFull(self.fetcher)
        tuples = helpfulness.get_helpfullness_word_tuples()
        return tuples

    def parse_wordlist(self):
        heap = self.get_helpfullness_list()
        listed = []
        while len(heap) > 0:
            listed.append(heappop(heap)[1])
        return listed

    def clear_text_input(self):
        self.wordlist.delete("1.0","end")

    def display_wordlist(self):
        self.clear_text_input()
        words = self.parse_wordlist()
        for i, word in enumerate(words, 1):
            self.wordlist.insert(f"{str(i)}.1", word)

    def display_wordlist2(self):
        self.clear_text_input()
        words = self.fetcher.fetch_words(self.game_data)
        for i, word in enumerate(words, 1):
            self.wordlist.insert(f"{str(i)}.0", word + '\n')

    def autoguess(self):###########################################
        self.clear_text_input()
        words = self.parse_wordlist()
        self.submit(words[0])

    def set_up_widgets(self):
        self.high_frame = Frame(self.window)
        self.high_frame.pack(side=constants.TOP, pady=(20))
        self.main_label = Label(self.high_frame, text="Write your guess:")
        self.main_label.pack(side=constants.TOP)
        self.guess = StringVar(self.high_frame) #no packing right? since just var
        self.entry = Entry(self.high_frame, textvariable=self.guess)
        self.entry.pack(side=constants.TOP)
        self.submit_button = Button(self.high_frame, text="Submit", command=self.submit)
        self.submit_button.pack(side=constants.TOP)
        
        self.middle_frame = Frame(self.window)
        self.middle_frame.pack(side=constants.TOP, pady=10)
        self.middle_left = Frame(self.middle_frame)
        self.middle_left.pack(side=constants.LEFT)
        self.middle_middle = Frame(self.middle_frame)
        self.middle_middle.pack(side=constants.LEFT)
        self.middle_right = Frame(self.middle_frame, height=350, width=200)
        self.middle_right.pack(side=constants.LEFT, expand=False, padx=50)

        self.data_canvas = Canvas(self.middle_left, bg="white", height=350, width=200)
        self.data_canvas.pack(side=constants.TOP, padx=50)

        self.main_canvas = Canvas(self.middle_middle, bg="white", height=350, width=300)
        self.main_canvas.pack(side=constants.TOP)

        self.wordlist = Text(self.middle_right, height=20)
        self.wordlist.pack(side=constants.TOP, expand=False)

        self.low_frame = Frame(self.window)
        self.low_frame.pack(side=constants.TOP, pady=10)
        self.help_button = Button(self.low_frame, text="HELP", command=self.display_wordlist2)
        self.help_button.pack(side=constants.TOP, pady=10)
        self.ai_play_button = Button(self.low_frame, text="Let AI guess", command=self.autoguess)
        self.ai_play_button.pack(side=constants.TOP, pady=10)


    def play(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = WordleGui()
    gui.window.mainloop()
