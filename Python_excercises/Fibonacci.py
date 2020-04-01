# this is to print a fobonacci sequence based on the parameters added
def fibonacci(n):
    s = str(type(n))
    s = 'int' in s
    f = str(type(n))
    f = 'float' in f
    if s == False:
        return print('the paramenter must me an integer not text nor float')
    elif n < 1:
        n = 1
    else:
        l = [0,1]
        i = 0
        o = 0
        while i < n - 1:
            o = (l[-1] + l[-2])
            l.append(o)
            i += 1
        return l

output = fibonacci(10.8)
print('the list of values is',output)
print('the last value is',output[-1])