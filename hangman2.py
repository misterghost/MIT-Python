# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:34:39 2016

@author: ArqSantos
"""
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for a in secretWord:
        if not a in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    z = ('')
    for char in secretWord:
        if char in lettersGuessed:
            z += char
        else:
            z += (' _ ')
    return z
    
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #wordlist = loadWords()
    #secretWord = chooseWord(wordList)
    import string
    availableLetters = string.ascii_lowercase
    guesses = 8
    lettersGuessed = []
    ended = False
    print('Welcome to the game Hangman!','\n','I am thinking of a word that is',len(secretWord),'letters long')
    while not ended :
        print('-----------')
        print('You have', guesses,  'guesses left')
        print('Available Letters:',availableLetters)
        guess = input('Please guess a letter: ')
        guess = guess.lower()

        if guess in availableLetters:
            availableLetters = availableLetters.replace(guess, '')
            lettersGuessed += guess
            if guess in secretWord:
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    ended = True
            else:
                guesses -= 1
                print('Oops! that letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            if guesses < 1:
                ended = True
                
        else:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
    if isWordGuessed(secretWord, lettersGuessed):
        print('-----------')
        print('Congratulations, you won!')
    else: 
        print('-----------')
        print('Sorry, you ran out of guesses.' ,'\n' , 'The secret Word was: ' , secretWord)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    