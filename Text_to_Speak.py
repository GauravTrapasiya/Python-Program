
#pip install gTTS

from gtts import gTTS
import os
f = open('Text.txt').read()
audio = gTTS(text = f,lang = 'en',slow = False)
audio.save('1.wav')
os.system("1.wav")
