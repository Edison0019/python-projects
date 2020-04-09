#print all values starting from n
#terminates when n reaches 1
def seq3n1(n):
    while n != 1:
        print(n,end=', ')
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print(n,end='.\n')

seq3n1(19)