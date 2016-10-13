#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:38:41 2016

@author: ArqSantos
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        #time = '6:30' why are we assigning a default value that later will be replaced?
        print(time)

