#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:30:21 2016

@author: ArqSantos
"""
import random 

def genEven():
    """
    Generates an EVEN, RANDOM number between 0 and 100.
    """
    x = random.randrange(0,100,2)
    return(x)
    