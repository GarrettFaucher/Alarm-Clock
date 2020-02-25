from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
from datetime import datetime

print(datetime.now())

BEEP = AudioSegment.from_wav("beep.wav")
WHITENOISE = AudioSegment.from_mp3("Testing.mp3")

def playWhite():
    global wakeUp
    while !wakeUp:
        play(WHITENOISE)

def alarm():
    global wakeUp
    wakeUp = True
    t1.kill()
    while(True):
        play(BEEP)
        sleep(200)

global wakeUp = False
t1 = Thread(target=blink_loop)
t1.start()
