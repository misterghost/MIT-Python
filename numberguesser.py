# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:07:59 2016

@author: ArqSantos
"""

#start = 0
#end = 100
#guess = int(start+end)//2
#print("Please think of a number between 0 and 100!")
#while True:
#    print("Is your secret number " + str(guess) + "?")
#    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " )
#    if user == "l":
#        start = guess
#        guess = (guess+end)//2
#    elif user == "h":
#        end = guess
#        guess = (start+guess)//2
#    elif user == "c":
#        print("Game Over, Your secret number was: " + str(guess),)
#        break
#    elif user != "h" or user != "l" or user != "c":
#        user = input("Sorry, I did not understand your input. ")
#    print("Is your secret number " + str(guess) + "?")
#    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " )

start = 0
end = 100
guessed = False
print("Please think of a number between 0 and 100!")
while not guessed:
    guess = (start + end) // 2
    print("Is your secret number " + str(guess) + " ?")
    user_says = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_says == "c":
        guessed = True
    elif user_says == "h":
        end = guess
    elif user_says == "l":
        start = guess
    else: 
        print("Sorry, I did not understand your input")
print("Game Over, your secret number was: " + str(guess))