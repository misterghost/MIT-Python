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


#def isvalidword(word, hand, wordList):
#    handCounter = hand.copy()
#    for letter in word:
#        if handCounter.get(letter,0) > 0:
#            handCounter[letter] -= 1
#        else:
#            return False
#    if word not in wordList:
#        return False
#    return True



#def calculateHandlen(hand):
#    """ 
#    Returns the length (number of letters) in the current hand.
#    
#    hand: dictionary (string-> int)
#    returns: integer
#    """
#
#    return sum(hand.values())
    





#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------



# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    if len(word) > 0:
        for char in word:
            score += (SCRABBLE_LETTER_VALUES.get(char)) * len(word)
    if len(word) == n:
        score = score + 50
    return(score)


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand2 = hand.copy()
    for letter in word:
        hand2[letter] = hand2.get(letter, 0) - 1
    return(hand2)



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCounter = hand.copy()
    for letter in word:
        if handCounter.get(letter,0) > 0:
            handCounter[letter] -= 1
        else:
            return False
        if word not in wordList:
            return False
    return True

# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    x = hand.values()
    return sum(x)


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0
    newhand = hand.copy()
    while calculateHandlen(newhand) >= 0:
        if calculateHandlen(newhand) == 0:
            print('Run out of letters. Total score:', score, 'points')
            break
        print('Current Hand: ', end ='') 
        displayHand(newhand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if word == ".":
            print("Goodbye! Total score: ",score,"points")  
            break
        elif isValidWord(word, newhand, wordList) == False:
            print('Invalid Word, please try again.')
            print('')
        else:
            score = score + getWordScore(word, n)
            print('"',word,'"', 'earned', getWordScore(word, n), 'points.', 'Total:', score, 'points.')
            newhand = updateHand(newhand, word)


#2222222222222222222222222222222222222222222222222222222222222222222222222222
#3333333333333333333333333333333333333333333333333333333333333333333333333333
#4444444444444444444444444444444444444444444444444444444444444444444444444444

    
 


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    user_selection = None
    while True:
        user_selection = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user_selection == 'n':
            player_hand = dealHand(HAND_SIZE)
            playHand(player_hand.copy(), wordList, HAND_SIZE)
            print()
        elif user_selection == 'r':
            try:
                playHand(player_hand.copy(), wordList, HAND_SIZE)
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        elif user_selection == 'e':
            break
        else:    
            print('Invalid command.')
        


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)








#================================================
#================================================

#from B


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = None
    while True:
        user_selection = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user_selection == 'e':
            break
        else:
            if user_selection == 'n':
                hand = dealHand(HAND_SIZE)
                while True:
                    user_selection_2 = input('Enter u to have yourself play, c to have the computer play: ')
                    if user_selection_2 == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        print('')
                        break
                    elif user_selection_2 == 'c':                
                        compPlayHand(hand, wordList, HAND_SIZE)
                        print('')
                        break
                    else: 
                        print('Invalid command.')
                        #user_selection_2 = input('Enter u to have yourself play, c to have the computer play: ')
                
            elif user_selection == 'r':         
                if hand == None:
                    print('You have not played a hand yet. Please play a new hand first!')
                else:
                    user_selection_2 = input('Enter u to have yourself play, c to have the computer play: ')
                    if user_selection_2 == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        print('')
                    elif user_selection_2 == 'c':                
                        compPlayHand(hand, wordList, HAND_SIZE)
                        print('')
                    else: 
                        print('Invalid command.')
                        
            else: 
                print('Invalid command.')  
                print('')            





























































        





























