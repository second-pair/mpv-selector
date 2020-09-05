build:  mpv-selector.py
	PyInstaller.exe --onefile --workpath build --specpath build --distpath bin --icon ../mpv-icon.ico --name mpv-selector.exe mpv-selector.py
	
clean:
	rm -rf bin build __pycache__

all:  clean build
