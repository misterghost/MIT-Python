# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:03:35 2016

@author: ArqSantos
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    z = string.ascii_lowercase
    y = ('')
    for char in z:
        if char in lettersGuessed:
            y = y
        else:
            y += char
    return y
    
            
    