import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

voice = engine.getProperty('voice')
engine.setProperty('voice', 'TTS_MS_EN_US_ZIRA11.0')

engine.say("This was easy")
engine.say("Now what?")

engine.runAndWait()