def readwrite(file,newfile):
    infile = open(file,'r')
    outfile = open(newfile,'w')
    txt = infile.read()
    txt = txt.split('\n')
    x = 0
    while x < len(txt):
        if txt[x] == "":
            del txt[x]
            continue
        x += 1
    for i in txt:
        outfile.writelines(i + '\n')
    infile.close()
    outfile.close()


readwrite('file.txt','newfile.txt')