import socket

sock = socket.socket()
try:
    sock.connect(('192.168.43.145'))
    print('port 22 is openned')

except Exception as e:
    print(e)
    print('\n')
    print('port 22 is closed')
