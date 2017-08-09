def selSort(L):
    suffixStart=0
    while suffixStart!=len(L):
        for i in range(suffixStart, len(L)):
            print("i=",i,"suffixStart=",suffixStart)
            print("L[i]=",L[i],"L[suffixStart]=",L[suffixStart])
            if L[i]<L[suffixStart]:
                L[suffixStart],L[i] = L[i],L[suffixStart]
            print("New L[i] =",L[i],"New L[suffixStart]=",L[suffixStart])
            print("L=",L)
        print("L=",L)
        suffixStart+=1
        print(suffixStart)


def merge(left, right,compare):
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        print("i=",i, "left=",left,"j=", j, "right",right)
        if compare(left[i],right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while (i<len(left)):
        result.append(left[i])
        i+=1
    while(j<len(right)):
        result.append(right[j])
        j+=1
    print("result=",result)
    return result

import operator

def mergeSort(L,compare=operator.lt):
    if len(L)<2:
        print ("L[:]=",L)
        return L[:]
    else:
        middle =len(L)//2
        print("middle=",middle)
        left=mergeSort(L[:middle],compare)
        right=mergeSort(L[middle:],compare)
        print("left=",left,"right=",right)
        return merge(left,right,compare)

L=[1,5,12,18,19,20,2,3,4,17]
        
    
def lastNameFirstName(name1,name2):
    import string
    name1=str.split(name1,' ')
    name2=str.split(name2,' ')
    print("name1=",name1,"name2=",name2)
    if name1[1]!=name2[1]:
        print("Here!",name1[1]<name2[1])
        return name1[1]<name2[1]
    else:
        return name1[0]<name2[0]

def firsNameLastName(name1,name2):
    import string
    name1=str.split(name1,' ')
    name2=str.split(name2,' ')
    if name1[0]!=name2[0]:
        return name1[0]<name2[0]
    else:
        return name1[1]<name2[1]

L=['Chris Terman','Tom Brady','Eric Grimson','Gisele Bundchen']
newL=mergeSort(L,lastNameFirstName)
print("sorted by last name=",newL)
newL=mergeSort(L,firsNameLastName)
print("sorted by first name=",newL)
