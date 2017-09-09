# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.

    inputFile = open(filename)
    subject_dir={}
    for line in inputFile:
        line.strip()
        key=line.split(',')[0]
        val=int(line.split(',')[1])
        work=int(line.split(',')[2])
        subject_dir[key]=val,work
    return subject_dir


    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames= sorted(subjects.keys(),reverse=True)


    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

#Problem 2: Subject Selection By Greedy Optimization


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[0]>subInfo2[0]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[1]<subInfo2[1]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...
    
    return ((subInfo1[0])/(subInfo1[1]))>((subInfo2[0])/(subInfo2[1]))

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    j=0
    totalVal=0
    totalWork=0
    subNames= sorted(subjects.keys(),reverse=True)
    advisor_dir={}
    index=0

## Another way to implement this algorithm
##    while index != len(subNames):
##        for i in range(index, len(subNames)):
##            if comparator(subjects[subNames[i]],subjects[subNames[index]]):
##                          subNames[index],subNames[i]=subNames[i],subNames[index]
##        index+=1
    
    for name1 in subNames:
        for name2 in subNames:
            if comparator(subjects[name2],subjects[name1]):
                subNames[subNames.index(name2)],subNames[subNames.index(name1)]=subNames[subNames.index(name1)],subNames[subNames.index(name2)]
                
    while totalWork< maxWork and j < len(subNames):
        if (totalWork + (subjects[subNames[j]])[1])<= maxWork:
            advisor_dir.update({subNames[j]:subjects[subNames[j]]})
            totalWork+=(subjects[subNames[j]])[1]
        j+=1
    
    return advisor_dir


# Problem 3: Subject Selection By Brute Force
#

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    subNames= sorted(subjects.keys(),reverse=True)
    n=len(subNames)
    def dToB(n,numDigits):
        bStr=''
        while n>0:
            bStr=str(n%2)+bStr
            n=n//2
        while numDigits-len(bStr)>0:
            bStr='0'+bStr
        return bStr

    numSubsets=2**n
    templates=[]
    for i in range(numSubsets):
        templates.append(dToB(i,n))
    pset=[]
    for t in templates:
        elem=[]
        for j in range(len(t)):
            if t[j]=='1':
                elem.append(subNames[j])
        pset.append(elem)

    bestVal=0.0
    bestSet=None
    bestDir={}
    for sets in pset:
        itemsVal=0.0
        itemsWeight=0.0
        for name in sets:
            itemsVal+=subjects[name][0]
            itemsWeight+=subjects[name][1]
        if itemsWeight<=maxWork and itemsVal>bestVal:
            bestVal=itemsVal
            bestSet=sets
    for name in bestSet:
        bestDir.update({name:subjects[name]})
    return bestDir


test={'6.00': (16, 8),
'1.00': (7, 7),
'6.01': (5, 3),
'15.01': (9, 6)}            


Short_Sub =loadSubjects(SHORT_SUBJECT_FILENAME)
Subject_Sub =loadSubjects(SUBJECT_FILENAME)

print("*****************Test**********************")
print("\n")
printSubjects(test)
print("Greedy Value: ")
Test1=greedyAdvisor(test, 7, cmpValue)
printSubjects(Test1)

print("Greedy Work: ")
Test1=greedyAdvisor(test, 7, cmpWork)
printSubjects(Test1)

print("Greedy Ratio:")
Test2=greedyAdvisor(test, 7, cmpRatio)
printSubjects(Test2)

print("BruteForce:")
Test3=bruteForceAdvisor(test, 7)
printSubjects(Test3)


print("*****************Short Subject**********************")
print("\n")
printSubjects(Short_Sub)
print("Greedy Value: ")
Short1=greedyAdvisor(Short_Sub, 7, cmpValue)
printSubjects(Short1)

print("Greedy Work: ")
Short2=greedyAdvisor(Short_Sub, 7, cmpWork)
printSubjects(Short2)


print("Greedy Ratio:")
Short3=greedyAdvisor(Short_Sub, 7, cmpRatio)
printSubjects(Short3)

print("BruteForce:")
Short4=bruteForceAdvisor(Short_Sub, 7)
printSubjects(Short4)


print("*****************Short Subject**********************")
print("\n")
printSubjects(Subject_Sub)
print("Greedy Value: ")
sub1=greedyAdvisor(Subject_Sub, 7, cmpValue)
printSubjects(Short1)

print("Greedy Work: ")
sub2=greedyAdvisor(Subject_Sub, 7, cmpWork)
printSubjects(Short2)


print("Greedy Ratio:")
sub3=greedyAdvisor(Subject_Sub, 7, cmpRatio)
printSubjects(Short3)

##print("BruteForce:")
##sub4=bruteForceAdvisor(Subject_Sub, 7)
##printSubjects(Short4)

"""
1. What is the algorithmic complexity of greedyAdvisor?

O(n**2)

2. What is the algorithmic complexity of bruteForceAdvisor?

O(n*(2**n))

3. Assuming 1 microsecond (1 microsecond = 1×10^-6 seconds) to compute the value of a
solution in bruteForceAdvisor, how much time in years (365 days per year) would it take
for bruteForceAdvisor to find an optimal solution for the following number of subjects:
1. 8 subjects?

time=8*(2**8)*(1*10**-6)=0.002048 seconds

2. 16 subjects?

time=1.048576 seconds

3. 32 subjects?

time = 0.004358160625063419 years

4. 321 subjects (the number of courses in the problem set)? 

time = 4.348375434618291e+85 years

"""





















