import os
#this function is to extract a list of elements within a specified directory
def path_list(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path,prefix = ""):
    if prefix == "":
        print('Folder listing for',path)
    
    dirlist = path_list(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path,f)
        if os.path.isdir(fullname):
            print(fullname,prefix + "| ")

p = '/mnt/c/Users/ediso/OneDrive/Escritorio/python-projects'
print_files(p)