#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:21:49 2016

@author: ArqSantos
"""

def linear_search(L, e):
    """
    We will start searching equality between each member of L and e.
    L is an UNSORTED list.
    We need to go thru all elements in the list L, to deduce if e 
    is present or not inside of it.
    Overall complexity is: O(n)
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
    