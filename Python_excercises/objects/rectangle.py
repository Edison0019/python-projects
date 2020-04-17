class rectangle:
    def __init__(self,corner,width,height):
        self.corner = corner
        self.width = width
        self.height = height
    
    #this is the object string defition
    def __str__(self):
        return "({}, {}, {})".format(self.corner,self.width,self.height)
    
    #this method is for changing the rectangle size
    def grow(self,width,height):
        self.width += width
        self.height += height
    
    #this method is for changing the rectangle position
    def change(self,x,y):
        self.corner.x += x
        self.corner.y += y