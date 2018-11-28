#! /usr/bin/python

#  Author:  Blair Edwards 2018

#  Simple script to wrap MPV, to make specifying YT-DLs easier.

from subprocess import Popen

mpvPath = "/Program Files/MPV/"
mpvExe = "mpv.exe"

Popen (mpvPath + mpvExe)
