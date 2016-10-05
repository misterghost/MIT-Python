# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:19:41 2016

@author: ArqSantos
"""
from math import *

def polysum(n,s):
    '''
    n = number of sides of a polygon.
    s = length of each side.
    Should get the Area and square of the perimeter of the polygon, and add those together.
    This sum should be rounded to 4 decimals.
    '''
    
    polygon_area = (0.25 * n  * (s*s)) / (tan(pi/n))
    polygon_perimeter = (n * s)
    polygon_perimeter_squared = (polygon_perimeter * polygon_perimeter)
    return round(polygon_area + polygon_perimeter_squared, 4)