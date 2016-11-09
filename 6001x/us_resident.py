#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:14:08 2016

@author: ArqSantos
"""
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        self.name = name
        possibilities = ['citizen', 'legal_resident', 'illegal_resident']
        if status not in str(possibilities):
            raise ValueError ('Status should be one of these strings: citizen, legal_resident, illegal_resident')
        else: 
            self.status = status

        
    def getStatus(self):
        """
        Returns the status
        """
        possibilities = ['citizen', 'legal_resident', 'illegal_resident']
        if self.status not in str(possibilities):
            raise ValueError ('Status should be one of these strings: citizen, legal_resident, illegal_resident')        
        return self.status