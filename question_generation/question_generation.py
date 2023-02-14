import requests
import os
import getpass
import time
import sys
from colorama import Fore
import mysql.connector

def is_exist(tbs, ids):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="past_question"
 )

  mycursor = mydb.cursor()

  sql = f"SELECT * FROM {tbs} WHERE unique_id = {ids}"

  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  if myresult:
    return True
  return False

def create_database(db_name = "past_question"):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  )

  mycursor = mydb.cursor()
  mycursor.execute(f"CREATE DATABASE {db_name}")
  return True, db_name

def check_database(db_name = "past_question"):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  )

  mycursor = mydb.cursor()
  mycursor.execute("SHOW DATABASES")

  for x in mycursor:
    if db_name in x:
      return True
  return False

def create_table(tb_name, db_name = "past_question"):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=db_name
  )

  mycursor = mydb.cursor()

  mycursor.execute(f"CREATE TABLE {tb_name} (id INT AUTO_INCREMENT PRIMARY KEY, question longtext, image VARCHAR(255), answer VARCHAR(255), optionA longtext, optionB longtext, optionC longtext, optionD longtext, exam_type VARCHAR(255), examyear VARCHAR(255), solution longtext, unique_id VARCHAR(255))")
  return True, f"table {tb_name} successfully created in {db_name} database"

def check_table(tb_name, db_name = "past_question"):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=db_name
  )

  mycursor = mydb.cursor()

  mycursor.execute("SHOW TABLES")

  for x in mycursor:
    if tb_name in x:
      return False
  return True

def insert_db(tb_name, question, image, answer, optionA, optionB, optionC, optionD, exam_type, examyear, solution, unique_id, db_name = "past_question"):
  global number
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=db_name
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO " + tb_name + " (question, image, answer, optionA, optionB, optionC, optionD, exam_type, examyear, solution, unique_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (question, image, answer, optionA, optionB, optionC, optionD, exam_type, examyear, solution, unique_id)
  mycursor.execute(sql, val)

  mydb.commit()
  print(Fore.BLUE + str(mycursor.lastrowid), "record inserted.")
  

#endpoint = 'https://question.aloc.com.ng/api/v2/m?subject=mathematics'
#AccessToken = 'ALOC-fa77c5b56cc4a7ba95d9'

def make_request(subject, types = '', times = 1, accesstoken='ALOC-fa77c5b56cc4a7ba95d9'):
  d = 0
  timer = 1
  if types == '':
    types='utme'
  if times == 0:
    times=1
  while timer <= times:
    ds = 0
    try:
        os.system('cls')
        print(f"getting {subject} past_question....\n {timer} times")
        if accesstoken == '':
          my_headers = {'AccessToken':'ALOC-fa77c5b56cc4a7ba95d9'}
        else:
          my_headers = {'AccessToken':accesstoken}
        response = requests.get('https://question.aloc.com.ng/api/v2/m?', params = {'subject': subject, 'type': types}, headers = my_headers, allow_redirects=False)
        response = response.json()
        timer = timer + 1
        if check_database():
          valid = check_table(tb_name = subject)
          if valid:
            valids, output = create_table(tb_name=subject)
            if valids:
              print(Fore.GREEN + str(output))
              try:
                responses = response['data']
                for i in responses:
                  if is_exist(tbs=subject, ids = i['id']):
                    ds = ds + 1
                    d = d + 1
                    print(Fore.RED + 'duplicate found and removed')
                  else:
                    insert_db(tb_name=subject, question=i['question'], image=i['image'], answer=i['answer'], optionA = i['option']['a'], optionB = i['option']['b'], optionC = i['option']['c'], optionD = i['option']['d'], exam_type= i['examtype'], examyear = i['examyear'], solution = i['solution'],  unique_id = i['id'])
                os.system('cls')
                print(Fore.LIGHTRED_EX + f"{str(ds)} duplicate found and avoided to {subject} database")
                print(Fore.RED + f"in general, {str(d)} duplicate found and avoided to {subject} database")
                print(Fore.GREEN + """
                =====================================
                      Data Inserted successfully
                =====================================
                """)
                time.sleep(5)
              except Exception as e:
                print(responses)
                print(f"{e} - first")
                print(Fore.LIGHTRED_EX + """
                =====================================
                    Data Inserted unsuccessfully
                =====================================
                """)
                print(Fore.RED + "\n\n This is an error from the API and not the code")
                time.sleep(10)
                continue
            else:
              print(Fore.LIGHTRED_EX + f"unable to create table {subject}")
              time.sleep(10)
              input_fields()
          else:
            try:
                responsea = response['data']
                for i in responsea:
                  if is_exist(tbs=subject, ids = i['id']):
                      d = d + 1
                      ds = ds + 1
                      print(Fore.RED + 'duplicate found and removed')
                  else:
                    insert_db(tb_name=subject, question=i['question'], image=i['image'], answer=i['answer'], optionA = i['option']['a'], optionB = i['option']['b'], optionC = i['option']['c'], optionD = i['option']['d'], exam_type= i['examtype'], examyear = i['examyear'], solution = i['solution'],  unique_id = i['id'])
                os.system('cls')
                print(Fore.LIGHTRED_EX + f"{str(ds)} duplicate found and avoided to {subject} database")
                print(Fore.RED + f"in general, {str(d)} duplicate found and avoided to {subject} database")  
                print(Fore.GREEN + """
                  =====================================
                        Data Inserted successfully
                  =====================================
                  """)
                time.sleep(5)
            except Exception as e:
              print(responsea)
              print(f"{e} - third")
              print(Fore.RED + """
              =====================================
                  Data Inserted unsuccessfully
              =====================================
              """)
              print(Fore.LIGHTRED_EX + "\n\n This is an error from the API and not the code")
              time.sleep(10)
              continue
        else:
          valid, name = create_database()
          if valid:
            print(Fore.LIGHTGREEN_EX + f"{name} as been created successfully")
            valids, output = create_table(tb_name=subject)
            if valids:
              print(Fore.LIGHTGREEN_EX + output)
              try:
                response = response['data']
                for i in response:
                  if is_exist(tbs=subject, ids = i['id']):
                    d = d + 1
                    ds = ds + 1
                    print(Fore.RED + 'duplicate found and removed')
                  else:
                    insert_db(tb_name=subject, question=i['question'], image=i['image'], answer=i['answer'], optionA = i['option']['a'], optionB = i['option']['b'], optionC = i['option']['c'], optionD = i['option']['d'], exam_type= i['examtype'], examyear = i['examyear'], solution = i['solution'],  unique_id = i['id'])
                os.system('cls')
                print(Fore.LIGHTRED_EX + f"{str(ds)} duplicate found and avoided to {subject} database")
                print(Fore.RED + f"in general, {str(d)} duplicate found and avoided to {subject} database")
                print(Fore.GREEN + """
                =====================================
                      Data Inserted successfully
                =====================================
                """)
                time.sleep(5)
              except Exception as e:
                print(response)
                print(f"{e} - second")
                print(Fore.RED + """
                =====================================
                    Data Inserted unsuccessfully
                =====================================
                """)
                print(Fore.LIGHTRED_EX + "\n\n This is an error from the API and not the code")
                time.sleep(10)
                continue
            else:
              print(Fore.LIGHTRED_EX + f"unable to create table {subject}")
              time.sleep(10)
              input_fields()
          else:
            print(Fore.LIGHTRED_EX + f"creating {name} database was unsuccessfully")
            time.sleep(10)
            input_fields()
    except requests.exceptions.HTTPError:
        print(Fore.LIGHTRED_EX + """
        ###########################################
                    INVALID RESPONSE 
        ###########################################
          The json responses look strange, the
          problem can be from the input provided
          or from the api rules.
        """)
        print(Fore.RESET + "terminating program...")
        break
    except requests.exceptions.ConnectionError:
        os.system('cls')
        print(Fore.LIGHTRED_EX + """
        ###########################################
                    CONNECTIONS ERROR 
        ###########################################
          This is caused when your network failed,
          DNS error so check your Internet.
        """)
        print(Fore.LIGHTGREEN_EX + "trying to reconnect...")
        time.sleep(10)
        print(Fore.RESET + "terminating program...")
        time.sleep(5)
        input_fields()
    except requests.exceptions.RequestException:
        os.system('cls')
        print(Fore.LIGHTRED_EX + "An unexpected error just occurs")
        time.sleep(5)
        print(Fore.LIGHTGREEN_EX + "please wait while we fix the prolem...")
        time.sleep(20)
        print(Fore.RESET + "terminating program...")
        time.sleep(10)
        input_fields()
    except KeyboardInterrupt:
      confirm = input(Fore.RESET + "\n\n\n did you want to terminate this program [Y/N]: ").lower()
      if confirm == 'n':
        continue
      else:
        os.system('cls')
        exit()
  time.sleep(3)
def banner():
  os.system('cls')
  print(Fore.GREEN + """\n\n
    ################################################# ########################
   |            supported subject ==> subject        |    Exams Supported     |
    ################################################# ########################
   English language               ==> english        |
   Mathematics                    ==> mathematics    |        UTME
   Commerce                       ==> commerce       | 
   Accounting                     ==> accounting     |        
   Biology                        ==> biology        |    WASSCE(limited)
   physics                        ==> physics        |
   Chemistry                      ==> chemistry      |
   English literature             ==> englishlit     |   POST-UTME(very limited) 
   Government                     ==> government     |
   Christain Religious Knowledge  ==> crk            |############################
   Geography                      ==> geography      |     Years Supported        |
   Economics                      ==> economics      |############################
   Islamic Religious Knowledge    ==> irk            |This depends on the subject,
   Civic Education                ==> civiledu       |but please note, the years
   Insurance                      ==> insurance      |vary from 2001 to 2013
   Current Affairs                ==> currentaffairs |
   History                        ==> history        |
  ___________________________________________________!______________________________|  
  \n\n\n""")

def input_fields():
  banner()
  subject = input(Fore.LIGHTYELLOW_EX + '[+] Enter the subject(split with comma(,) for multiple subject): ').lower()
  types = input(Fore.LIGHTYELLOW_EX + '[+] Enter the exam type(default = utme) (e.g: utme):').lower()
  requesters = input(Fore.LIGHTYELLOW_EX + '[+] Enter the number of time you want to make request(default=1): ')
  token = getpass.getpass(Fore.LIGHTYELLOW_EX + '[+] Enter the accesstoken if required (default = \'ALOC-fa77c5b56cc4a7ba95d9\'): ')
  confirm = input(Fore.YELLOW  + "did you want to continue [Y/N]: ").lower()
  if confirm == 'n':
    input_fields()
  else:
    if requesters == '':
      requesters = 0

    if ',' in subject:
      for i in subject.split(','):
        make_request(subject=i.strip(' '), types=types, accesstoken=token, times=int(requesters))
    else:
          make_request(subject=subject, types=types, accesstoken=token, times=int(requesters))

input_fields()
