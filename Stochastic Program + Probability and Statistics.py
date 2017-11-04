#flip coin
#standard deviation
#Coefficient of variation
#Error bars
#Geometric Distribution  
#p-value (basball game prediction example)
#Hashing and Collisions

import random
import pylab

def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads +=1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    sd=stdDev(fracHeads)
    mean =sum(fracHeads)/len(fracHeads)
    return fracHeads, mean,sd

def flipPlot(minExp,maxExp):
    ratios =[]
    diffs = []
    xAxis = []
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        Heads = 0.0
        for n in range(numFlips):
            if random.random() < 0.5:
                Heads+=1
        Tails=numFlips - Heads
        ratios.append(Heads/Tails)
        diffs.append(abs(Heads-Tails))
    pylab.title("Difference Between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads-#Tails")
    pylab.plot(xAxis,diffs)
    pylab.figure()
    pylab.title("Heads/Tails Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("#Heads/#Tails")
    pylab.plot(xAxis,ratios)
    pylab.figure()
    pylab.show()

#random.seed(0)
#flipPlot(4,20)

def stdDev(X):
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot+=(x-mean)**2
    return (1/len(X)*tot)**0.5

def makePlot(xVals,yVals,title,xLabel,yLabel,style,logX=False,logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals,yVals,style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()

def runTrial(numFlips):
    Heads = 0.0
    for i in range(numFlips):
        if random.random()<0.5:
            Heads+=1
    Tails = numFlips - Heads
    return (Heads, Tails)


def CV(X):
    """Coefficient of variation is the standard deviation divided by the mean,
       which is more informative than Std, when we are comparing data
       with highly variable means. The plot of the CV for heads/tails
       ratios is not much different from the plot of the standard deviation
       because the only difference is the division by mean and since the mean
       is close to 1 so that makes little difference.
       However, for the plot of the coefficient of variation for the abs(heads-tails)
       is totally different. The reason is that the values of abs(heads-tails) are
       independent from number of flips. The std mislead us to believe that CV is
       growing. The std is growing because the number of flips are growing.
       CV is independet because CV = std/mean. Usually under 0.75 is good. 

    """
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')
    

def flipPlot1(minExp,maxExp,numTrials):
    xAxis=[]
    mean_ratios=[]
    mean_diffs=[]
    ratioSD=[]
    diffSD=[]
    ratiosCVs=[]
    diffsCVs=[]
    for i in range(minExp,maxExp+1):
        xAxis.append(2**i)
    for numFlips in xAxis:
        ratios=[]
        diffs=[]
        for r in range(numTrials):
            Heads,Tails = runTrial(numFlips)
            ratios.append(float(Heads)/Tails)
            diffs.append(abs(Heads-Tails))
        mean_ratios.append(sum(ratios)/numTrials)
        mean_diffs.append(sum(diffs)/numTrials)
        ratioSD.append(stdDev(ratios))
        diffSD.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    
        
    numTrialsString="(" + str(numTrials)+" Trials)"
    title = "Mean Heads/Tails Ratios" + numTrialsString
    makePlot(xAxis,mean_ratios,title,"Number of flips","Mean Heads/Tails",'bo', logX=True)
    title = "SD Heads/Tails Ratios" + numTrialsString
    makePlot(xAxis,ratioSD,title,"Number of flips","Standard Deviation",'bo',
             logX=True,logY=True)
    title = "Mean abs(#Heads-#Tails)" + numTrialsString
    makePlot(xAxis,mean_diffs,title,"Number of flips","Mean Heads/Tails",'bo', logX=True,logY=True)
    title = "SD abs(#Heads-#Tails)" + numTrialsString
    makePlot(xAxis,diffSD,title,"Number of flips","Standard Deviation",'bo',
             logX=True,logY=True)
    title = "Coeff. of Var. abs(#Heads - #Tails)" + numTrialsString
    makePlot(xAxis, diffsCVs,title,"Number of Flips","Coeff. of Var.",'bo',logX=True)
    title = "Coeff. of Var. Heads/Tails Ratio" + numTrialsString
    makePlot(xAxis,ratiosCVs,title,"Number of Flips","Coeff. of Var.", 'bo', logX=True,logY=True)

    pylab.show()
                         
vals=[1,100]
for i in range(1,200):
    num1=random.choice(range(1,100))
    num2=random.choice(range(1,100))
    vals.append(num1+num2)
#pylab.hist(vals,bins=10)
#pylab.show()
    
def labelPlot(numFlips,numTrials,mean,sd):
    pylab.title(str(numTrials)+' trials of ' + str(numFlips)+' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Numer of Trials')
    xmin,xmax=pylab.xlim()
    ymin,ymax=pylab.ylim()
    
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads +=1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    sd=stdDev(fracHeads)
    mean =sum(fracHeads)/len(fracHeads)
    return fracHeads, mean,sd

def makePlots(numFlips1,numFlips2,numTrials):
    val1,mean1,sd1=flipSim(numFlips1,numTrials)
    legend = 'Mean= ' + str(round(mean1,4))+'\nSD= '+str(round(sd1,4))
    pylab.hist(val1,bins=10,label=legend)
    xmin,xmax=pylab.xlim()
    ymin,ymax=pylab.xlim()
    labelPlot(numFlips1,numTrials,mean1,sd1)
    pylab.legend(loc= 'best')
    pylab.figure()

    val2,mean2,sd2=flipSim(numFlips2,numTrials)
    legend = 'Mean= ' + str(round(mean2,4))+'\nSD= '+str(round(sd2,4))
    pylab.hist(val2,bins=10,label=legend)
    pylab.xlim(xmin,xmax)
    labelPlot(numFlips2,numTrials,mean2,sd2)
    pylab.legend(loc= 'best')
    pylab.figure()
    
#makePlots(100,1000,100000)        
#pylab.show()
"""A political poll might indicate that a candidate is likely to get
   52% of the vote +-4%(condidence interval= 8%, with a confidence level of
   95%. It means that the pollster believes that 95% if the time the candidate
   will receive between 48%-56% of the vote"""

def showErrorBars(minExp,maxExp,numTrials):

    means,stds=[],[]
    xVals=[]
    for exp in range(minExp,maxExp+1):
        xVals.append(2**exp)
        fracHeads,mean,std=flipSim(2**exp,numTrials)
        means.append(mean)
        stds.append(std)
    pylab.errorbar(xVals,means,yerr=2*pylab.array(stds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' + str(numTrials)+' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of eads & 95% confidence')
    
#showErrorBars(3,10,100)
#pylab.show()

def clear(n,p,steps):
    numRemaining=[n]
    for i in range(steps):
        numRemaining.append(numRemaining[-1]*(1-p))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.semilogy()
    pylab.title('Clearnace of Drug')


#Geometric Distribution  
def successfulStarts(eventProb, numTrials):
    triesBeforeSuccess=[]
    for i in range(numTrials):
        consecFailures=0
        while random.random() >eventProb:
            consecFailures +=1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

##random.seed(0)
##probOfSuccess = 0.5
##numTrials=5000
##distribution=successfulStarts(probOfSuccess,numTrials)
###print(distribution)
##pylab.hist(distribution,bins =14)
##pylab.xlabel('Tries Before Success')
##pylab.ylabel('Number of Occurances Out of '+str(numTrials))
##pylab.title('Probability of Starting Each Try '+str(probOfSuccess))
###pylab.show()

#Benford's Law
"""P(d) = log10(1+1/d), A set of decimal numbers is said to satisfy
   Benford's Law if the probability of the first digit being d is
   consistent with P(d) = log10(1+1/d)"""
#p-value: determine whether or not a result is statistically significant
"""p-value gives us likelihood that the observation is consistent with the
   null hypothesis(no relationship). The smaller the p-value (<0.05), the more
   likely it is that we should reject the null hypothesis."""


def playSeries(numGames,teamProb):
    numWon=0
    for i in range(numGames):
        if random.random()<teamProb:
            numWon+=1
    return (numWon > numGames//2)
"""simSeries indicate that if the better team needs to win, it need to
   be more than three times better than its opponent"""
def simSeries(numSeries):
    prob=0.5
    fracWon=[]
    probs=[]
    for i in range(numSeries):
        while prob <= 1.0:
            seriesWon=0.0
            for i in range(numSeries):
                if playSeries(7,prob):
                    seriesWon+=1
            fracWon.append(seriesWon/numSeries)
            probs.append(prob)
            prob+=0.01 #When the Series length is fixed(7)
                       #compare the chance of win a Series with differnet team
                       #probabilities of winning a game(strength of a team)
    pylab.plot(probs,fracWon,linewidth=5)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability if Winning a series')
    pylab.axhline(0.95) #draw horizontal line at y=0.95
    pylab.ylim(0.5,1.1)
    pylab.title(str(numSeries)+' Seven-Game Series')
    pylab.ylim(0.5,1.1)
    pylab.title(str(numSeries)+' Seven-Game Series')

#simSeries(400)

"""When the length of series is longer than 1000, we have the confidence
   to say that better team had almost certainly won"""
def findSeriesLength(teamProb):
    numSeries = 200
    maxLen = 2500
    step = 10

    def fracWon(teamProb,numSeries,seriesLen):
        won = 0.0
        for series in range(numSeries):
            if playSeries(seriesLen,teamProb):
                won+=1
        return won/numSeries
    winFrac= []
    xVals =[]
    for seriesLen in range(1, maxLen,step):
        xVals.append(seriesLen)
        winFrac.append(fracWon(teamProb,numSeries,seriesLen))
        #When the team probability is fixed
        #compare the chance of winning a Series with different length of Series
        
    pylab.plot(xVals,winFrac,linewidth =5)
    pylab.xlabel ('Length of Series')
    pylab.ylabel('Probability of Winning Series')
    pylab.title(str(round(teamProb,4))+' Probability of Better Team Winning a Game')
    pylab.axhline(0.95)

##YanksProb = 0.636
##PhilsProb = 0.574
##findSeriesLength(0.52)


#Hashing and Collisions

"""Assue the range of the hash function is 1 to n, the number of insertions is
   K. The probability of the first element that have no collision is 1.
   The probability of second insertion that have no collision is (n-1)/n.
   The probability of k insertion is
   p=1*((n-1)/n)*((n-2)/n)*...(((n-(k-1))/n))
   The probability of at least one collision after k insertion is
   1-(1*((n-1)/n)*((n-2)/n)*...(((n-(k-1))/n)))
   """

def collisionProb(n,k):
    probability=1
    for i in range(k):
        probability *= ((n-i)/float(n))
    return 1-probability

def simInsertion(numIndices,numInsertions):
    choices = range(numIndices)
    used=[]
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions=0.0
    for t in range(numTrials):
        collisions += simInsertion(numIndices,numInsertions)
    return collisions/numTrials

print('Actual probability of a collision=', collisionProb(1000,50))
print('Est. probability of a collision=', findProb(1000,50,100000))
print('Actual probability of a collision=', collisionProb(1000,200))
print('Est. probability of a collision=', findProb(1000,200,10000))
