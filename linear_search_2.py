#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:29:19 2016

@author: ArqSantos
"""

def search(L, e):
    """
    This is an example of linear search of a SORTED list.
    Overall complexity is the same as previous example:
    O(len(L)) for the loop * O(1) to test if e == L[i]
    Overall complexity is: O(n)     where: n is len(L)
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
    
    