import random
import math
import pylab

class Location(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self,other):
        ox=other.x
        oy=other.y
        xDist = self.x - ox
        yDist = self.x - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Field(object):
    """
       maintains a mapping of drunks to locations and allow multiple drunks
       to be added in to a field at random location
    """

    def __init__(self):
        self.drunks = {}  #create a dictionary of drunks

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc #add a drunk and set his value to location object

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist,yDist=drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist,yDist)

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self,name=None):
        self.name=name

    def __str__(self):
        if self!=None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =[(0.0,1.0),(0.0,-2.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

def walk(f,d,numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def walk2(f,d,walkLength):
    start = f.getLoc(d)
    numStep = 0
    while start.distFrom(f.getLoc(d)) < walkLength:
        f.moveDrunk(d)
        numStep +=1
    return numStep
        

def simWalks(numSteps,numTrials,dClass):
    Homer = dClass()
    origin = Location(0.0,0.0)
    distance=[]
    for t in range(numTrials):
        f =Field()
        f.addDrunk(Homer,origin)
        distance.append(walk(f,Homer,numSteps))
    return distance

def simWalks2(walkLength,numTrials,dClass):
    Barny = dClass()
    origin = Location(0.0,0.0)
    numSteps =[]
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Barny,origin)
        numSteps.append(walk2(f,Barny,walkLength))
    return numSteps
        
def drunkTest(walkLengths,numTrials,dClass):
    for numSteps in walkLengths:
        distance = simWalks(numSteps,numTrials,dClass)
        print (dClass.__name__,'random walk of', numSteps,'steps')
        print ('Mean =', sum(distance)/len(distance))
        print('Max =',max(distance),'Min =', min(distance))

"""number of steps needed for specific distances among three kinds of drunk"""
def drunkTest2(walkLengths,numTrials,dClass):
    for walkLength in walkLengths:
        numSteps = simWalks2(walkLength,numTrials,dClass)
        print(dClass.__name__,'random walk of', walkLength,'length')
        print('Mean =', sum(numSteps)/len(numSteps))
        print('Max =', max(numSteps),'Min =',min(numSteps))
        
def simAll(drunkKinds,walkLengths,numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths,numTrials,dClass)

def simAll2(drunkKinds,walkLengths,numTrials):
    for dClass in drunkKinds:
        drunkTest2(walkLengths,numTrials,dClass)


##drunkTest((10,100,1000,10000),100,UsualDrunk)
##drunkTest2((3,9,28,100),100,UsualDrunk)
        
##simAll((UsualDrunk,ColdDrunk,EWDrunk),(100,10000),100)
##simAll2((UsualDrunk,ColdDrunk,EWDrunk),(20,100),100)
##

class styleIterator(object):
    def __init__(self,styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles)-1:
            self.index =0
        else:
            self.index+=1
        return result

def stdDev(x):
    mean = float(sum(x)/len(x))
    tot = 0.0
    for i in x:
        tot +=(i-mean)**2
    return (tot/len(x))**0.5


def simDrunk(numTrials,dClass,walkLengths):
    meanDistance = []
    for numSteps in walkLengths:
        print ('Starting simulation of', numSteps,'steps')
        trials = simWalks(numSteps,numTrials,dClass)
        mean = sum(trials)/float(len(trials))
        meanDistance.append(mean)
    return meanDistance

def simAllGraph(drunkKinds,walkLengths,numTrials):
    styleChoice = styleIterator(('b-','r:','m-'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of',dClass.__name__)
        means = simDrunk(numTrials,dClass,walkLengths)
        pylab.plot(walkLengths,means,curStyle,label = dClass.__name__)
    pylab.title('Mean Distance from Origion (' + str(numTrials)+' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from origin')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

    
##simAllGraph((UsualDrunk,ColdDrunk,EWDrunk),(10,100,1000,10000),100)
    
def getFinalLocs(numSteps,numTrials,dClass):
    locs = []
    d = dClass()
    origin = Location(0,0)
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d,origin)
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds,numSteps,numTrials):
    styleChoice = styleIterator(('b+','r^','mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps,numTrials,dClass)
        xVals,yVals =[],[]
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle)
    pylab.title('Location at End of Walks (' + str(numSteps) + ' steps')
    pylab.xlabel('East/West')
    pylab.ylabel('North/South')
    pylab.show()

def traceWalk(drunkKinds,numSteps):
    styleChoice = styleIterator(('b+','r^','mo'))
    f = Field()
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d,Location(0,0))
        locs =[]
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals =[]
        yVals =[]
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle)
    pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps')
    pylab.xlabel('East/West')
    pylab.ylabel('North/South')
    pylab.show()


plotLocs((UsualDrunk,ColdDrunk,EWDrunk),100,200)
traceWalk((UsualDrunk,ColdDrunk,EWDrunk),200)







