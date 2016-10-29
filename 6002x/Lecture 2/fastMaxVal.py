#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:44:43 2016

@author: ArqSantos
"""

def fastMaxVal(toConsider, avail, memo = {}):
    """
    Assumes toConsider is a list of subjects.
    Avail is a weight memo supplied by recursive calls.
    Returns a tuple of the total value of a solution to the
    knapsack problem and the subjects of said solution.
    """
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        withVal, withToTake =\ fastMaxVal(toConsider[1:], avail-nextItem.getCost(), memo)
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result
    
    
    
    