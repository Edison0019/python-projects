#this is class of cardinal points
class point:
    def __init__(self,x = 0, y = 0):
        self.x = x #this are properties
        self.y = y #this are properties

    def distance(self): #this is a method
        return ((self.x ** 2) + (self.y ** 2)) ** (1/2)
    
    def midpoint(self,target):
        m1 = (self.x + target.x) / 2
        m2 = (self.y + target.y) / 2
        return point(m1,m2)

    def __str__(self):
        return '({}, {})'.format(self.x,self.y)

    def reflection(self):
        return point(-self.x,-self.y)