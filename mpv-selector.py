#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.
#  This script doesn't have any runtime dependencies that aren't included with Python.  Other than that, I'm not 100% sure.

#  TODO:  Automatically keep MPV up-to-date.  Work out how to include the local MPV in Git.  Switch 'youtube-dl' -> 'yt-dlp'.
#--script-opts=ytdl_hook-ytdl_path=/custom/path/yt-dlp

#  Imports
from subprocess import run
import urllib .request
from os import path
#from os .path import path .expanduser
#from os .path import path .getmtime
import time

#  Variables
homeDir = path .expanduser ("~")
validWatchOrDl = ('w', 'd', 'wh', 'dh')
#  Youtube DL
ytdlFolder = "./"
ytdlFile = "yt-dlp.exe"
ytdlPath = ytdlFolder + ytdlFile
#ytdlDlUrl = "https://youtube-dl.org/downloads/latest/youtube-dl.exe"
#ytdlSigUrl = "https://yt-dl.org/downloads/latest/youtube-dl.sig"
ytdlDlUrl = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
ytdlSigUrl = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-512SUMS"
#  MPV
mpvFolder = "./mpv/"
mpvFile = "mpv.exe"
mpvPath = mpvFolder + mpvFile
#https://sourceforge.net/projects/mpv-player-windows/files/64bit/
#  Video Options
dlLocDefault = homeDir + '/YTDL/%(playlist_title)s'
fileName='/%(playlist_title)s-%(upload_date)s,%(playlist_index)s-%(title)s.%(ext)s"'
dlCmds1 = ytdlPath + ' -i -o "'
dlCmds2 = ' --netrc --format="'
dlCmdsSubs = ' --all-subs --sub-format srt --embed-subs'
noDlCmds = mpvPath + ' --script-opts=ytdl_hook-ytdl_path=' + ytdlPath + ' --ytdl-format="'
pLStartPos = ""
cacheLimit = "100M"

#  Function to retrieve the latest release URL of yt-dlp.
def getYtDlUrl ():
	pass

#  Function to update the local copy of yt-dlp.
def updateYtdl ():
	#  First check if we're out-of-date and try to download a new copy of yt-dlp if needed.
	try:
		dlObj = urllib .request .urlopen (ytdlDlUrl)
		if (dlObj .status == 200):
			dlObjTime = time .gmtime (0)
			dlFileTime = time .gmtime (0)
			dlObjSize = 0
			dlFileSize = 0
			#  Grab the modification time and size of the remote file.
			try:
				dlObjTime = time .strptime (dlObj .headers ['Last-Modified'], "%a, %d %b %Y %H:%M:%S %Z")
				dlObjSize = int (dlObj .headers ['Content-Length'])
			except:
				print ("Had trouble parsing the modification time or size of the remote file.  Time was:")
				print (dlObj .headers ['Last-Modified'])
				print (dlObj .headers ['Content-Length'])
			#  Grab the modification time and size of the local file.
			try:
				dlFileTime = time .gmtime (path .getmtime (ytdlPath))
				dlFileSize = path .getsize (ytdlPath)
			except:
				dlFileTime = time .gmtime (0)
				dlFileSize = 0

			#  Start comparing.
			print ("Local Stats :  date %s  size %d" % (time .strftime ("%Y-%m-%d_%H-%M-%S", dlFileTime), dlFileSize))
			print ("Remote Stats:  date %s  size %d" % (time .strftime ("%Y-%m-%d_%H-%M-%S", dlObjTime), dlObjSize))
			if (dlObjTime > dlFileTime):
				print ("Newer version available, updating local 'yt-dlp.exe' programme...")
			elif (dlFileSize < 1000):
				print ("Local file is very small (< 1000 bytes)!  Grabbing a new version.")
			elif (dlFileSize != dlObjSize):
				print ("Local and remote files are different sizes!  Grabbing the remote one, since it may still be newer (local could have been `touch`ed, for example).")
			else:
				print ("No update needed.  Continuing...")
				return
			#  Perform the update.
			try:
				dlFile = open (ytdlPath, 'wb')
				dlFile .write (dlObj .read ())
				dlFile .close ()
			except:
				print ("ERROR:  Couldn't open %s in 'wb'!  Trying the download from YT anyway..." % ytdlPath)
			print ("'yt-dlp.exe' updated.")
		else:
			print ("ERROR:  Bad response from the URL (%s)!  Trying the download from YT anyway..." % dlObj .status)
	except urllib .error .URLError as exception:
		print ("ERROR:  Issue with the URL (%s)!  Trying the download from YT anyway..." % exception)
	except urllib .error .HTTPError as exception:
		print ("ERROR:  Bad response from the URL (%s)!  Trying the download from YT anyway..." % exception)
	except:
		print ("ERROR:  Bad response from the URL (not sure what)!  Trying the download from YT anyway...")


#  Find out what the user wants.
watchOrDl = ""
while (not watchOrDl in validWatchOrDl):
	watchOrDl = input ("(w)atch or (d)ownload?  Append 'h' to halt after execution.  ")
print ("Good qualities include:  a; audio; 720; 1080; 1440; 2160.")
userQuality = input ("Which quality would you like?  ")
theUrl = ""
while (theUrl == ""):
	theUrl = input ("Plese drop your URL here:  ")

#  If this is a playlist, get extra playlist info from the user.
if (watchOrDl [0] == 'd') and (theUrl .find ("youtube.com") != -1) and (theUrl .find ("list=") != -1):
	pLStartPos = "--playlist-start %s " % input ("Where in the playlist would you like to start?  (1 - default;  0 - just this;  -1 - this onward.)  ")
	if pLStartPos == "--playlist-start 0 ":
		pLStartPos = "--no-playlist "
	elif pLStartPos == "--playlist-start -1 ":
		indexIndex = theUrl .find ("index=")
		nextAmpersandIndex = theUrl .find ("&", indexIndex)
		if (nextAmpersandIndex == -1):
			pLStartPos = "--playlist-start %s " % theUrl [indexIndex + 6:]
		else:
			pLStartPos = "--playlist-start %s " % theUrl [indexIndex + 6:nextAmpersandIndex]
	elif pLStartPos == "--playlist-start  ":
		pLStartPos = "--playlist-start 1 "

#  Handle the required stream format.
#  Bear in mind we can't embedd subtitles into an audio file...
if userQuality == "audio" or userQuality == "a":
	theQuality = 'bestaudio[ext=m4a]/bestaudio/best" '
elif userQuality == "":
	dlCmds2 = dlCmdsSubs + dlCmds2
	theQuality = 'best" --cache --demuxer-max-bytes=' + cacheLimit + ' '
else:
	dlCmds2 = dlCmdsSubs + dlCmds2
	theQuality = "bestvideo[height<=?" + userQuality + '][ext=?webm]+bestaudio/best" --cache --demuxer-max-bytes=' + cacheLimit + ' '

#  User wants to stream it.
if (watchOrDl in ("w", "wh")):
	specCmds = noDlCmds

#  User wants to download it.
elif (watchOrDl in ("d", "dh")):
	dlLoc = input ("Where do you want to save this?  (Leave blank for default.)  ")
	if dlLoc == "":
		dlLoc = dlLocDefault
	specCmds = dlCmds1 + dlLoc + fileName + dlCmds2
	updateYtdl ()

#  The hell did you just say to me??
else:
	print ("ERROR:  watchOrDl invalid - please report this.")
	exit (0)

#  Start thine engines.
print ("Sure thing, boss.")
theWholeCmd = specCmds + theQuality + pLStartPos + theUrl
print (theWholeCmd)
run (theWholeCmd)

#  Finish up.
if (len (watchOrDl) == 2 and watchOrDl [1] == 'h'):
	input ("Donezo!  Press any key to exit.")
else:
	print ("Donezo!")
