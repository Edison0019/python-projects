#defining an object with a recursive method
class large:
    def __init__(self):
        pass

    def largest(self,v):
        large = 0
        for i in v:
            if type(i) == type([]):
                val = self.largest(i)
            else:
                val = i
            if val > large:
                large = val
        return large

#x = [1,2,3,[8,67],3,4] #this is for testing purposes
#number = large()
#print(number.largest(x)) #this is for testing purposes