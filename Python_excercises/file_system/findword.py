def clean(array):
    for i in array:
        if '\n' in i:
            i.replace('\n','')
    return array

def findword(file,value):
    fil = open(file,'r',encoding='ISO-8859-1')
    content = fil.read()
    fil.close()
    content = content.split()
    clean(content)
    x = 0
    for i in content:
        if i == value:
            return print('the value is the word number {0:.2f} within the file'.format(x + 1))
        x +=1
    return print('No word found. {0} words searched within: \n{1}'.format(x + 1,content[:100]))

fil = '../../books/learn python.pdf'
findword(fil,'python')