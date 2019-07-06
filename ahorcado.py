# -*- coding: utf-8 -*-
import random
import os


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


#Shows a welcome messege when starting the program.
def welcome():
    print('B I E N V E N I D O S  A  A H O R C A D O S')


#Pick a random word from storaged.
def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


#Pints on prompt the display board.
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


#This function clears the prompt.
def clearPrompt():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


#Main function. Drives the game logic.
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        clearPrompt()
        welcome()
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        #
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        #
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era %s' % (word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        #Error manager.
        try:
        
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades, ganaste!. La palabra es: %s' % (word))
            break




if __name__ == '__main__':
    """Main game function."""
    run()