from os import system
import urllib2 as ul

#Asking the user to enter the playlist link from stdin
link = raw_input("Enter the playlist link : ")

#Open the given url
response = ul.urlopen(link)

#Try to read the response got from the url
webContent = response.read()

#Create a file web_page to store the contents of the webpage fetched
fp = open("web_page","a+")

#Writing the contents of the fetched webpage to the file
fp.write(webContent)

#Reseting the file pointer to initial position
fp.seek(0,0)

#This string is searched in the fetch web page content.
#After this content we can get the unique id for every video in playlist.
string = 'data-video-id="'

#This file stores the links of the videos fetched from the web page.
fp2 = open("Videos_List","w")

#Reading every line of the fetched webpage.
for x in fp:
    #This string is searched in every line.
    if 'yt-uix-scroller-scroll-unit  vve-check' in x :

        #Starting postion of the video id in the fetched line.
        pos = x.index(string)+len(string)

        #string storing the link to the video
        s = ""

        #The video id is written within the double quotes in the fetched webpage.
        #Hence searching for the second qoute as we have already skipped the first one.
        while x[pos]!='"':

            #concatenating the each character to the string
            s=s+x[pos]
            pos+=1
        #Writing the link to the file
        fp2.write("https://www.youtube.com/watch?v="+s+"\n")

#Deleting the fetched content from the file.
system("rm -rf web_page")

#Starting youtube-dl to download all the videos listed in the file.
system("youtube-dl -a Videos_List")
