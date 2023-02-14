import pyttsx3
import pyjokes
import wikipedia
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices [1].id)
engine.say(pyjokes.get_joke())
engine.say('oh it\'s boring right')
engine.say('am gonna tell you another joke')
engine.say(' oooh i bet you this one is funny ')
engine.runAndWait()
