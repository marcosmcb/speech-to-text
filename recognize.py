import speech_recognition as sr
from subprocess import check_output
import os
from threading import Thread


from_audio = 'msg0019.wav'
to_wav     = from_audio.split('.')[0] + '-converted.wav'

check_output( 'ffmpeg -i ' + from_audio + ' ' + to_wav, shell=False )


r = sr.Recognizer()
with sr.AudioFile( to_wav ) as source:
    audio = r.record(source)


command = r.recognize_google(audio)
print ('\n\n\n\n\n\n\n\n\n\n\n\n')
print ('************************')
print (command)
print ('************************')