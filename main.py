import os
import eel
from Engine.command import *
from Engine.features import *

eel.init("frontend")

# Launch Brave on macOS with the desired URL
os.system('open -a "Brave Browser" "http://localhost:8000/index.html"')

# Start Eel (in non-embedded browser mode)
eel.start("index.html", mode=None,port=8000, host='localhost', block=True)



def start():

    eel.init("www")

    os.system('open -a "Brave Browser" "http://localhost:8000/index.html"') 

    os.system('index.html' , mode =None ,port=8000, host = 'localhost' , block = True)