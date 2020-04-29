import traceback
from time import localtime


try:
    raise Exception('error has occurred')
except:
    date = list(localtime())
    date = date[0:3]
    with open('errorlog.txt','w') as errorfile:
        errorfile.write('Error date ' + str(date))
        errorfile.write('\n\n')
        errorfile.write(traceback.format_exc())
    print('traceback info has been printed')