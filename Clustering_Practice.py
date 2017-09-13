import pylab
import random

def minkowskiDist(v1,v2,p):
    dist=0.0
    for i in range(len(v1)):
        dist += abs(v1[i]-v2[i])**p
    return dist**(1.0/p)


class Example(object):
    def __init__(self,name,features,label=None):
        self.name=name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self,other):
        return minkowskiDist(self.features,other.getFeatures(),2)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':' + str(self.label)

class Cluster(object):
    def __init__(self,examples,exampleType):
        """examples are list of example"""
        self.examples=examples
        self.exampleType=exampleType
        self.centroid=self.computeCentroid()

    def update(self,examples):
        """replace the examples in the cluster by new examples
           return how much the centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        if len(examples)>0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0

    def members(self):
        for e in self.examples:
            yield e

    def size(self):
        return len(self.examples)

    def getCentroid(self):
        return self.centroid

    def computeCentroid(self):
        dim = self.examples[0].dimensionality()
        totVals=pylab.array([0.0]*dim)
        for e in self.examples:
            totVals += e.getFeatures()
        centroid = self.exampleType('centroid',totVals/float(len(self.examples)))
        return centroid

    def variance(self):
        totDist = 0.0
        for e in self.examples:
            totDist +=(e.distance(self.centroid))**2
        return totDist**5

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid' + str(self.centroid.getFeatures()) +\
                 ' Contains:\n '
        for e in names:
            result += e + ', '
        return result[:-2]

def kmean(examples,exampleType,k,verbose):
    """Assume examples is a list of examples of type exampleType,
       k is a positive int, verbose is a Boolean
       returns a list containing k custers. If verbose is True it
       prints result of each iteration of k-mneans"""
    initialCentroids = random.sample(examples,k)
    clusters = [] #create a singleton cluster for each centroid
    for e in initialCentroids:
        clusters.append(Cluster([e],exampleType))

    coverged = False
    numIterations = 0
    while not coverged:
        numIterations +=1
        newClusters = []
        for i in range(k):
            newClusters.append([])

        for e in examples: #associate each example with closest centroid
            smallestDistance = e.distance(clusters[0].getCentroid())
            index=0
            for i in range (1,k):
                distance = e.distance (clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance= distance
                    index+=1
            newClusters[index].append(e)

        coverged = True

        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                coverged = False
        if verbose:
            print ('Iteration #'+str(numIterations))
            for c in clusters:
                 print (c)
            print ('')
    return clusters

def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist +=c.variance()
    return totDist

def trykmeans(examples,exampleType,numClusters,numTrials,verbose =False):
    """cal k means numTrials times and returns the result with the lowest
       dissimilarity"""
    best = kmean(examples,exampleType,numClusters,verbose)
    minDissimilarity = dissimilarity(best)
    for trail in range(1,numTrials):
        clusters = kmean (examples, exampleType, numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
    return best

def genDistribution(xMean,xSD,yMean,ySD,n,namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean,xSD)
        y = random.gauss(yMean,ySD)
        samples.append(Example(namePrefix+str(s),[x,y]))
    return samples

def plotSamples(samples,marker):
    xVals,yVals = [],[]
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        pylab.annotate(s.getName(),xy =(x,y),
                       xytext = (x+0.13,y-0.07),
                       fontsize = 'x-large')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals,yVals,marker)

def contrivedTest(numTrials,k,verbose):
    random.seed(0)
    xMean=3
    xSD=1
    yMean=5
    ySD=1
    n=10
    d1Samples = genDistribution(xMean,xSD,yMean,ySD,n,'1.')
    plotSamples(d1Samples, 'b^')
    d2Samples = genDistribution(xMean+3,xSD,yMean+1,ySD,n,'2.')
    plotSamples(d2Samples,'ro')
    clusters = trykmeans(d1Samples +d2Samples,Example,k,numTrials,verbose)
    print('Final result')
    for c in clusters:
        print('',c)
    pylab.show()
    

def contrivedTest2(numTrials,k,verbose):
    random.seed(0)
    xMean=3
    xSD=1
    yMean=5
    ySD=1
    n=8
    d1Samples=genDistribution(xMean,xSD,yMean,ySD,n,'1.')
    plotSamples(d1Samples,'b^')
    d2Samples=genDistribution(xMean+3,xSD,yMean,ySD,n,'2.')
    plotSamples(d2Samples,'ro')
    d3Samples=genDistribution(xMean,xSD,yMean+3,ySD,n,'3.')
    plotSamples(d3Samples,'gd')
    clusters =trykmeans(d1Samples + d2Samples +d3Samples,Example,k,numTrials,verbose)
    print('Final Result')
    for c in clusters:
        print('',c)
    pylab.show()
    
    
def showChart(verbose):
    contrivedTest(1,2,verbose)
    contrivedTest(40,2,verbose)
    contrivedTest2(1,2,verbose)
    contrivedTest2(40,2,verbose)  



    
