#!/usr/bin/python


def draw_hangman():
    hm = f" ________\n |/.    |\n |.     O\n |.    /|\\\n |.     |\n |.    / \\\n |.   |.  |\n |.   d.  b\n |__________ "
    print(hm)

draw_hangman()
def get_word(f):
    with open(f) as file:
        data = file.read()
        print(data)
