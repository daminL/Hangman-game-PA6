# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:36:51 2020

@author: zzipk
"""
"PRINTER OF ALL PRINTERS"
def poap(choices, listylistylisty):
    print('-----------')
    print(listylistylisty)
    print(str(choices)+" choices left")
def playagain(yes_no):
    if ord(yes_no)==89 or ord(yes_no)==121:
        return True
    else:
        return False
def cvi1(a):
    if len(a)==1:
        if ord(a)==89 or ord(a)==121 or ord(a)==78 or ord(a)==110:
            return True
        else:
            return False
    else:
        return False
def guessLetter(rw, ans):
    for w in range(len(rw)):
        if ord(rw[w])==ord(ans) or ord(rw[w])==ord(ans)+32 or ord(rw[w])==ord(ans)-32:
            "print('Done')"
            return True
    else:
        return False
"guessLetter('Bannana','n')"
def win_checker(word,l):
    length=len(word)
    counter=0
    for i in range(len(l)):
        if (ord(l[i])>=65 and ord(l[i])<91) or (ord(l[i])>=97 and ord(l[i])<123):
            "if letter"
            counter+=1
    if counter==length:
        return True
    else:
        return False
def reveal(letter,word,listy_list):
    for i in range(len(word)):
        if ord(word[i])==ord(letter) or ord(word[i])==ord(letter)+32 or ord(word[i])==ord(letter)-32:
            listy_list[i]=letter
    return listy_list
def dash(rw):
    l=[]
    for r in rw:
        l.append('-')
    return l
def cvi(a,bank):
    "check that it is a single input"
    if len(a)==1:
        "check that the input is either an upper or lowercase letter"
        if (ord(a)>=65 and ord(a)<91) or (ord(a)>=97 and ord(a)<123):
            "check that the letter is not in the bank"
            for i in range(len(bank)):
                "for all things in the bank, is the thing entered in the bank"
                if ord(a)==ord(bank[i]) or ord(a)==ord(bank[i])+32 or ord(a)==ord(bank[i])-32:
                    "32 is the difference between upper and lower case characters in html"
                    return False
            "we want a single letter entry, that has not been given before"
            return True
        else: 
            return False
    else: 
        return False
cvi("a",["a"])
cvi("a",["A"])
import random as rand
def generate_random_word():   
    with open("wordbank.txt","r") as bank:
        mywords=[word.strip() for word in bank]
        rw=rand.choice(mywords)
        return rw
"generate_random_word()"
def play_hangman():
    valid_input_check=False
    "setting up a while loop for a valid input letter"
    want_to_play=True
    "overall while loop for continued play"
    while want_to_play:
        rw=generate_random_word()
        "print(rw)"
        word=rw
        "generate random word basically"
        l=dash(rw)
        won=False
        "need a var for winning"
        choices=6
        bank=[]
        "we need print thing for a blank, bank right here"
        while not won and choices>0:
            "comment so basically this is a check for if you have won(reveal) lost(choices)"
            valid_input_check=False
            "checks if letter is a valid entry"
            poap(choices,l)
            while not valid_input_check:
                    "while it's false pick a letter, check if its valid"
                    letter=input("pick a letter:")
                    "if not valid have them try inputting again"
                    if cvi(letter,bank):
                        "checks that it is a single unguessed letter"
                        bank.append(letter)
                        "if so add it to the bank"
                        if guessLetter(word,letter):
                            "check letter in word function"
                            l=reveal(letter,word,l)
                            "print formatted thing"
                            if win_checker(word,l):
                                won=True
                                valid_input_check=True
                            else:
                                won=False
                                valid_input_check=True
                        else:
                            valid_input_check=True
                            choices-=1
                            "Print formatted stuff"            
                    else:
                        print("I'm sorry that was not a valid letter please enter it again")
                        valid_input_check=False
                        "if it's not valid then ask for it again"
        play_again_input_check=True
        "checks for valid input when display says play again"
        if not won:
            "once you end either by guessing all letters or losing all choices"
            "check how much of word revealed, if not all revealed they lose"
            print("You lost")
        else:
            print("You won")
            "otherwise they win"
        while play_again_input_check:
            yes_no=input("want to play again yes, no? y or n:")
            if cvi1(yes_no):
                "check if input is a single letter and y or n"
                if playagain(yes_no):
                    "play another round or not"
                    play_again_input_check=False
                    want_to_play=True
                    "restarts the game"
                else:
                    want_to_play=False
                    play_again_input_check=False
                    "ends game"
            else:
                print("invalid input please enter either y or n")
                play_again_input_check=True
                "invalid input"
    print("hope you had a fun time playing")
play_hangman()