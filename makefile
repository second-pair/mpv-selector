build: mpv-selector.py
	pyinstaller.exe --onefile --specpath build --distpath bin --icon mpv-icon.ico mpv-selector.py
	
clean:
	rm -rf bin build __pycache__
