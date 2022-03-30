from os import path
from pydub import AudioSegment

# files                                                                         
src = "eat.aac"
dst = "eat.wav"

#convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")