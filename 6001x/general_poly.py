#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:40:27 2016

@author: ArqSantos
"""

def general_poly (L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """ 
    y = len(L)
    result = 0
    for i in L:
        pre = i * y^i
        result += int(pre)
    return result
        
        