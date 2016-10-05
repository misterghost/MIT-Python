# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:09:23 2016

@author: ArqSantos
"""
balance = 320000
annualInterestRate = 0.2

start = balance / 12.0
end = balance * ( 1 + annualInterestRate / 12) ** 12  / 12

fixed_monthly_payment = (start + end) / 2.0

while True:
    remaining_balance = balance
    for i in range(1, 13):
        remaining_balance = (remaining_balance - fixed_monthly_payment) * (1 + annualInterestRate / 12.0)
    if remaining_balance > 0:
        start = fixed_monthly_payment
    elif remaining_balance <= 0 and remaining_balance >= -0.01:
        break
    else:
            end = fixed_monthly_payment
            
    fixed_monthly_payment = (start + end) / 2.0

print 'Lowest Payment:', round(fixed_monthly_payment, 2)
            
            
            





























