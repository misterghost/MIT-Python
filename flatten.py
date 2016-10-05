# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:20:05 2016

@author: ArqSantos
"""

#
#def is_list(p):
#    return isinstance(p, list)
#    
#def deep_reverse(p):
#    result = []
#    if is_list(p):
#        for i in range( len(p)-1, -1, -1):   
#            result.append(deep_reverse(p[i]))     
#        return result         
#    else:
#        return p
#def flatten(x):
#    if isinstance(x, collections.Iterable):
#        return [a for i in x for a in flatten(i)]
#    else:
#        return [x]
        
        
#def flatten(L):
#    for item in L:
#        try:
#            yield from flatten(item)
#        except TypeError:
#            yield item
        
#def flatten(xs):
#    res = []
#    def loop(ys):
#        for i in ys:
#            if isinstance(i, list):
#                loop(i)
#            else:
#                res.append(i)
#    loop(xs)
#    return res
        
        
        
        ###si funciona!!!!
        
#def flatten(l): 
#    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
#    
        
#def flatten(l):
#    if isinstance(l,list):
#        return sum(map(flatten,l))
#    else:
#        return l


def flatten(aList):
    if not isinstance(aList,list):
        return aList
    elif len(aList) is 0:
        return []
    elif isinstance(aList[0],list):
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return [aList[0]] + flatten(aList[1:])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        