#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:21:41 2016

@author: ArqSantos
"""
import random

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
        
        
class Field(object):
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        

class Drunk(object):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return 'This drunk is named ' + self.name
        
        

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0,0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (1.0, 0,0), (-1.0, 0.0)]
        return random.choice(stepChoices)
        

            
            
        




def walk(f, d, numSteps):
    """Assumes f is a Field, d is a Drunk, and numSteps an int >= 0
    Moves d number of steps times;returns the distance between the 
    final location and the location at the start of the walk"""
    
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
    
    
def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps is an int >= 0, numTrials is an int > 0,
    dClass is a subclass of Drunk.
    Simulates numTrials walks of numSteps steps each.
    Returns a list of the final distances for each trial."""
    
    Homer = UsualDrunk
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        
#        print(walk(f, Homer, 0))
#        print(walk(f, Homer, 1))
#        assert False
        
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances
    
    
    
def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLenghts is a sequence of integers > = 0,
    numTrials is an integer > 0, dClass is a subclass of Drunk.
    For each number of steps in walkLengths, runs simWalks with
    numTrials walks, and prints results."""
    
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of ', numSteps, 'steps')
        print('Mean =', round(sum(distances)/len(distances), 4))
        print('Max =', max(distances), 'Min =', min(distances))
        
        
        
def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, mans, curStyle, label = dClass.__name__)
        pylab.title('Mean Distance from Origin' + str(numTrials) + 'trials')
        pylab.xlabel('Number of steps')
        pylab.ylabel('Distance from origin')
        pylab.legend(loc = 'best')
        
        
    
     #   3drunkTest(walkLengths, numTrials, dClass)     

        
        
        
        
random.seed(0)
#drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
simAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000), 100)




class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
        
        

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of ', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances
    


    
    
    
def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0,0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










        
        
            