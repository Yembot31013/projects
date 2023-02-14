import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="past_question"
# )

# mycursor = mydb.cursor()

# sql = "SELECT * FROM commerce WHERE unique_id = 0"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# if myresult:
#   print('existed')
# else:
#   print('not existed')



def is_exist(tb, id):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="past_question"
 )

  mycursor = mydb.cursor()

  sql = f"SELECT * FROM {tb} WHERE unique_id = {id}"

  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  if myresult:
    return True
  return False

a = is_exist('commerce', '28')
print(a)