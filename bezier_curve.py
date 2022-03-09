from point import *

class Bezier:
    __k = 0.01
    pts = list()

    def __init__(self):
        pass

    def linear(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.__l = []

        for i in range(100):
            t = self.__k*(i+1)
            x = self.__bezi(self.__x1, self.__x2, t)
            y = self.__bezi(self.__y1, self.__y2, t)

            self.__l.append(Point(x, y))

        
        return self.__l
        

    def fromPoints(self, p1: Point, p2: Point):
        return self.linear(p1.x, p1.y, p2.x, p2.y)
    
    def fromBezier(self, b1, b2):
        self.__m = []
        for i in range(100):
            t = self.__k*(i+1)
            x = self.__bezi(b1[i].x, b2[i].x, t)
            y = self.__bezi(b1[i].y, b2[i].y, t)
            self.__m.append(Point(x, y))
        
        return self.__m


    def __bezi(self, a, b, t):
        return a+(b-a)*t

    # def points(self):
    #     return self.pts
