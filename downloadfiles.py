import mechanize
from time import sleep
import requests
#Make a Browser (think of this as chrome or firefox etc)
br = mechanize.Browser()

#visit http://stockrt.github.com/p/emulating-a-browser-in-python-with-mechanize/
#for more ways to set up your br browser object e.g. so it look like mozilla
#and if you need to fill out forms with passwords.

# Open your site
br.open('http://http://archive.wizards.com/default.asp?x=dnd/arch/ls')

f=open("source.html","w")
f.write(br.response().read()) #can be helpful for debugging maybe

filetypes=[".zip"] #you will need to do some kind of pattern matching on your files
myfiles=[]
for l in br.links(): #you can also iterate through br.forms() to print forms on the page!
    for t in filetypes:
        if t in str(l): #check if this link has the file extension we want (you may choose to use reg expressions or something)
            myfiles.append(l)


def downloadlink(l):
    name = l.url.split('/')[-1]
##    f=open(name,"w") #perhaps you should open in a better way & ensure that file doesn't already exist.
##    br.click_link(l)
##    f.write(br.response().read())
    url = r'http://archive.wizards.com/dnd/files/articles/' + name
    r = requests.get(url, stream=True)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    print(name," has been downloaded")
    return name
        
    print(name," has been downloaded")
    #br.back()




for l in myfiles:
    sleep(1) #throttle so you dont hammer the site
    downloadlink(l)
