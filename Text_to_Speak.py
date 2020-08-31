
#pip install gTTS

from gtts import gTTS
import os
f = open('Enter text file here...').read()
audio = gTTS(text = f,lang = 'en',slow = False)
audio.save('1.wav')
os.system("1.wav")
