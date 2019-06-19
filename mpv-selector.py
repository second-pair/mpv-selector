#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.

#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestaudio/best"
#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestvideo[height<=?1080][ext=?webm]+bestaudio/best" --cache=1048576

from subprocess import Popen
from os import environ
environ["HOME"] = "/Users/Blair"

mpvPath = "/Program Files/MPV/"
commonCmds = "--netrc --all-subs --embed-subs "
dlCmds = 'youtube-dl.exe -o "C:/Users/Blair/Videos/%(title)s.%(ext)s" --format="'
noDlCmds = 'mpv.exe --ytdl-format="'

watchOrDl = input ("(w)atch or (d)ownload?  ")
print ("Good qualities include:  a; audio; 720; 1080; 1440; 2160.")
userQuality = input ("Which quality would you like?  ")
theUrl = input ("Plese drop your URL here:  ")

if userQuality == "audio" or userQuality == "a":
	theQuality = 'bestaudio/best" '
elif userQuality == "":
	theQuality = 'best" --cache=1048576 '
else:
	theQuality = "bestvideo[height<=?" + userQuality + '][ext=?webm]+bestaudio/best" --cache=1048576 '

if watchOrDl == "w":
	specCmds = noDlCmds
	
elif watchOrDl == "d":
	specCmds = dlCmds

else:
	print ("Error")
	exit (0)

print ("Sure thing, boss.")
theWholeCmd = mpvPath + specCmds + theQuality + commonCmds + theUrl
print (theWholeCmd)
Popen (theWholeCmd)
