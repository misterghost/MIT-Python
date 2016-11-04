#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:34:03 2016

@author: ArqSantos
"""

import random

def rollDie():
    """
    returns a random integer between 1 and 6.
    """
    return random.choice([1,2,3,4,5,6])
    
    
def testRoll(n=10):
    """
    Test our stochastic process.
    """
    result = ""
    for i in range(n):
        result = result + str(rollDie())
    print(result)
    