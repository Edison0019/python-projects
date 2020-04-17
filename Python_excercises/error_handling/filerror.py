#this is how to use error handling with the try and except statements
#if there is an error in the try block then the except block code is going to be executed
#THIS IS NOT RECOMMENDED FOR KNOWING IF A FILE EXISTS, BETTER USING os.path.isfile(path) INSTEAD FROM THE OS MODULE
def exists(file):
    try:
        f = open(file,'r')
        f.close()
        return True
    except:
        return False