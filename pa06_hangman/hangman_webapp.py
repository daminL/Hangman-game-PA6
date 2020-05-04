"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app

app = Flask(__name__)

global state
state = {'guesses': [],
         'word': "",
         'done': False,
         'letter_guessed': "",
         'correct_letters': [],
         'found_all_letters': False,
         'all_letters_found': "",
         'not_in_word': "",
         'letter_in_word': "",
         'dashes': ""}


@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')


@app.route('/about')#about the team
def aboutdamin():
    return render_template('about.html')


@app.route('/start')
def play():
    global state
    state['rw'] = hangman_app.generate_random_word()
    state['guesses'] = []
    return render_template("start.html", state=state)


@app.route('/play', methods=['GET', 'POST'])
def hangman():
    """ plays hangman game """
    global state

    if request.method == 'GET':
        return play()

    elif request.method == 'POST':
        letter = request.form['guess']
        state['letter_guessed'] = ""
        state['all_letters_found'] = ""
        state['not_in_word'] = ""
        state['letter_in_word'] = ""
        state['dashes'] = ""

        if letter in state['guesses']:
            state['letter_guessed'] = "That letter has already been guessed. Guess again!"
        if letter in state['rw']:
            state['correct_letters'] += letter
            state['letter_in_word'] = "That letter is in the word! You are one step closer to getting the word!"
            for i in state['rw']:
                if i not in state['correct_letters']:
                    state['found_all_letters'] = False
                    break
                else:
                    state['found_all_letters'] = True
            if state['found_all_letters'] == True:
                state['all_letters_found'] = "You got it! You guessed the word!"
                state['letter_in_word'] = ""
        else:
            state['not_in_word'] = "Poop! the letter guessed is not in the word! Try again!"

        state['guesses'] += [letter]

        for d in state['rw']:
            if d in state['guesses']:
                state['dashes'] += d
            else:
                state['dashes'] += '-'
        return render_template('play.html', state=state)


if __name__ == '__main__':
    app.run('localhost', port=5000)
