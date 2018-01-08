from os import system
import urllib2 as ul

link = raw_input("Enter the link : ")

response = ul.urlopen(link)
webContent = response.read()

fp = open("web_page","a+")

fp.write(webContent)
fp.seek(0,0)
f=0
string = 'data-video-id="'
fp2 = open("Videos_List","w")

for x in fp:
    if 'yt-uix-scroller-scroll-unit  vve-check' in x :
        pos = x.index(string)+len(string)
        s = ""
        while x[pos]!='"':
            s=s+x[pos]
            pos+=1
        fp2.write("https://www.youtube.com/watch?v="+s+"\n")

system("rm -rf web_page")
system("youtube-dl -a Videos_List")
