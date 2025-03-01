import os
import eel

eel.init("www")

# Open Microsoft Edge in app mode
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# eel.start() function
eel.start('index.html', mode=None, host='localhost', block=True)
