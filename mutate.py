# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:13:21 2016

@author: ArqSantos
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers.
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer. 
    g takes in an integer, applies a Boolean function, 
        returns either True or False.
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements.
    Returns the largest element in the mutated L or -1 if the list is empty.
    """
    new_List = []
    for item in (L):
        if g(f(item)) == True:
            new_List.append(item)
    L = new_List
    if len(new_List) == 0:
        return -1
    else:
        return max(L)
      
def f(i):
    '''
    f takes in an integer, applies a function, returns another integer 
    '''
    return i + 2
    
    
def g(i):
    '''
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    '''
    return i > 5