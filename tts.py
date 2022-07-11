from gtts import gTTS
import time
import os

text = "hello"
language = "en"
myobj = gTTS(text=text, lang=language, slow=False)

myobj.save("tts.mp3")
os.system("start tts.mp3")