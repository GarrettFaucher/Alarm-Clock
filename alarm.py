from pydub import AudioSegment
from pydub.playback import play
import multiprocessing as mp
from datetime import datetime
import time

global alarm_time
global BEEP
global WHITENOISE
BEEP = AudioSegment.from_wav("beep.wav")
WHITENOISE = AudioSegment.from_mp3("whitenoise.mp3")

def main():
    global alarm_time
    global wakeUp
    global p1

    alarm_time = getInput()
    wakeUp = False
    p1 = mp.Process(target=playWhite) # Process for white noise so it can be killed early
    p1.start()
    wakeUp = True

    waitAlarm()
    alarm()

# Gets alarm time to be set, validates input
def getInput():
    alarm_time = input("Alarm Time (hh:mm): ")
    if(len(alarm_time) != 5):
        alarm_time = getInput()
    elif(alarm_time[2] != ":"):
        alarm_time = getInput()
    return alarm_time

def playWhite():
    global wakeUp
    while (wakeUp == False):
        play(WHITENOISE)

def alarm():
    global wakeUp
    global p1
    wakeUp = True
    p1.terminate()
    time.sleep(2)
    while(True):
        play(BEEP)
        time.sleep(0.3)

def waitAlarm():
    now = datetime.now()
    current = now.strftime("%H:%M")
    while (alarm_time != current):
        time.sleep(5)
        now = datetime.now()
        current = now.strftime("%H:%M")
        print("\"" + current + "\" VS \"" + alarm_time + "\"")

main()
