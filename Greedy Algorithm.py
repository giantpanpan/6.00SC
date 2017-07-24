#find the maximum value of goods with constraint of weight

class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=float(v)
        self.weight=float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result='<'+self.name+', '\
                +str(self.value)+', '\
                +str(self.weight) +'>'
        return result

def buildItems():
    name=['clock','painting','radio','vase','book','computer']
    vals=[175,90,20,59,10,200]
    weights=[10,9,4,2,1,20]
    Items=[]                                                      #Items= 6 * Item
    for i in range(len(vals)):
        Items.append(Item(name[i],vals[i],weights[i]))
    return Items

def greedy(Items,maxWeight,keyFcn):
    assert type(Items)==list and maxWeight>=0
    ItemCopy=sorted(Items,key=keyFcn,reverse=True)
    result=[]                                                     #sort the list depends on value, weight or density
    totalVal=0.0                                                  #reverse=True means the order of list starts from largest to smallest
    totalWeight=0.0
    i=0
    while totalWeight<maxWeight and i <len(Items):
        if (totalWeight+ItemCopy[i].getWeight())<=maxWeight:
            result.append((ItemCopy[i]))
            totalWeight+=ItemCopy[i].getWeight()
            totalVal+=ItemCopy[i].getValue()
        i+=1
    return (result,totalVal)

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print ('  ', item)

def testGreedys(maxWeight=20):
    Items=buildItems()
    print('Items to choose from: ')
    for item in Items:
        print(' ', item)
    print('Use greedy by value to fill a knapsack of size', maxWeight)
    testGreedy(Items,maxWeight,value)
    print('Use greedy by weight to fill a knapsack of size', maxWeight)
    testGreedy(Items,maxWeight,weightInverse)
    print ('Use greedy by density to fill a knapsack of size', maxWeight)
    testGreedy(Items,maxWeight,density)

def dToB(n,numDigits):
    assert type(n)==int and type(numDigits)==int\
           and n>=0 and n<2**numDigits
    bStr=''
    while n>0:
        bStr=str(n%2)+bStr
        n=n//2
    while numDigits-len(bStr)>0:
        bStr='0'+bStr
    return bStr

def genPset(Items):                                               #generate every possible of set of items. 2^6=36 sets in total
    numSubsets=2**len(Items)                                      #Use binary combination from [0 0 0 0 0 0] to [1 1 1 1 1 1]
    templates=[]
    for i in range(numSubsets):
        templates.append(dToB(i,len(Items)))
    print(templates)
    pset=[]
    for t in templates:
        elem=[]
        for j in range(len(t)):
            if t[j]=='1':
                elem.append(Items[j])
        pset.append(elem)
    print(pset)
    return pset

def chooseBest(pset,constrain,getVal,getWeight):
    bestVal=0.0
    bestSet=None
    for Items in pset:
        ItemsVal=0.0
        ItemsWeight=0.0
        for item in Items:
            ItemsVal+=getVal(item)
            ItemsWeight+=getWeight(item)
        if ItemsWeight<=constrain and ItemsVal>bestVal:
            bestVal=ItemsVal
            bestSet=Items
    return (bestSet, bestVal)

def testBest():
    items=buildItems()
    pset=genPset(items)
    taken,val=chooseBest(pset,20,Item.getValue,Item.getWeight)
    print("Total value of item takes " + str(val))
    for item in taken:
        print("  ",item)
