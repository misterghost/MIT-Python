# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:17:29 2016

@author: ArqSantos
"""

print("Please think of a number between 0 and 100.")
min = 0
max = 100
med = max / 2

b = input("Is your secret number : " + str(med) + "? " + "Please enter 'h' if the guess is too high, 'l' if its too low, and 'c' if it is correct.")

if b == "l" or "L" :
    min = med
    guess = (min + max) / 2
    print(guess)
elif b == "h" or "H":
    max = guess
    guess = (min + max) / 2
    print(guess)
elif b == "c" or "C":
    print("Perfect, your secret number is: ", guess)
else:
    b = input("Is your secret number : " + str(med) + "? " + "Please enter 'h' if the guess is too high, 'l' if its too low, and 'c' if it is correct.")
