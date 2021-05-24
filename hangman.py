# Hangman
# This is probably the hardest one out of these 6 small projects. This will be similar to guessing the number,
# except we are guessing the word. The user needs to guess letters,
# Give the user no more than 6 attempts for guessing wrong letter. This will mean you will have to have a counter.
# You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a random word to use.
import sys

guess_count = 0

word = input("Enter secret word: ")
word_len = len(word)
hidden = list("_" * word_len)

while True:
    guess = input("Letter: ")
    if guess == word:
        print("Brawo! Wygrałeś :D")

    if guess in word:
        print("Dobrze")
        for i in range(0, word_len):
            if guess == word[i]:
                hidden[i] = guess
    else:
        print("Źle...")

    wynik = ""
    for i in hidden:
        wynik += i
    print(wynik)

    if wynik == word:
        print("Brawo! Wygrałeś :D")
        break
