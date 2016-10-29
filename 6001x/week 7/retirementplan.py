#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:54:00 2016

@author: ArqSantos
"""
import pylab as plt 



def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings
    
    
    
    
    
    
    
    
    
def displayRetireWithMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')
        
        
        
        
        
        
        
def displayRetireWithRates(month, rates, terms):
    plt.figure('retireMonth')
    plt.clf()
    for rate in rates:
       xvals, yvals = retire(month, rate, terms)
       plt.plot(xvals, yvals, label = 'retire:' + str(month) + ':' + str(int(rate*100)))
       plt.legend(loc = 'upper left')
  
       
       
       
       
       
       
def displayRetireWithMonthsAndRates(monthlies, rates, terms):
        plt.figure('retireMonth')
        plt.clf()
        plt.xlim(30*12, 40*12)                  #only for the last 10 years
        for monthly in monthlies:
            for rate in rates:
                xvals, yvals = retire(monthly, rate, terms)
                plt.plot(xvals, yvals, label = 'retire:' + str(monthly) + ':' + str(int(rate*100)))
                plt.legend(loc = 'upper left')
                
                
                
def displayRetireWithMonthsAndRates2(monthlies, rates, terms): #now with ordered visualization
        plt.figure('retireMonth')
        plt.clf()
        plt.xlim(30*12, 40*12)                  #only for the last 10 years
        monthLabels = ['r', 'b', 'g', 'k']
        rateLabels = ['-', 'o', '--']
        for i in range(len(monthlies)):
            monthly = monthlies[i]
            monthLabel = monthLabels[i%len(monthLabels)]
            for j in range(len(rates)):
                rate = rates[j]
                rateLabel = rateLabels[j%len(rateLabels)]
                xvals, yvals = retire(monthly, rate, terms)
                plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire:' + str(monthly) + ':' + str(int(rate*100)))
                plt.legend(loc = 'upper left')  
                
                
        
        
                
                
        # displayRetireWithMonthsAndRates2([500,700,900,1100], [.03, .05, .07], 40*12)
        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                