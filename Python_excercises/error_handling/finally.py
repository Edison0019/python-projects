#the finally statement executes code even though there is an error
#the code is also going to be executed if there is not error in the block of code

def read(file):
    try:
        doc = open(file,'r')
        output = doc.read()
        print(output)
    finally:
        doc.close()
        print('file closed')
    except:
        print('there is an error')

read('test.txt')