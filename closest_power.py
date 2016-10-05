# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:15:58 2016

@author: ArqSantos
"""

#def closest_power(base, num):
#    exp = 1
#    if num == 1:
#        return 0
#    product = base ** exp
#
#    while product < num:
#        exp += 1
#    return exp
        

#def closest_power(base, num):
#    exp = 0
#    temp_exp = 1
#    while exp < num:
#        if num == 1:
#            return 0
#        elif base ** exp == num:
#            return exp
#        elif base ** exp < num:
#            exp += 1 
#            temp_exp = exp 
#        elif base ** exp > num:
#            return temp_exp
#            
#    return exp

def closest_power(base, num):
    exp = 0
    while base ** exp < num:
        exp +=1
    return exp if base ** exp - num < num - base ** (exp - 1) else exp - 1 
