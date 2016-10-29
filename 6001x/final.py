#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:26:57 2016

@author: ArqSantos
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    translation = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
    if int(us_num) == 10:
        print('shi')
    elif int(us_num) < 10:
        x = translation.get(str(us_num))
        print(x)
       
    elif int(us_num) > 10 and int(us_num) < 20:
        for i in str(us_num):
            x = translation.get(i)
        print('shi' + ' ' +  x)
           
    elif int(us_num) > 19:
        x = translation.get(str(us_num)[:1])
        y = translation.get(str(us_num)[1:])
        if y == 'ling':
            print(x + ' ' + 'shi')
        else:
            print(x + ' ' + 'shi' + ' ' +  y)
            
        
            
            
            
            
            

        
        
        
#        
#    elif us_num > 19:
#        for i in str(us_num):
#            x = translation.get(i)
#            print(i, 'shi', i)
        
          
          
          
          
          
          
          
          
          
#    if us_num == 10:
#        print ('shi')
#        
#    elif us_num < 11:
#          for i in str(us_num):
#              x = translation.get(i)
#              print(x)
#    elif 11 < us_num < 20:
#        for i in str(us_num):
#            x = translation.get(i)
#            print (x)
#            
#            
#            
#            
#            
#    if us_num == 0:
#        print('ling')
#    elif us_num == 1:
#        print('yi')
#    elif us_num == 2:
#        print('er')
#    elif us_num == 3:
#        print('san')
#    elif us_num == 4:
#        print('si')
#    elif us_num == 5:
#        print('wu')
#    elif us_num == 6:
#        print('liu')
#    elif us_num == 7:
#        print('qi')
#    elif us_num == 8:
#        print('ba')        
#    elif us_num == 9:
#        print('yiu')
#    elif us_num == 10:
#        print('shi')
#    elif us_num == 11:
#        print('shi yiu')
#    elif us_num == 12:
#        print('shi er')
#    elif us_num == 13:
#        print('shi san')
#    elif us_num == 14:
#        print('shi si')
#    elif us_num == 15:
#        print('shi wu')
#    elif us_num == 16:
#        print('shi liu')       
#    elif us_num == 17:
#        print('shi qi')
#    elif us_num == 18:
#        print('shi ba')
#    elif us_num == 19:
#        print('shi yiu')
#    elif us_num == 20:
#        print('er shi')
#    elif us_num == 21:
#        print('er shi yiu')
#    elif us_num == 22:
#        print('er shi er')       
#    elif us_num == 23:
#        print('er shi san')
#    elif us_num == 24:
#        print('er shi si')       
#    elif us_num == 25:
#        print('er shi wu')
#    elif us_num == 26:
#        print('er shi liu')       
#    elif us_num == 27:
#        print('er shi qi')
#    elif us_num == 28:
#        print('er shi ba')         
#    elif us_num == 29:
#        print('er shi yiu')
#    elif us_num == 30:
#        print('san shi') 
#    elif us_num == 31:
#        print('san shi yiu')         
#        
#        
#        
#        
#        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        