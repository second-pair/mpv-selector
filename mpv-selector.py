#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.

#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestaudio/best"
#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestvideo[height<=?1080][ext=?webm]+bestaudio/best" --cache=1048576

from subprocess import Popen
from os.path import expanduser
homeDir = expanduser ("~")
#from os import environ
#environ["HOME"] = "/Users/Blair"

mpvPath = "/Program Files/MPV/"
commonCmds = "--netrc --all-subs --embed-subs "
dlLocDefault = homeDir + '/YTDL/%(playlist_title)s'
fileName='/%(playlist_title)s-%(upload_date)s,%(playlist_index)s-%(title)s.%(ext)s'
dlCmds1 = 'youtube-dl.exe -o "'
dlCmds2 = '" --format="'
noDlCmds = 'mpv.exe --ytdl-format="'
pLStartPos = ""

watchOrDl = input ("(w)atch or (d)ownload?  ")
print ("Good qualities include:  a; audio; 720; 1080; 1440; 2160.")
userQuality = input ("Which quality would you like?  ")
theUrl = input ("Plese drop your URL here:  ")

if theUrl .find ("list=") != -1:
	#https://www.youtube.com/watch?v=oYSVMj2ItIA&list=PLV2ONwtymjs9rgivAxvpjODCy0ZuF0yFr&index=101&t=0s
	#https://www.youtube.com/playlist?list=PLV2ONwtymjs9rgivAxvpjODCy0ZuF0yFr
	pLStartPos = "--playlist-start %s " % input ("Where in the playlist would you like to start?  (Default is 1, use 0 for just this video.)  ")
	if pLStartPos == "--playlist-start 0 ":
		pLStartPos = "--no-playlist "

if userQuality == "audio" or userQuality == "a":
	theQuality = 'bestaudio/best" '
elif userQuality == "":
	theQuality = 'best" --cache=1048576 '
else:
	theQuality = "bestvideo[height<=?" + userQuality + '][ext=?webm]+bestaudio/best" --cache=1048576 '

if watchOrDl == "w":
	specCmds = noDlCmds

elif watchOrDl == "d":
	dlLoc = input ("Where do you want to save this?  (Leave blank for default.)  ")
	if dlLoc == "":
		dlLoc = dlLocDefault
	specCmds = dlCmds1 + dlLoc + fileName + dlCmds2

else:
	print ("Error")
	exit (0)

print ("Sure thing, boss.")
theWholeCmd = mpvPath + specCmds + theQuality + pLStartPos + commonCmds + theUrl
print (theWholeCmd)
Popen (theWholeCmd)
