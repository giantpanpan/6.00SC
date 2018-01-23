import math
import random
import pylab
import ps6_visualize

class Position(object):
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getNewPosition(self,speed,angle):
        oldx,oldy=self.X,self.Y
        deltax=speed*math.sin(math.radians(angle))
        deltay=speed*math.cos(math.radians(angle))
        newx=oldx+deltax
        newy=oldy+deltay
        return Position(newx,newy)
    
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.cleaned_tiles = set()
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        x, y = int(pos.getX()), int(pos.getY())
        self.cleaned_tiles.add((x, y))
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.cleaned_tiles
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        return self.width * self.height
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        return len(self.cleaned_tiles)
    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        rand_x = round(random.uniform(0, self.width), 1)
        rand_y = round(random.uniform(0, self.height), 1)
        return Position(rand_x, rand_y)
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.
        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        return 0 <= pos.getX() <= self.width and 0 <= pos.getY() <= self.height

class BaseRobot():
    def __init__(self,room,speed):
        self.room=room
        self.speed=speed
        self.p=self.room.getRandomPosition()
        self.d=random.randrange(0,360)

    def getRobotPosition(self):
        return self.p
    def getRobotDirection(self):
        return self.d
    def setNewPosition(self,position):
        self.p=position
    def setNewDirection(self,direction):
        self.d=direction

class Robot(BaseRobot):
    def upDatePositionAndClean(self):
        current_p=self.getRobotPosition()
        self.room.cleanTileAtPosition(current_p)
        new_p=current_p.getNewPosition(self.speed,self.setNewDirection(random.randrange(0, 360)))
        while not self.room.isPositionInRoom(new_p):
            self.setNewDirection(random.randrange(0, 360))
            new_p=current_p.getNewPosition(self.speed,self.getRobotDirection())
        self.setNewPosition(new_p)
        return self.getRobotPosition()

def runSimulation(num_robots,speed,width,height,min_coverage,numTrials,robot_type,visualize):
    all_trial_progress=[]
    for i in range(numTrials):
        if visualize:
            anim= ps6_visualize.RobotVisualization(num_robots, width, height)
        room=RectangularRoom(width,height)
        robots=[robot_type(room,speed) for i in range(num_robots)]
        progress_list=[]
        cleaned_percentage=0.0
        while cleaned_percentage<min_coverage:
            for robot in robots:
                robot.upDatePositionAndClean()
                if visualize:
                    anim.update(room,robots)
                cleaned_percentage=float(room.getNumCleanedTiles())/float(room.getNumTiles())
                progress_list.append(cleaned_percentage)
        if visualize:
            anim.done()
        all_trial_progress.append(progress_list)
    print(all_trial_progress)
    return all_trial_progress

runSimulation(2,1.0,2,2,1.0,3,Robot,True)
    











            
