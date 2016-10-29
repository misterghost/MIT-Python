#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:34:49 2016

@author: ArqSantos
"""

def selection_Sort_2(L):
    for i in range(len(L) - 1):
        min_Index = i
        min_Value = L[i]
        j = i + 1
        while j < len(L):
            if min_Value > L[j]:
                min_Index = j
                min_Value = L[j]
            j += 1
        if min_Index != i:
            temp = L[i]
            L[i] = L[min_Index]
            L[min_Index] = temp

        
        