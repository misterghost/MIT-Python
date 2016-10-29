#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:51:51 2016

@author: ArqSantos
"""

def yieldAllCombos(items):
    """
    Generates all possible combinations on F items into 2 bags.
    Item is either in one or zero bags.
    Yields a tuple (bag1, bag2).
    Each bag is a list of items contained in said bag.
    """
    N = len(items)
    #enumerate the 3**N possible combinations
    for i in range (3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
        
                
items = [1,2,3,4,5,6,7,8,9]