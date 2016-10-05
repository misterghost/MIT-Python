# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:11:11 2016

@author: ArqSantos
"""
minimum_fixed_payment = 10
balance = 3329
annual_interest_rate = 0.2
remaining_balance = 0


while True:
    remaining_balance = balance
    for i in range(1, 13):
        remaining_balance = (remaining_balance - minimum_fixed_payment) * (1 + annual_interest_rate / 12.0)
    if remaining_balance > 0:
        minimum_fixed_payment += 10
    else:
        break
print 'Lowest Payment:', minimum_fixed_payment
