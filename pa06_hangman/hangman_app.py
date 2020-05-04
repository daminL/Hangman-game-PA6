"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random


def generate_random_word():
    wordbank = "text", "document", "fedora", "league", "legends", "dungeons" "dragons", "pokemon", "smash", "mathematics", "economics", "timber", "kesha", "papers", "Irving", "hope", "your", "enjoying", "quarantine"
    rw = random.choice(wordbank)
    return rw


def play_hangman():
    playing = True

    while (playing):
        guessed_letters = []
        correct_letters = []
        guesses_left = 5
        rw = generate_random_word()
        letter = input("Pick a letter:")
        done = False
        while not done or guesses_left > 0:
            if letter in guessed_letters:
                guesses_left -= 1
                print("You have already guessed the letter", letter,
                      ".")
            elif letter not in list(rw):
                guessed_letters += letter
                print(letter, "is not in the word.")
                guesses_left -= 1
                print("You have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")
            else:
                guessed_letters += letter  # add letter to guessed letters
                correct_letters += letter
                print(letter, "is in the word!")  # tell user the letter is in the word
                print("You have guessed:", guessed_letters)
                print("You have", guesses_left, "guesses left.")
            if guesses_left == 0:  # the number of guesses left is zero
                done = True  # set done to be true and tell the user they lost!
                print("You ran out of guesses. Sorry, you lost :(")
            else:
                dashes = []
                for d in rw:
                    if d in guessed_letters:
                        dashes += d
                    else:
                        dashes += '-'
                print(dashes)
                print()
            foundAllLetters = True
            for i in range(len(rw)):
                if rw[i] not in correct_letters:
                    foundAllLetters = False
                    letter = input("Pick a letter:")  # ask the user for another letter
                    break
            if foundAllLetters:
                print("The word was", rw + ". You got the word! You won!")
                done = True
                break
        want_to_play = input(
            "Would you like to play again?[y]/[n]")
        if want_to_play == "y":
            playing = True
        elif want_to_play == "n":
            playing = False
            print("Thank you for playing and stay safe and healthy!")


if __name__ == '__main__':
    play_hangman()
