read = open('test.txt','r')

def readfile():
    while True:
        newline = read.readline()
        if len(newline) == 0:
            break
        print(newline,end='')

readfile()

read.close()