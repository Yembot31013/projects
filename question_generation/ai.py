import speech_recognition as sr
import pyttsx3
import datetime

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("yembot 1 point o")
	speak("I am your Assistant")
	speak(assname)
  
wishMe()
	
with sr.Microphone() as source:
  
  print("Listening...")
  audio = r.listen(source)

try:
  print("Recognizing...")
  query = r.recognize_google(audio)
  print(query)
  speak(query)

except Exception as e:
  print(e)
  print("Unable to Recognize your voice.")
  speak("Unable to Recognize your voice.")
  
