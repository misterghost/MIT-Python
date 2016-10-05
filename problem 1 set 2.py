# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:00:41 2016

@author: ArqSantos
"""


balance = 42
annual_interest_rate = 0.2
monthly_payment_rate = 0.04

total = 0 
for i in range(1, 13):
    minimum_monthly_payment = balance * monthly_payment_rate
    balance = (balance - minimum_monthly_payment) * (1 + annual_interest_rate / 12.0)
    total += minimum_monthly_payment    
print("Remaining balance: ", round(balance, 2))