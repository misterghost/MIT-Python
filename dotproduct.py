# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:14:30 2016

@author: ArqSantos
"""

def dotProduct(listA, listB):


    listC = []                        
    for i in range(0, len(listA)):
        listC.append(listA[i]*listB[i])
    suma = sum(i for i in listC)
    return suma