from pydub import AudioSegment
from pydub.playback import play
import multiprocessing
from datetime import datetime
import time

global alarm_time
global p

def playWhite():
    white_noise = AudioSegment.from_mp3("whitenoise.mp3")
    play(white_noise)

# Gets alarm time to be set, validates input
def getInput():
    alarm_time = input("Alarm Time (hh:mm): ")
    if(len(alarm_time) != 5):
        alarm_time = getInput()
    elif(alarm_time[2] != ":"):
        alarm_time = getInput()
    return alarm_time

def determineAlarm():
    global p
    p.start()
    waitAlarm()
    p.terminate()
    p.join()
    alarm()

def alarm():
    beep = AudioSegment.from_wav("beep.wav")
    while(True):
        play(beep)
        time.sleep(0.3)

def waitAlarm():
    global alarm_time
    now = datetime.now()
    current = now.strftime("%H:%M")
    while (alarm_time != current):
        time.sleep(5)
        now = datetime.now()
        current = now.strftime("%H:%M")
        print("\"" + current + "\" VS \"" + alarm_time + "\"")


if __name__ == "__main__":
    global alarm_time
    global p
    alarm_time = getInput()
    p = multiprocessing.Process(target = playWhite)
    determineAlarm()
