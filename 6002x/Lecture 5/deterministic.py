#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:55:55 2016

@author: ArqSantos
"""

#import random 
#
#def deterministicNumber():
#    """
#    Generates an EVEN, RANDOM number between 9 and 21. DETERMINISTICALLY.
#    """
#    list = [10,12,14,16,18,20]
#
#    return random.choice(list)
#    
#    
    
    
import random

UPPER = 21


def deterministicNumber():
    random.seed(0)  # use a constant seed

    for i in range(10):
        return random.randint(9, UPPER) 