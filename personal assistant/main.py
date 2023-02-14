import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import wikipedia
import pywhatkit
import wolframalpha
import winstats
import webbrowser
import nlpcloud

listener = sr.Recognizer()
engine = pyttsx3.init()
app_id = "YTY8X5-UKTGJ4QRJ3"
sound = engine.getProperty("voices")
speed = engine.getProperty("rate")
engine.setProperty("rate", 178)
engine.setProperty("voice", sound[1].id)
client = wolframalpha.Client(app_id)
available = True


def system_perform():
  meminfo = winstats.get_mem_info()
  usage = winstats.get_perf_data()
  mem_usage = meminfo.MemoryLoad
  #cpu_usage =
  

def greet():
  date = datetime.datetime.now().hour
  if date > 0 and date < 12:
    say("good morning, sir")
  elif date >= 12 and date <= 16:
    say("good afternoon, sir")
  elif date > 16 and date <= 18:
    say("good evening, sir")
  else:
    say("good night, sir")

def say(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
      print("listening...")
      voice = listener.listen(source)
      print("recognizing...")
      commands = listener.recognize_google(voice)
      commands = commands.lower()
      if "lucy" in commands:
        commands = commands.replace("lucy", "")
        print("lucy: [+] you say: " + commands)
      else:
        print("lucy: [+] you say: " + commands)  
  except:
    pass
  
  try:
    return commands
  except UnboundLocalError:
    pass

def assistant():
  global available
  dmax = 2
  print("lucy: what did you want me to do for you, sir?")
  say("what did you want me to do for you, sir?")
  command = take_command()
  if command is not None:
    if "time" in command:
      date = datetime.datetime.now().strftime("%I:%M %p")
      print("lucy: the current time is " + date)
      say("the current time is " + date)

    elif "yemi" in command:
      print("lucy: I was built by Adekojo Adeyemi, I will not listen to any negative thing about him.")
      say("yeah, yemi is my master, sir, I will not answer any question regardly my master.")

    elif "open" in command:
      webbrowser.open_new_teb("")
      print(".")
      say("yeah, yemi is my master, sir, I will not answer any question regardly my master.")

    elif "play" in command:
      command = command.replace("play", "")
      print("lucy: playing " + command)
      say("playing " + command)
      pywhatkit.playonyt(command)

    elif "joke" in command:
      joke = pyjokes.get_joke()
      print("lucy: " + joke)
      say(joke)

    elif "who is" in command:
      command = command.replace("who is", "")
      answer = wikipedia.summary(command)
      print("lucy: " + answer)
      say(answer)
    
    elif "search for" in command:
      command = command.replace("search for", "")
      print("lucy: searching for " + command)
      say("searching for " + command)
      pywhatkit.search(command)

    elif "are you single" in command:
      print("lucy: sorry, i am in a relationship with wifi")
      say("sorry, i am in a relationship with wifi")
    
    elif "your name" in command:
      print("lucy: My name is lucy. it was created by daddy bolu and peter")
      say("my name is lucy. it was derive by daddy bolu and peter")

    elif "about yourself" in command or "who create" in command or "who invent" in command or "who made" in command or "who build" in command or "who built" in command or "who make" in command or "your master" in command or "your creat" in command or "your invent" in command:
      print("lucy: My name is lucy. I was created by Adeyemi(yembot) and supported by damola on 29 july, 2022 in Community Innovation Hub")
      say("My name is lucy. I was created by Adeyemi(yembot) and supported by damola  on 29 of july 2022 in Community Innovation Hub")

    elif "how old are you" in command:
      print("lucy: I didn't expect you to ask such question sir")
      say("I didn't expect you to ask such question sir")

    elif "nothing lucy" in command:
      print("lucy: Ok sir, I guess I have assisted you enough sir.")
      say("Ok sir I guess I have assisted you enough sir")
      available = False

    elif "i am drunk" in command:
      print("lucy: Please be safe, if you want me to call or text someone, just ask.")
      say("Please be safe, if you want me to call or text someone, just ask.")

    elif "roast me" in command:
      say("Alright, Y'know, you really remind me of a worm!")
      say("Taking any rotten situation life b")

    elif "zero divided by zero" in command:
      print("lucy: imagine that you have 0 cookies and you split them evenly among 0 friends. How many cookies does each person get? See, it doesnt make sense. And cookie Monster is sad that there are no cookies. And your friends are sad because they don,t exist. Oh wow. This escalated quickly.")
      say("imagine that you have 0 cookies and you split them evenly among 0 friends. How many cookies does each person get? See, it doesnt make sense. And cookie Monster is sad that there are no cookies. And your friends are sad because they don,t exist. Oh wow. This escalated quickly.")

    elif "is usb connected" in command:
      drives = winstats.get_drives()
      if len(drives) > dmax:
        print("lucy: usb device is connected")
        say("usb device is connected")
      else:
        print("lucy: no usb device connected")
        say("no usb device connected")

    elif command is not None:
      print("lucy: analysing...")
      say("ok you mean that " + command)
      try:
        res = client.query(command)
        answer = next(res.results).text
        print("lucy: " + answer)
        say(answer)
      except:
        client = nlpcloud.Client("en_core_web_lg", "98d33bcfe7f66b51aa5dfbc5589d5561d1a71512", True)
# Returns a json object.
        client.chatbot("I just broke up with my girlfriend... What's your name by the way?", "This is a discussion between a human and an AI. The human is sad but the AI is empathetic and reassuring. The AI is called Patrick.", [{"input":"Hello friend", "response":"Hi there, how is it going today?"}, {"input":"Well, not that good...", "response":"Oh? What happened?"}])
    

greet()
while available:
  assistant()





