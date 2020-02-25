# 2020-02-25 13:15:50.537775

from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
from datetime import datetime

print(datetime.now())

global BEEP
global WHITENOISE

BEEP = AudioSegment.from_wav("beep.wav")
WHITENOISE = AudioSegment.from_mp3("Testing.mp3")

def playWhite():
    global wakeUp
    while (wakeUp == False):
        play(WHITENOISE)

def alarm():
    global wakeUp
    wakeUp = True
    t1.kill()
    while(True):
        play(BEEP)
        sleep(200)

global wakeUp
wakeUp = False
t1 = Thread(target=playWhite)
t1.start()
