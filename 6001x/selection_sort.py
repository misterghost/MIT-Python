#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:02:24 2016

@author: ArqSantos
"""

def selection_sort(L):
    """
    Using selection sorting, we will order a list of elements.
    First find the smallest element, and swap it with element at index zero.
    Then find the smallest element in the remaining list and swap it 
    with element at index 1. Repeat.
    Overall complexity: Quadratic: O(n^2) Because it has a nested loop.
    """
    suffixST = 0                                        #Counter
    while suffixSt != len(L):                           #As long as i dont get to the length of L
        for i in range(suffixSt, len(L)):               #From suffixSt -start point- to the end of list -end point-
            if L[i] < L[suffixSt]:                      #If element smaller than the end of suffixSt 
                L[suffixSt], L[i] = L[i], L[suffixSt]   #Swap
        suffixSt += 1                                   #Increase counter
        