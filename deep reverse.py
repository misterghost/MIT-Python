# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:03:16 2016

@author: ArqSantos
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in L:  
        if type(i)==list:deep_reverse(i)  
    L.reverse()  
