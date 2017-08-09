class intDict(object):
    ##Create an empty dictionary
    def __init__(self,numBuckets):
        self.buckets=[]
        self.numBuckets=numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self,dictKey,dictVal):
        ##Assumes dickKey an int. Adds an entry, if the bucket is empty,
        ##then add the new key and val to this bucket, else, replace the
        ##value in the existing entry
        hashBucket=self.buckets[dictKey%self.numBuckets]
        print("len hashBucket= ",len(hashBucket))
        for i in range(len(hashBucket)):
            if hashBucket[i][0]==dictKey:
                hashBucket[i]==(dictKey,dictVal)
                return
        hashBucket.append((dictKey,dictVal))

    def getValue(self,dictKey):
        ##Assumes dickKey is an int. Returns entry associated
        ##firstly locate which bucket this key within, then
        ##use linear search to search the val with that key
        ##return the val if found, else, return None
        hashBucket=self.buckets[dictKey%self.numBuckets]
        print("hashBucket= ",hashBucket)
        for e in hashBucket:
            print("e= ",e)
            if e[0]==dictKey:
                return e[1]
        return None

    def __str__(self):
        result='{'
        for b in self.buckets:
            for e in b:
                result=result+str(e[0])+':'+str(e[1])+','
        return result[:-1]+'}'


D=intDict(29)
for i in range(20):
    key=random.randint(0,10**5)
    D.addEntry(key,i)
print("The value of the intDict is: ",D)
print("The Buckets are: ")
for hashBucket in D.buckets:
    print(' ',hashBucket)
