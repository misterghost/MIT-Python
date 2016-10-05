# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:41:15 2016

@author: ArqSantos
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    test_list = ()
    test_list = test_list + aTup[1::2]
    return test_list