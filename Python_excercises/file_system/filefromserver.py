#this is how we can use a python lib for getting files from a remote server using the url
#with the fetched file we can either create a new file, get the data only and also applying some logics to the file

import urllib.request

def geturlfile(url):
    socket = urllib.request.urlopen(url)
    filecontent = str(socket.read())
    socket.close()
    return filecontent

address = "https://d.docs.live.net/ff64906a6daafe8a/Carvision/Data%20sources/Leads%20data/Leads.csv"
output = geturlfile(address)
print(output)

#this code didnt work since the url is no longer available but it is one of the ways we can do this