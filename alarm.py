from pydub import AudioSegment
from pydub.playback import play

beep = AudioSegment.from_wav("beep.wav")
whiteNoise = AudioSegment.from_mp3("Testing.mp3")

wakeUp = False

while (wakeUp == False):
    play(whiteNoise)
    wakeUp = True

while (True):
    play(beep)
