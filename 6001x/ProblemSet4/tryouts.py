#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:29:39 2016

@author: ArqSantos
"""

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def getWordScore(word, n):
    score = 0
    if len(word) != 0:
        for char in word:
            score += (SCRABBLE_LETTER_VALUES.get(char)) * len(word)
        if len(word) == n:
            score = score+50
    return(score)
