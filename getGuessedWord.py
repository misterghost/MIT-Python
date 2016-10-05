# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:33:35 2016

@author: ArqSantos
"""

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




