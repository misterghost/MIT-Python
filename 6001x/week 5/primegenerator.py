#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:53:46 2016

@author: ArqSantos
"""

def genPrimes():
    """Should generate the sequence of prime numbers on
    successive calls to its next() method, as in : 2,3,5,7,11...
    """
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
            else:
                primes.append(last)
                yield last