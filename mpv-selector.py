#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.

#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestaudio/best"
#"C:\Program Files\MPV\mpv.exe" --ytdl-format="bestvideo[height<=?1080][ext=?webm]+bestaudio/best" --cache=1048576

from subprocess import Popen

mpvPath = "/Program Files/MPV/"
mpvExe = "mpv.exe"
theCmdPre = ' --ytdl-format="'

print ("Good qualities include:  a; audio; 720; 1080; 1440; 2560.")
theQuality = input ("Which quality would you like?  ")
theUrl = input ("Plese drop your URL here:  ")

if theQuality == "audio" or theQuality == "a":
	theCmd = 'bestaudio/best" '
elif theQuality == "":
	theCmd = 'best" --cache=1048576 '
else:
	theCmd = "bestvideo[height<=?" + theQuality + '][ext=?webm]+bestaudio/best" --cache=1048576 '

print ("Sure thing, boss.")
Popen (mpvPath + mpvExe + theCmdPre + theCmd + theUrl)
