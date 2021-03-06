# Add a method reflect_x to Point which returns a new Point, one which 
# is the reflection of the point about the x-axis. 
# For example, Point(3, 5).reflect_x() is (3, -5)

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY
        
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
    def distanceFromPoint(self, point):
        horiz_diff = self.getX() - point.getX()
        vert_diff = self.getY() - point.getY()
        return math.sqrt((horiz_diff ** 2) + (vert_diff ** 2))
    
    def reflect_x(self):
        return Point((self.x * (-1)), self.y)

p = Point(-3, 5)
q = Point(36, 19)
print(p.reflect_x())
