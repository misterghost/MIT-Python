#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:59:43 2016

@author: ArqSantos
"""

def fib_recur(n):
    """
    We will recreate fibonacci recursively and find its 
    algorithmic complexity, as it is O(2^n).
    """
    """
    Assumes n is an integer equal or greater than zero.
    """   
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)
        