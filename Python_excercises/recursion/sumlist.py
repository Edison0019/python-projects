def suml(value):
    t = 0
    for i in value:
        if type(i) == type([]):
            t += suml(i)
        else:
            t += i
    return t
#x = [1,2,3,[8,67],3,4] #this is for testing purposes
#print(suml(x)) #this is for testing purposes