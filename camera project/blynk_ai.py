import os
import random
import smtplib
import subprocess
import sys
import time
import colorama
import requests
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import sqlite3
import pyjokes
import wikipedia
import uuid
from cryptography.fernet import Fernet
from pywhatkit.exceptions import InternetException

try:
  import pywhatkit
except InternetException:
  print("[-] NO INTERNET - this program needs an active internet connection and a fast internet")
  print("[-] Terminating...")
  time.sleep(20)
  exit()

init = 20

engine = pyttsx3.init()
engine. setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def create_table():
  try:
    c.execute("CREATE TABLE answer (question text,response text)")
    c.execute("CREATE TABLE unanswer (question text)")
    c.execute("CREATE TABLE profile (myname text, master text)")
    c.execute("CREATE TABLE device (name text, pin text, token text, mode text)")
    c.execute("CREATE TABLE history (date text , period text, shutdown text)")
    c.execute("CREATE TABLE auther (passer text, valid text, count text, confirm text)")
    c.execute("CREATE TABLE fresh (count integer)")
    c.execute("CREATE TABLE used (count integer)")
    c.execute("CREATE TABLE free (count integer)")
    conn.commit()
  except sqlite3.OperationalError:
    pass

def answer_insert(question, response):
  value = (question, response)
  c.execute("INSERT INTO answer VALUES (?,?)", value)
  conn.commit()
def unanswer_insert(question):
  value = str(question)
  c.execute(f"INSERT INTO unanswer VALUES ({value})")
  conn.commit()
def profile_insert(myname, master):
  value = (myname, master)
  c.execute("INSERT INTO profile VALUES (?,?)", value)
  conn.commit()
def device_insert(name, pin, token, mode):
  value = (name, pin, token, mode)
  c.execute("INSERT INTO device VALUES (?,?,?,?)", value)
  conn.commit()
def history_insert(date, period, shutdown):
  value = (date, period, shutdown)
  c.execute("INSERT INTO history VALUES (?,?,?)", value)
  conn.commit()

def fetchs(table):
  c.execute(f"SELECT * FROM {table}")
  conn.commit()
  return c.fetchall()

def find(question):
  query = f"SELECT * FROM answer"
  c.execute(query)
  conn.commit()
  if c.fetchall() == []:
    return 'none'
  else:
    for i in c.fetchall():
      if i[0] == question or i[0] in question or question in i[0]:
        return i[1]
      else:
        return 'none'
  
def finds(question):
  query = f"SELECT * FROM unanswer"
  c.execute(query)
  conn.commit()
  if c.fetchall() == []:
    return 'true'
  else:
    for i in c.fetchall():
      if i[0] == question or i[0] in question or question in i[0]:
        return 'false'
      else:
        return 'true'

def mynamefetch():
  query = f"SELECT * FROM profile where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][0]
  except:
    return 'none'

def masterfetch():
  query = f"SELECT * FROM profile where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][1]
  except:
    return 'none'

def update_myname(myname):
  c.execute(f"UPDATE profile SET myname = '{myname}' WHERE rowid = 1")

def update_master(master):
  c.execute(f"UPDATE profile SET master = '{master}' WHERE rowid = 1")


def speak(text):
  try:
    engine.say(text)
    engine.runAndWait()
  except Exception as e:
    print("[-] This program would work well because of the below error")
    print(e)
    pletter(value = "if you didn't recognise this error please contact the admin.", times = 0.07)

def talk(text):
  try:
    engine.say(text)
    engine.runAndWait()
  except Exception as e:
    print("[-] This program would work well because of the below error")
    print(e)
    pletter(value = "if you didn't recognise this error please contact the admin.", times = 0.07)


def check_status(token):
  try:
    s = requests.session()
    param = {"token": token}
    req = s.get("https://blynk.cloud/external/api/isHardwareConnected", params=param)
    if req == 'true':
      return True
    elif req == 'false':
      return False
    else:
      return 'unknown'
  except requests.HTTPError:
    talk(req["error"])
  except requests.ConnectionError:
    talk("connection error, you need to check your internet connections")
  except Exception as e:
    print(e)
  return 'error'

def day():
  hours = datetime.now().hour
  if hours > 0 and hours < 12:
    return "morning"
  elif hours > 11 and hours < 16:
    return "afternoon"
  elif hours > 15 and hours < 20:
    return "evening"
  else:
    return "night"

def greet(name):
  hours = day()
  if hours == "morning":
    talk(f"good morning {name}")
    print(f"good morning {name}")
  elif hours == "afternoon":
    talk(f"good afternoon {name}")
    print(f"good afternoon {name}")
  elif hours == "evening":
    talk(f"good evening {name}")
    print(f"good evening {name}")
  elif hours == "night":
    talk(f"good night {name}")
    print(f"good night {name}")


def control_sensor(name, token, pin, mode):
  if mode == 'input':
    try:
      session = requests.Session()
      session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
      session.params["token"] = token
      session.params["pin"] = pin
      response = session.get('https://blynk.cloud/external/api/get')
      talk(f"the value of {name} is {response}")
    except requests.HTTPError:
      talk(response["error"])
    except requests.ConnectionError:
      talk("connection error, you need to check your internet connections")
    except Exception as e:
      print(e)
  else:
    try:
      session = requests.Session()
      session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
      params = {}
      params["token"] = token
      params["pin"] = pin
      response = session.get('https://blynk.cloud/external/api/get', params=params)
      if response == 1:
        try:
          params["value"] = 0
          response = session.get('https://blynk.cloud/external/api/update', params=params)
          if response == 1:
            talk(f"successfully turn off {name}")
          else:
            talk("request was unsuccessful due to some unknown issue")
        except requests.HTTPError:
          talk(response["error"])
        except requests.ConnectionError:
          talk("connection error, you need to check your internet connections")
        except Exception as e:
          print(e)
      else:
        try:
          params["value"] = 1
          response = session.get('https://blynk.cloud/external/api/update', params=params)
          if response == 1:
            talk(f"successfully turn on {name}")
          else:
            talk("request was unsuccessful due to some unknown issue")
        except requests.HTTPError:
          talk(response["error"])
        except requests.ConnectionError:
          talk("connection error, you need to check your internet connections")
        except Exception as e:
          print(e)
    except requests.HTTPError:
      talk(response["error"])
    except requests.ConnectionError:
      talk("connection error, you need to check your internet connections")
    except Exception as e:
      print(e)

def inits():
  create_table()
  name = mynamefetch()
  master = masterfetch()
  if name == 'none' and master == 'none':
    talk('sir this is our first time of talk')
    print('sir this is our first time of talk')
    talk('and i need to know more about you sir')
    print('and i need to know more about you sir')
  if master == 'none':
    talk("what should i call you sir")
    master = take_command()
    talk("what will you like to call me sir")
    myname = take_command()
    profile_insert(myname=myname, master=master)
  name = mynamefetch()
  master = masterfetch()
  greet(master)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        talk('Listening')
        r.pause_threshold = 1
        r.energy_threshold = 50
        audio = r.listen(source)
    try:
        print('Recognizing...')
        qry = r.recognize_google(audio, language='en-in')
        qry = qry.lower()
        print(qry)     
    except Exception as e:
        print(e)
        print('please can you Say that again sir\n')
        talk(e)
        talk('please can you Say that again sir')
        return 'None'

    return qry

def banner():
  data = fetchs('device')
  print(data)
  print("""
             ==========================================
               device that have been connected before
             ==========================================
  """)
  if len(data) > 0:
    print("""
====================================================================
      name      ||     pin       ||    token          ||   mode
====================================================================
    """)
    for i in data: 
      print(f"""
====================================================================
      {i[0]}    ||    {i[1]}     ||     {i[2]}        ||   {i[3]}
====================================================================
      """)
  else:
    print("""
               ==========================================
                          NO DEVICE CONNECTED
                ==========================================
  """)
  print("""
                 ==========================================
                 ==========================================
  """)

def create_device():
  name = input('please choose the name of the device you want to connect to sir: ')
  pin = input('please enter the name of device to represent with: ')
  token = input('please enter the auth token of the device you want create: ')
  mode = input('please enter the auth token of the device you want create: ')
  if condition(name) == 'none':
    device_insert(name, pin, token, mode)
  else:
    talk('device with this name already exist sir')
    talk('you need to restart the creation process again sir')
    create_device()
    talk('sorry for your inconvinence')
  return name
  
def condition(name):
  if name == "yembot":
    return 'none'
  query = f"SELECT * FROM device where name = {name}"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][1], c.fetchall()[0][2], c.fetchall()[0][3]
  except:
    return 'none'

def fcreate(req):
  if req == 'yes':  
    nam = create_device()
    talk(f'sir, did you want to connect to {nam}')
    reqs = input(f'sir, did you want to connect to {nam}: ')
    if reqs == 'yes':
      valer = check_status(token)
      if valer == True:
        token, pin, mode = condition(nam)
        control_sensor(token, pin, mode)
      elif valer == False:
        talk('sorry, The device is offline sir')
      elif valer == 'unknown':
        talk('sorry, unable to complete your request due to an unknown error')
      elif valer == 'error':
        pass
      else:
        pass
    else:
      connect()
  else:
    pass

def connect(name):
  if condition(name) == 'none':
    banner()
    talk('let me know the device you want to connect to, sir')
    talk('you will have to fill out some couple of forms sir')
    talk('I hope you will be satisfy with that sir')
    dev = fetch('device')
    if len(dev) > 0:
      v = input('please choose the device you want to connect to: ')
      try:
        token, pin, mode = condition(v)
        if condition(v) == 'none':
          talk('sir, there is no such device available, did you want to create a device')
          req = input('did you want to create a device: ')
          fcreate(req)
        else:
          valer = check_status(token)
          if valer == True:
            token, pin, mode = condition(v)
            control_sensor(token, pin, mode)
          elif valer == False:
            talk('sorry, The device is offline sir')
          elif valer == 'unknown':
            talk('sorry, unable to complete your request due to an unknown error')
          elif valer == 'error':
            pass
          else:
            pass
      except Exception as e:
        print(e)
    else:
      talk('sir, you haven\'t connect any device before')
      talk('sir, let connect our first device')
      req = input('did you want to create your first device: ')
      fcreate(req)
  else:
    token, pin, mode = condition(name)
    control_sensor(name, token, pin, mode)

def improve_mail(question):
  keys = f'unable to answer ==> {question}'
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(user='malwarefinder3@gmail.com', password='3101331013')
  server.sendmail('malwarefinder3@gmail.com', 'malwarefinder3@gmail.com', msg = keys)
  server.quit()

def trying_to_get_answer(answer):
  if finds(answer) == 'false':
    talk('there is an error with my brain')
  else:
    if find(answer) == 'none':
      talk("sir i didn't understand your demand but you will assist me in getting the answer right")
      query = wikipedia.search(answer)
      for i in query:
        print(i)
        talk(f'sir did you mean {i}')
        # response = take_command()
        response = input("yes/no: ")
        if 'yes' in response:
          answer = i
          break
      try:
        ans = wikipedia.summary(answer)
        speak(ans)
        pletter(value=ans, times=0.07)
      except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        ans = pywhatkit.info(answer)
        speak(ans)
        pletter(value=ans, times=0.07)
      talk("did you agree with this response")
      talk("you response will let me understand better")
      response = input("answer yes/no sir: ")
      if response == 'yes':
        answer_insert(question=answer, response=ans)
      else:
        talk("i will google search the result for you sir")
        talk("before that let me give admin feedback to improve my new update")
        unanswer_insert(answer)
        improve_mail(answer)
        pywhatkit.search(answer)
    else:
      speak(find(answer))
      pletter(value = find(answer), times=0.07)

def sheemar_assistant():
    inits()
    vals = fetch('used') + 1
    vari = fetch('free') - 1
    update('free', vari)
    update('used', vals)
    # answer = take_command()
    answer = input("give me command: ")
    if "bye" in answer:
      days = day()
      if days == 'morning':
        talk('bye sir, have a good day')
      elif days == 'afternoon':
        talk('bye sir, it is so cool talking to you')
      elif days == 'evening':
        talk('bye sir, it late already you need to have things done and sleep earlier')
      else:
        talk('bye sir, have a sweet sleep sir')
      history_insert('date', 'period', shutdown='false')
      exit()
    elif "good morning" in answer:
      days = day()
      if days != 'morning':
        talk(f'sorry sir, we are in the {days}')
      talk('sir, have a good day')
    elif "good afternoon" in answer:
      days = day()
      if days != 'afternoon':
        talk(f'sorry sir, we are in the {days}')
      talk('thank you sir')
    elif "good evening" in answer:
      days = day()
      if days != 'evening':
        talk(f'sorry sir, we are in the {days}')
      talk('ok sir, it is so cool talking to you')
    elif "good night" in answer:
      days = day()
      if days != 'night':
        talk(f'sorry sir, we are in the {days}')
      talk('have a great sleep sir')
    elif "your name" in answer:
      name = mynamefetch()
      talk(f'my name is {name} sir')
      print(f'my name is {name} sir')
      talk('and you?')
      ver = input()
      talk(f'that is cool {ver}, your name is cool')
    elif "my name" in answer:
      talk('cool')
    elif "temperature" in answer:
      connect("temperature")
    elif "humidy" in answer:
      connect("humidy")
    elif "read" in answer:
      name = answer.replace('read', '')
      connect(name)
    elif "turn on" in answer:
      connect("led")
    elif "turn off" in answer:
      connect("led")
    elif "sensor" in answer:
      connect("yembot")
    elif "connected" in answer:
      connect("yembot")
    elif "device" in answer:
      connect("yembot")
    elif "connect" in answer:
      connect("yembot")
    elif "trial" in answer:
      val = trial()
      talk(f"you still have {val} trial left")
    elif "help" in answer:
      answer = answer.replace('help', '')
      trying_to_get_answer(answer)
    elif "how are you" in answer:
      talk('i am fine thank you sir and you')
    elif "hello" in answer:
      talk('sir, how can i help you sir')
    elif "hi" in answer:
      talk('sir, how can i help you sir')
    elif "play" in answer:
      answer = answer.replace('play', '')
      pywhatkit.playonyt(answer)
    elif "who is" in answer:
      answer = answer.replace('who is ', '')
      pywhatkit.info(answer)
    elif "joke" in answer:
      talk("did you really want me to tell you a joke: ")
      resp = input("response: ")
      if resp == 'yes':
        print("""
        _______________________________________________
                        category
                  -----------------------
          Choices: 'neutral', 'chuck', 'all', 'twister'
          default = 'neutral'
      ||||||||||||||||||||||||||||||||||||||||||||||||||||||
          ______________________________________________
                        language
                  -----------------------

          Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
          default = 'en'
        """)
        talk("i guess you will have to fill some couple of forms to give you your taste")
        talk("which language did you prefer")
        lans = input("which language did you prefer: default('en')")
        talk("let me know the category you want")
        category = input("which category did you prefer: default('neutral')")
        if category != '' and lans != '':
          for i in pyjokes.get_jokes(category=category, language=lans):
            talk(i)
            print(i)
        elif category != '':
          for i in pyjokes.get_jokes(category=category):
            talk(i)
            print(i)
        elif lans != '':
          for i in pyjokes.get_jokes(language=lans):
            talk(i)
            print(i)
        else:
          for i in pyjokes.get_jokes():
            talk(i)
            print(i) 
    else:
      trying_to_get_answer(answer)
  	
def pletter(value, times=1, ends='\n', seps=''):
    for i in value:
        sys.stdout.write(colorama.Fore.RED +i+seps)
        sys.stdout.flush()
        time.sleep(times)
    sys.stdout.write(ends)
    print(colorama.Fore.RESET)

def banners():
  try:
    os.system("clear")
    danger_print("""
  Blynk Ai for Windows v0.0.1
  (built: may 27 2022 14:12:27)

    """)


    success_print("""
                                Introduction
    """)
    speak("I am your personal assistant that can do multiple tasks like connect to your blynk project and manipulate it. I can answer various questions, tell jokes, play musics and videos, and many fun stuff. I am built to get smarter with time. The more you ask questions, the more I learn.")                                   
    pletter(value = """    
          I am your personal assistant that can do multiple tasks
          like connect to your blynk project and manipulate it. 
          I can answer various questions, tell jokes, play musics 
          and videos, and many fun stuff.
          I am built to get smarter with time. The more you ask
          questions, the more I learn.

   """, times=0.04)
    success_print('Press Enter key to Continue only if you AGREE to the above DISCLAIMER.\n')
    ans = input("[+] input exit to Exit/close or press Enter to continue: ").lower()
    if ans == "exit":
      os.system('clear')
      exit()
    success_print('[✔] ok')
    os.system("clear")
  except KeyboardInterrupt:
    danger_print("terminating...")
    exit()

def send_mail(key, id, confirm):
  try:
    keys = f"""
          auth id                 ==> {id}
          authenication number    ==> {key}
          authentication verified ==> {confirm}
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user='malwarefinder3@gmail.com', password='3101331013')
    server.sendmail('malwarefinder3@gmail.com', 'malwarefinder3@gmail.com', msg = keys)
    server.quit()
    return True
  except KeyboardInterrupt:
    danger_print("terminating...")
    deletet()
    exit()
  except:
    return False

def unique():
  chc = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5)
  schc = ''.join(chc)
  return schc

def special():
  ran = random.randint(111111111, 999999999)
  chc = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5)
  ran = str(ran)
  schc = ''.join(chc)
  return ran + schc

def generate():
  key = Fernet.generate_key()
  key = key.decode()
  key = 'yembot-' + key
  with open("virus.txt", 'w') as thekey:
    thekey.write(key)
  return key

def password(key):
  key = uuid.uuid5(uuid.NAMESPACE_DNS, key)
  key = key.hex
  key = uuid.UUID(key)
  key = key.bytes_le
  return key

def auther_insert(passer, valid, count, confirm):
  value = (passer, valid, count, confirm)
  c.execute("INSERT INTO auther VALUES (?,?,?,?)", value)
  conn.commit()
def fresh_insert(count):
  value = int(count)
  c.execute(f"INSERT INTO fresh VALUES ({value})")
  conn.commit()
def used_insert(count):
  value = int(count)
  c.execute(f"INSERT INTO used VALUES ({value})")
  conn.commit()
def free_insert(count):
  value = int(count)
  c.execute(f"INSERT INTO free VALUES ({value})")
  conn.commit()

def update(table, counts):
  c.execute(f"UPDATE {table} SET count = {int(counts)} WHERE rowid = 1")
  conn.commit()
def updateauth(valid):
  c.execute(f"UPDATE auther SET valid = '{valid}' WHERE rowid = 1")
def fetch(table):
  c.execute(f"SELECT * FROM {table} Where rowid = 1")
  # val = 'none' if c.fetchall() == [] else c.fetchall()[0][0]
  try:
    return c.fetchall()[0][0]
  except:
    return 'none'
def trial():
  fresh = fetch('fresh')
  used = fetch('used')
  free = fetch('free')

  rem = fresh - used
  return rem
def passfetch():
  query = f"SELECT * FROM auther where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][0]
  except:
    return 'none'
def validfetch():
  query = f"SELECT * FROM auther where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][1]
  except:
    return 'none'
def countfetch():
  query = f"SELECT * FROM auther where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][2]
  except:
    return 'none'
def confirmfetch():
  query = f"SELECT * FROM auther where rowid = 1"
  c.execute(query)
  conn.commit()
  try:
    return c.fetchall()[0][3]
  except:
    return 'none'

def success_print(value):
  print(colorama.Fore.GREEN + value)
  print(colorama.Fore.RESET)
def danger_print(value):
  print(colorama.Fore.RED + value)
  print(colorama.Fore.RESET)
def primary_print(value):
  print(colorama.Fore.BLUE + value)
  print(colorama.Fore.RESET)
def progess_print(value):
  print(colorama.Fore.YELLOW + value)
  print(colorama.Fore.RESET)
def deletet():
  query = "DELETE FROM auther WHERE rowid = 1"
  c.execute(query)
  conn.commit()
def validate(key):
  passers = passfetch()
  pascal = password(key)
  if pascal == passers:
    return True
  else:
    return False

def confirm():
  danger_print("[❌] you trial has expired, you have use up your trial")
  print("[+] contact +2347084375332 via whatsapp to purchase your authentication number")
  talk("you trial has expired, you have use up your trial, if you love me, please contact my master via whatsapp to purchase your authentication number")
  talk("because i can't coutinue without it")
  valid = validfetch()
  counters = countfetch()
  passers = passfetch()
  confirm = confirmfetch()
  if passers == 'none':
    keyer = generate()
    key = password(keyer)
    valid = 'false'
    counters = special()
    confirm = unique()
    auther_insert(key, valid, counters, confirm)
    passers = passfetch()
    counters = countfetch()
    valid = validfetch()
    confirm = confirmfetch()
    if send_mail(keyer, counters, confirm):
      pass
    else:
      danger_print("""
        _________________________________________
                  FATAI ERROR              
                ---------------------
        solution:
        1) Check your connection

        if after you fixed your internet, contact +2347084375332
        via whatsapp. Thanks for your understanding.

      """)
      talk("There is no internet for me to connect to the server")
      deletet()
      danger_print("terminating the program...")
      time.sleep(10)
      exit()
  while valid == 'false':
    success_print("[**] your payment id is %s" % (counters))
    print("[**] contact +2347084375332 via whatsapp to purchase your authentication number")
    auth = input("[🔑] Enter the authentication number you purchased: ")
    progess_print('[🔂] confirming crediential...')
    if auth == confirm:
      success_print('[✔] verified: that is your authentication')
      continue
    elif validate(auth):
      success_print('[✔] validated')
      update('fresh', 50)
      update('used', 0)
      update('free', 50)
      updateauth('true')
      success_print('[✔] confirmed')
      talk("thanks for buying me food, i really appreciate it sir")
      valid = validfetch()
    elif auth == '\n' or auth == '' or auth == ' ':
      danger_print('[-] input is mandatory')
      continue
    else:
      print('\n' + auth + ' is invalid\n')
      danger_print('[x] Wrong authentication number')
      talk('oh sorry, that was a Wrong authentication number you provided')
      continue
  if valid == 'true':
    progess_print('[⚙] Redirecting...')
    deletet()
    os.system('clear')
    start()
  else:
    os.system("clear")
    exit()

def contact():
  try:
    val = trial()
    os.system("clear")
    primary_print("""
                      __________________________________________
                                  Blynk AI                 
                      ------------------------------------------
                      + builded by: Adekojo Adeyemi (yembot)
                      + country: nigeria
                      + state: lagos
                      + contact me via whatsapp: +2347084375332
                      _____________________________________________
    """)
    pletter(value = f"""
      this project is not perfect yet so if you find any bug you can contact me via whatsapp only. you still have {str(val)} trial left.   
    """, times=0.07)

    ans = input("Press Enter to contiune or exit to cancel: ")
    if ans == "exit":
      os.system('clear')
      exit()
    talk("you can ask me for your remaining trial")
  except KeyboardInterrupt:
    danger_print("terminating...")
    exit()

def start():
  progess_print('[**] starting...')
  fresh = fetch('fresh')
  valy = fetch('used')
  vary = fetch('free')
  if fresh == 'none':
    fresh_insert(init)
    fresh = int(fetch('fresh'))
  if valy == 'none':
    used_insert(0)
    valy = int(fetch('used'))
  if vary == 'none':
    free_insert(init)
    vary = int(fetch('free'))
  success_print('[**] preparing...')
  history_insert('date', 'period', shutdown='true')
  contact()
  while True:
    try:
      success_print('[**] please wait while i train my self')
      fresh = int(fetch('fresh'))
      valy = int(fetch('used'))
      vary = int(fetch('free'))
      if fresh >= valy and vary >= 0:
        sheemar_assistant()
      else:
        confirm()
    except KeyboardInterrupt:
      danger_print('\n [-] terminating program')
      os.system('clear')
      exit()

try:
  os.system("clear")
  path = os.path.join(os.path.expanduser("~"), 'AppData\\Local\\tasks.db')
  #create database
  primary_print('[**] connecting...')
  conn = sqlite3.connect(path)
  success_print('[**] processing...')
  # hid database
  command = "attrib +s +h " + path
  execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  c = conn.cursor()
  primary_print('[**] checking...')
  create_table()
  success_print('[**] verifying...')

  banners()
  start()
except KeyboardInterrupt:
  danger_print("terminating...")
  time.sleep(5)
  exit()
