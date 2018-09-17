import random
class Item():
    def __init__(self,name,val,weight):
        self.name = name
        self.val = val
        self.weight = weight
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.val
    def getName(self):
        return self.name
    def __str__(self):
        return "<"+self.getName()+" , "+str(self.getValue())+" , "+str(self.getWeight())+">"

def buildManyItems(numItems,maxVal,maxWeight):
    Items =[]
    for i in range(numItems):
        Items.append(Item(str(i),random.randrange(1,maxVal),random.randrange(1,maxWeight)*random.random()))
    return Items       



def solve(toConsider,avail):
    global numberCalls
    numberCalls +=1
    if toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getWeight()>avail:
        result = solve(toConsider[1:],avail)
    else:
        nextItem = toConsider[0]
        withVal,withToTake = solve(toConsider[1:],avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal,withoutToTake = solve(toConsider[1:],avail)
        if withVal > withoutVal:
            result = (withVal,withToTake + (nextItem,))
        else:
            result = (withoutVal,withoutToTake)
    return result


##def fastSolve(toConsider, avail,memo=None):
##    if memo == None:
##        memo={}
##    if (len(toConsider),avail) in memo:
##        result = memo[len(toConsider),avail]
##        return result
##    elif toConsider == [] or avail==0:
##        result = (0,())
##    elif toConsider[0].getWeight()>avail:
##        result = fastSolve(toConsider[1:],avail,memo)
##    else:
##        nextItem = toConsider[0]
##        withVal,withToTake = fastSolve(toConsider[1:],avail-nextItem.getWeight(),memo)
##        withVal += nextItem.getValue()
##        withoutVal,withoutToTake = fastSolve(toConsider[1:],avail,memo)
##        if withVal > withoutVal:
##            result = (withVal,withToTake+(nextItem,))
##        else:
##            result = (withoutVal,withoutToTake)
##    memo[(len(toConsider),avail)]=result 
##    return result 

def fastSolve(toConsider, avail, memo = None):
    if memo == None:
        #Initialize for first invocation
        memo = {}
    if (len(toConsider), avail) in memo:
        #Use solution found earlier
        result = memo[(len(toConsider), avail)]
        return result
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Lop off first item in toConsider and solve
        result = fastSolve(toConsider[1:], avail, memo)
    else:
        item = toConsider[0]
        #Consider taking first item
        withVal, withToTake = fastSolve(toConsider[1:],
                                        avail - item.getWeight(),
                                        memo)
        withVal += item.getValue()
        #Consider not taking first item
        withoutVal, withoutToTake = fastSolve(toConsider[1:],
                                              avail, memo)
        #Choose better alternative
        if withVal > withoutVal:
            result = (withVal, withToTake + (item,))
        else:
            result = (withoutVal, withoutToTake)
    #Update memo
    memo[(len(toConsider), avail)] = result
    return result


def smallTest():
    names = ['a','b','c','d']
    vals = [6,7,8,9]
    weights = [3,3,2,5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken = solve(Items,5)
    for item in taken:
        print(item)
    print("Total value of items taken =",val)


import time,sys
sys.setrecursionlimit(20000)
def test(maxVal = 10,maxWeight=10,runSlowly = False):
    random.seed(0)
    global numCalls
    capacity = 8*maxWeight
    print( '#items, #num taken, Value, Solver, #calls, time')
    for numItems in (4,8,16,32,64,128):
        Items = buildManyItems(numItems,maxVal,maxWeight)
        if runSlowly:
            tests = (faseSolve,solve)
        else:
            tests = (fastSolve,)
        for func in tests:
            startTime = time.time()
            val,toTake = func(Items,capacity)
            elapsed = time.time()-startTime
            funcName = func.__name__
            print(numItems, len(toTake), val, funcName, elapsed)


#smallTest()
test()
