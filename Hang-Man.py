#!/usr/bin/python
import random
import csv

def draw_hangman(idx):
    idx = int(idx)
    #hm = f" ________\n |/     |\n |      O\n |     /|\\\n |      |\n |     / \\\n |    |   |\n |    d   b\n |__________ "
    
    hm = list([
        f" \n\n\n\n\n\n\n\n  __________ ",
        f" \n |       \n |       \n |        \n |       \n |        \n |         \n |         \n |__________ ",
        f" ________\n |       \n |       \n |        \n |       \n |        \n |         \n |         \n |__________ ",
        f" ________\n |/      \n |       \n |        \n |       \n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |       \n |        \n |       \n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |      O\n |        \n |       \n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |      O\n |      | \n |      |\n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |      O\n |     /| \n |      |\n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |      O\n |     /|\\\n |      |\n |        \n |         \n |         \n |__________ ",
        f" ________\n |/     |\n |      O\n |     /|\\\n |      |\n |     /  \n |    |    \n |    d    \n |__________ ",
        f" ________\n |/     |\n |      O\n |     /|\\\n |      |\n |     / \\\n |    |   |\n |    d   b\n |__________ "
        ])
    print(hm[idx])





def get_word(f):
    '''
    Read words from a file (f). Randomly select one return a list
    containing each letter from the word as an element in the list
    '''
    with open(f) as file:
        # misusing ces.reader() here
        row = csv.reader(file, delimiter=',')
        words = list()
        for word in row:
            word = word[0].rstrip()
            words.append(word)
    # use i to pick a word randomly
    i = random.randint(0,len(words)-1)
    # letters will hold each letter in the word as a list
    letters = list()
    for l in words[i]:
        letters.append(l)
    return(letters)

def create_guess_status(letters):
    '''
    Return a list, the same length as the list returned by get_word.
    The list contains underscore characters that can be filled with
    correctly guessed letters
    '''
    g = list()
    for l in letters:
        g.append("_")
    return(g)

def check_guess(word, guess, letter):
    for i in range(0, len(word)):
        if letter == word[i]:
            guess[i] = letter
    return(guess)

def get_guess():
    inp = input("please type a letter:\n")
    inp.rstrip()
    return(inp)
    

# Test hangman drawing
draw_hangman(0)
draw_hangman(1)
draw_hangman(2)
draw_hangman(3)
draw_hangman(4)
draw_hangman(5)
draw_hangman(6)
draw_hangman(7)
draw_hangman(8)
draw_hangman(9)
draw_hangman(10)


word = get_word(f="words.txt")

guessed = create_guess_status(word)

guess = get_guess()

guessed = check_guess(word, guessed, guess)


print("".join(guessed))


