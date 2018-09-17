import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numWins =0.0 
    for trial in range(numTrials):
        for i in range(24):
            a = rollDie()
            b = rollDie()
            if a == 6 and b ==6:
                numWins +=1
                break
    return numWins/numTrials

print(checkPascal(10000))
        
