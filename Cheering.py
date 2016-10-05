# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:44:09 2016

@author: ArqSantos
"""

an_letters = "aefhilmnrosxAEFHILMNROSX"
word = input("I will cheer for you! Enter your name: ")
times = int(input("What is your enthusiasm level from 1 to 10?"))
i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "  !!  " + char)
    else:
        print("Give me a " + char + "  !!  " + char)
    i += 1
print("What does that spell ???")
for i in range(times):
    print(word + "!!!")
