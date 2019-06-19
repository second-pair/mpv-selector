#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.

#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestaudio/best"
#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestvideo[height<=?1080][ext=?webm]+bestaudio/best" --cache=1048576

from subprocess import Popen

mpvPath = "/Program Files/MPV/"
mpvExe = "mpv.exe"
ytdlExe = "youtube-dl.exe"
dlLoc = ' -o "C:/Users/Blair/Videos/%(title)s.%(ext)s"'

watchOrDl = input ("(w)atch or (d)ownload?  ")
print ("Good qualities include:  a; audio; 720; 1080; 1440; 2160.")
theQuality = input ("Which quality would you like?  ")
theUrl = input ("Plese drop your URL here:  ")

if theQuality == "audio" or theQuality == "a":
	theCmd = 'bestaudio/best" '
elif theQuality == "":
	theCmd = 'best" --cache=1048576 '
else:
	theCmd = "bestvideo[height<=?" + theQuality + '][ext=?webm]+bestaudio/best" --cache=1048576 '

if watchOrDl == "w":
	theCmdPre = ' --ytdl-format="'
	theWholeCmd = mpvPath + mpvExe + theCmdPre + theCmd + theUrl
	
elif watchOrDl == "d":
	theCmdPre = ' --format="'
	theWholeCmd = mpvPath + ytdlExe + dlLoc + theCmdPre + theCmd + theUrl

else:
	print ("Error")
	exit (0)

print ("Sure thing, boss.")
Popen (theWholeCmd)
