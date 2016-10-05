# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:07:45 2016

@author: ArqSantos
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    empty_list = []
    try:
        return item / denom      
    except ZeroDivisionError:
        return empty_list
        
        
        