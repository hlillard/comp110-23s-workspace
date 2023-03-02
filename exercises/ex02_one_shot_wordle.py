"""EX02 - One-Shot Wordle - Wordle with less guesses."""

__author__ = "730476613"

secret_word: str = "python"
word_idx: int = len(secret_word)
guessed_word: str = input(f"What is your {word_idx}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
gs_word_idx: int = 0
squares: str = ""
exs_var: bool = False
exs_idx: int = 0

while len(guessed_word) != len(secret_word):
    guessed_word = str(input(f"That was not {word_idx} letters! Try again: "))
while gs_word_idx < len(secret_word):
    if guessed_word[gs_word_idx] == secret_word[gs_word_idx]:
        squares = squares + GREEN_BOX
    else:
        exs_var = False
        exs_idx = 0
        while not exs_var and exs_idx < len(secret_word):
            if secret_word[exs_idx] == guessed_word[gs_word_idx]:
                exs_var = True
            else:
                exs_idx = exs_idx + 1
        if exs_var:
            squares = squares + YELLOW_BOX
        else:
            squares = squares + WHITE_BOX
    gs_word_idx = gs_word_idx + 1
print(squares)
if guessed_word == secret_word:
    print("Woo! You got it! ")
if guessed_word != secret_word:
    print("Not quite! Play again soon! ")