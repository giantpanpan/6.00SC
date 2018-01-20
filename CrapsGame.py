import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

class CrapsGame:
    def __init__(self):
        self.passWin, self.passLose =(0,0)
        self.dpWin,self.dpLose,self.dpPush =(0,0,0)
        
    def passResult(self):
        return (self.passWin,self.passLose)

    def dpResult(self):
        return (self.dpWin,self.dpLose,self.dpPush)

    def playHand(self):
        throw = rollDie()+rollDie()
        if throw == 7 or throw ==11:
            self.passWin +=1
            self.dpLose +=1
        elif throw == 2 or throw ==3 or throw == 12:
            self.passLose +=1
            if throw ==12:
                self.dpPush +=1
            else:
                self.dpWin +=1
                
        else:
            newThrow = 0
            while newThrow != throw and newThrow !=7:
                newThrow = rollDie()+rollDie()
                if newThrow == throw:
                    self.passWin+=1
                    self.dpLose+=1
                elif newThrow == 7:
                    self.passLose+=1
                    self.dpWin+=1

def crapsSim(handsPerGame,numGames):
    games = []
    for t in range(numGames):
        c= CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)

    pROIPerGame,dpROIPerGame=[],[]
    for g in games:
        wins,losses=g.passResult()
        pROIPerGame.append((wins-losses)/float(handsPerGame))
        wins,losses,pushes = g.dpResult()
        dpROIPerGame.append((wins-losses)/float(handsPerGame))

    meanROI = str(round(100.0*sum(pROIPerGame)/numGames,4)) + '%'
    print('Pass: Mean of ROI =', meanROI)
    meanROI = str(round(100.0*sum(dpROIPerGame)/numGames,4)) + '%'
    print('Don\'tPass: Mean of ROI =', meanROI)
    
crapsSim(10000,10)



    

                
                
