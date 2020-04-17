class mytime:
#create the mytime object initializaed by hour, minute and second
    def __init__(self,hour=0,minute=0,second=0) -> int:
        #this method aims to care about the correct allocation of the seconds in mytime class
        totalseconds = hour * 3600 + minute * 60 + second
        self.hour = totalseconds // 3600
        left = totalseconds % 3600
        self.minute = left // 60
        self.second = left % 60

    #the class properties converted to string
    def __str__(self):
        return '({}, {}, {})'.format(self.hour,self.minute,self.second)

    #this method is for increaing the time adding seconds
    def add_seconds(self,seconds):
        self.second += seconds
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    #this method converts all mehtos
    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    #this method is for comparing if one object is creater than the current object
    def after(self,obj2):
        return self.to_seconds() > obj2.to_seconds()

    #this is called operator overloading in python
    def __add__(self,other):
        return mytime(0,0,self.to_seconds() + other.to_seconds())
    
    #this is overloading the substraction operator
    def __sub__(self,other):
        return mytime(0,0,abs(self.to_seconds() - other.to_seconds()))