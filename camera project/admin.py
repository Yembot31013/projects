import ctypes, sys
import pprint
import subprocess

def command(cmd):
    execute = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    result = execute.stdout.read() + execute.stderr.read()
    result = result.decode()
    return result

def is_admin():
    try:
      return ctypes.windil.shell32.IsUserAnAdmin()
    except:
      return False

# if is_admin():
#   #code of your program
#   c = command('netsh wlan show wlan')
#   print(c)
# else:
#   #re-run the program with admin
#   ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#   print(0x000001797BCC2440)
#   # c = command('netsh wlan show wlan')
#   # print(c)

pprint.pprint('    hello world' )
print('   hello world')
