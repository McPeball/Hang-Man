#!/usr/bin/python
import random
import csv
def draw_hangman():
    hm = f" ________\n |/.    |\n |.     O\n |.    /|\\\n |.     |\n |.    / \\\n |.   |.  |\n |.   d.  b\n |__________ "
    print(hm)

draw_hangman()

def get_word(f):
    with open(f) as file:
        row = csv.reader(file, delimiter=',')
        words = list()
        for word in row:
            #print(word[0])
            word = word[0].rstrip()
            words.append(word)
    i = random.randint(0,len(words)-1)
    letters = list()
    for l in words[i]:
        letters.append(l)
    return(letters)

def create_guess(letters):
    g = list()
    for l in letters:
        g.append("_")
    return(g)

ws = get_word(f="words.txt")
guess = create_guess(ws)

print(guess)
print("mpty string")
