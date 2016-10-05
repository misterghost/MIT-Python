# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:28:15 2016

@author: ArqSantos
"""

def fancy(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

#def fancy(numbers, index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError:
#        fancy(numbers, len(numbers) - 1)
#    except ZeroDivisionError:
#        print("-2")
#    else:
#        print("1")
#    finally:
#        print("0")

#def fancy(numbers, index):
#    try:
#        try:
#            denom = numbers[index]
#            for i in range(len(numbers)):
#                numbers[i] /= denom
#        except IndexError:
#            fancy(numbers, len(numbers) - 1)
#        else:
#            print("1")
#        finally:
#            print("0")
#    except ZeroDivisionError:
#        print("-2")

#def fancy(list_of_numbers, index):
#    try:
#        try:
#            raise Exception("0")
#        finally:
#            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#                list_of_numbers[i] /= denom
#    except Exception as ex:
#        print(ex)



#def fancy(list_of_numbers, index):
#    try:
#        try:
#            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#                list_of_numbers[i] /= denom
#        finally:
#            raise Exception("0")
#    except Exception as ex:
#        print(ex)