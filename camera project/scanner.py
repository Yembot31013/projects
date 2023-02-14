import socket

ipaddress = input('[+] Enter target to scan')
port = 22

try:
    sock = socket.socket()
    sock.settimeout(0.5)
    sock.connect((ipaddress, port))
    print('[+] port 22 is opened')

except Exception as e:
    print(e)
    print('\n')
    print('[-] port 22 is closed')
