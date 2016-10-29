#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:30:20 2016

@author: ArqSantos
"""

def fastFib(n, memo = {}):
    """
    Assumes n is an integer > zero.
    Memo is used only by recursive cals.
    Returns Fibonacci of n
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
        
        
        
        