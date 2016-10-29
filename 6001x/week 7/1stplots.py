#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:58:51 2016

@author: ArqSantos
"""
import pylab as plt

samples = []
linear = []
quad = [] 
cube = []
expo = []

for i in range (0, 30):
    samples.append(i)
    linear.append(i)
    quad.append(i**2)
    cube.append(i**3)
    expo.append(1.5**i)
    
    