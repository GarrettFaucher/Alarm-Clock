# 2020-02-25 13:15:50.537775

from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
from datetime import datetime
import time

global alarm_time
global BEEP
global WHITENOISE

BEEP = AudioSegment.from_wav("beep.wav")
WHITENOISE = AudioSegment.from_mp3("Testing.mp3")

def main():
    global alarm_time
    alarm_time = input("Alarm Time (hh:mm): ")
    global wakeUp
    global t1
    wakeUp = False
    t1 = Thread(target=playWhite)
    t1.start()

    waitAlarm()
    alarm()

def playWhite():
    global wakeUp
    while (wakeUp == False):
        play(WHITENOISE)

def alarm():
    global wakeUp
    wakeUp = True
    # t1.kill() # Need to find way to kill playWhite
    while(True):
        play(BEEP)
        time.sleep(0.3)

def waitAlarm():
    now = datetime.now()
    current = now.strftime("%H:%M")
    while (alarm_time != current):
        now = datetime.now()
        current = now.strftime("%H:%M")
        print("\"" + current + "\" VS \"" + alarm_time + "\"")
        time.sleep(5)

main()
