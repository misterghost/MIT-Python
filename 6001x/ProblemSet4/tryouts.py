#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:29:39 2016

@author: ArqSantos
"""

#SCRABBLE_LETTER_VALUES = {
#    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
#}
#def getWordScore(word, n):
#    score = 0
#    if len(word) != 0:
#        for char in word:
#            score += (SCRABBLE_LETTER_VALUES.get(char)) * len(word)
#        if len(word) == n:
#            score = score+50
#    return(score)

#hand = {'h':1, 'e':1, 'l':2, 'o':1}
#for letter in hand.keys():
#    for j in range(hand[letter]):
#         print(letter,end=" ")       # print all on the same line
#print()  




#n = 7
#VOWELS = 'aeiou'
#CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
#hand={}
#numVowels = n // 3
#
#for i in range(numVowels):
#    x = VOWELS[random.randrange(0,len(VOWELS))]
#    hand[x] = hand.get(x, 0) + 1
#    
#for i in range(numVowels, n):    
#    x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
#    hand[x] = hand.get(x, 0) + 1
#    
#print(hand)


#hand = {'h':1, 'e':1, 'l':2, 'o':1}
#hand2 = hand.copy()
#hand[4] = '0.5'
#print("hand is: ", hand)
#print("hand2 is: ", hand2)

#def updateHand(hand, word):
#    hand2 = hand.copy()
#    for i in word:
#        if i in hand and hand[i] > 0:
#            hand2[i] = hand.get(i, 0) -1
#    return (hand2)            
                
#hand = {'h':1, 'e':1, 'l':2, 'o':0}           
#hand2 = hand.copy()
#word = 'hello'
#for letter in word:
#    hand2[letter] = hand2.get(letter, 0) - 1
#print(hand2)


def isvalidword(word, hand, wordList):
    handCounter = hand.copy()
#    if word in wordList:
#        if len(word) > 0:
#            for letter in word:
#                if handCounter.get(letter,0) > 0:
#                    handCounter[letter] -= 1
#                    return True
#                else:
#                    return False
#                    break
#    else:
#        return False
    for letter in word:
        if handCounter.get(letter,0) > 0:
            handCounter[letter] -= 1
        else:
            return False
    if word not in wordList:
        return False
    return True
        





























