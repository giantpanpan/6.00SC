import pylab

#--------------------------- Minkowski Distance -------------------------------#
"""Assume v1 and v2 are equal length arrays of numbers.
   Returns Minkowski distance of order p between v1 and v2"""
def minkowskiDist(v1,v2,p):
    dist=0.0
    for i in range(len(v1)):
        dist += abs(v1[i]-v2[i])**p
    return dist**(1.0/p)

#--------------------------------- Class --------------------------------------#
"""Creating a class of animal
   Features are list of numbers
   Assumes other an animal,
   Returns the Euclidean distance between feature vectors"""
class Animal(object):
    def __init__(self,name,features):
        self.name=name
        self.features=pylab.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self,other):
        return minkowskiDist(self.getFeatures(),other.getFeatures(),2)



#--------------------------------- Compare  --------------------------------------#
"""Assumes animals is a list of animals, precision an int>=0
   Builds a table of Euclidean distance between each animals"""

#get labels for columns and rows
def compareAnimals(animals,precision):
    columnLabels=[]
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels=columnLabels[:]
    tableVals=[]
#get distance between pairs of anumals for each row
    for a1 in animals:
        row=[]
        for a2 in animals:
            if a1==a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #produce table
    table = pylab.table(rowLabels = rowLabels,
                        colLabels = columnLabels,
                        cellText = tableVals,
                        cellLoc = 'center',
                        loc = 'center',
                        colWidths = [0.2]*len(animals))
    table.scale(1,2.5)
    pylab.axis('off') #don't display x and y-axes
    pylab.savefig('distance')

rattlesnake = Animal('rattlesnake',[1,1,1,1,0])
boa = Animal('boa\nconstrictor',[0,1,0,1,0])
dartFrog = Animal('dart frog', [1,0,1,0,4])
alligator=Animal('alligator',[1,1,0,1,4])
animals=[rattlesnake,boa,dartFrog,alligator]
compareAnimals(animals,3)
pylab.show()
