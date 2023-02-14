import pyttsx3
engine = pyttsx3.init() #object creation

#####RATE#####
rate = engine.getProperty('rate') #getting detail of speaking rate
print(rate)                       #printing current voice rate
engine.setProperty('rate', 125)   #setting up new voice rate

######volume#####
volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
print(volume)                         #printing current volume level
engine.setProperty('volume', 1.0)     #setting up volume level between 0 and 1

######voices#####
voices = engine.getProperty('voices')      #getting detail of current voice
#engine.setProperty('voices', voices[0].id) #changing index, changes voices. 0 for male.
engine.setProperty('voices', voices[1].id) #changing index, changes voices. 1 for female.

engine.say("Hello World!")
engine.say("my current speaking rate is " + str(rate))
engine.runAndWait()
engine.stop()