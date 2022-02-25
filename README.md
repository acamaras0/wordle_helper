# Wordle Clone, Assistant and Solver

## REQUIREMENTS

- A system with an installation of the programming language Python and its dependency management tool poetry

- Python = https://www.python.org/downloads/
- poetry = https://python-poetry.org/docs/

## INSTALLATION:

Clone repository and run this line of bash in repo root folder to install dependencies:

```bash
poetry install
```

## USAGE:

Start game by running this line of bash in the repo root folder:

```bash
poetry run invoke start
```

## PLAYING GUIDE:

To be written...

## TESTS

Run unit tests by running this line of bash in the repo root folder:

```bash
poetry run invoke test
```

Test case source code can be found from the src/tests -folder

To see test coverage you can run:

```bash
poetry run invoke coverage
```

And to generate a HTML coverage report you can run:

```bash
poetry run invoke coverage-report
```

## AI STRATEGY AND MEASURING IT

The AI player feature is very simple, but performance was so bad that it was replaced by very bad AI version last minute to have at least something...

This method could be used together with some data structure to store the model of behavior in a tree etc. so that no calculations would happen realtime.

- First time it will always try the word "raise"
- On every try after that, it will calculate the average information value that may be gained from guessing any specific word
- It chooses the word with the highest average information gain
- The way it calculates the information gain is by utilizing the classes and functions in the code to see how many words would remain after each pair of possible correct word and a quess. Then it averages out the count and the lower the count is, the better the information value

- The way to measure effectiveness of a strategy in this game is to run simulations and see how many guesses does it take to win on average with the strategy. The lower the average, the better strategy
- Assuming any word in the legal words has equal likelihood of being the chosen word, finding out the potential information gain from a guess and comparing them is the optimal strategy, since with the given information the likelihood of each guess of being the correct answer is equal.

## BONUSES 

- Game implemented
- Unittests have been implemented on the program to test specific features and measurements in the effectiveness of the AI strategy can be conducted by running simulations (invoke rule to run simulations yet to be implemented though... unless this note in brackets is old info...)
- Wordle can be cheated by looking at what word is coming next from the webpages source code.
