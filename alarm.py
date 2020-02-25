from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("beep.wav")
play(song)
