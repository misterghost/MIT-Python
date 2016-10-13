#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:15:54 2016

@author: ArqSantos
"""
import datetime
#we need to import this module or library to use its methods.
class Person(object):
    def __init__(self, name):
        """Create a person called Name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ') [-1]
        #take the full name, that we are expecting to be a string,
        #then split it by the spaces, and return anly the last string.
        
    def setBirthday(self, month, day, year):
        """Sets birthday of person to birthDate"""
        self.birthDate = datetime.date(year, month, day)
        
    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError('No birthday registered for this person')
        return(datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically less than 
        other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
    def __str__(self):
        """returns self's name"""
        return self.name
        
    for e in personList:
        print(e)
        
        
        
        