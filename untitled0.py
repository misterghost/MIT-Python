# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:45:35 2016

@author: ArqSantos
"""

start = 0
end = 100
guess = (start + end) / 2
print("Please think of a number between 1 and 100")
new_guess = 0
response = input("Is your secret number: " + str(guess) + "?" + " Please tell me H if too high, L it too low, or C if correct: ")
while response == "h" or response == "H":
    new_guess = (start + guess) / 2
    response = input("Is your secret number: " + str(new_guess) + "?" + " Please tell me H if too high, L it too low, or C if correct: ")
while response == "l" or response == "L":
    new_guess = (guess + end) / 2
    response = input("Is your secret number: " + str(new_guess) + "?" + " Please tell me H if too high, L it too low, or C if correct: ")
while response == "c" or response == "C": 
    print("Great !! I've found your secret number!" + str(new_guess) )
else:
    print("I can only accept C, H, or L")
print("please try again from the beginning")
