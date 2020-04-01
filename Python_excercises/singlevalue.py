import timeit

def singlevalue(lit):
    for x in lit:
        if lit.count(x) == 1:
            return x
        
var = [1,1,1,2,2,2,3,3,3,4,5,5,5]

