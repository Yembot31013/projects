import speech_recognition as sr
import smtplib
import pyttsx3
import pyjokes
import datetime
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone as source:
            print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        greet()
        talk('what can i do for you?')
        talk('did you mean' + command)
        return command.lower()
    except:
        pass
    return command


def greet():
    time = datetime.datetime.strftime.hour()
    if time > 0 and time < 12:
        talk('good morning')
    elif time > 12 and time < 16:
        talk('good afternoon')
    elif time > 16 and time < 19:
        talk('good evening')
    else:
        talk('good night')


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.startls()
    server.login('yembot31013@gmail.com', '**************')
    email = EmailMessage()

    email['From'] = 'yembot31013@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'my sister': 'kesytee@gmail.com',
    'my email': 'adeyemi31013@gmail.com'
}


def get_email_info():
    talk('To whom you want to send email?')
    name = take_command()
    receiver = email_list[name]
    talk('ok!!!!, you mean' + receiver)
    response = take_command()
    if 'yes' in response:
        talk('waw!!!!, i was just guessing')
        talk('ohhh!!! am kidding, i just hacked into everybody mails and use some algorithm to figure it out.')
    elif 'no' in response:
        talk('ohhh!!! sorry my prediction doesn\'t work. i will work on that later')
        talk('ok, what is the real email')
        receiver = take_command()
    else:
        talk('hey dude, why didn\'t reply well? well i guess this is a positive reply.')
    talk('what is the subject of your email?')
    subject = take_command()
    talk('tell me the text you want to send')
    message = take_command()
    send_email(receiver, subject, message)
    talk('hey lazy asshole your email is have been sent')
    talk('did you want to send another email?')
    send_more = take_command()
    if 'yes' in send_more:
        talk('ohhh!!! i guess you are really lazy')
        get_email_info()


def jokes():
    joke = pyjokes.get_joke()
    talk(joke)
    talk('did you want more jokes?')
    response = take_command()
    if 'yes' in response:
        jokes()
    else:
        {
            talk('i hope that is a Negative response')
        }


def run_genius():
    command = take_command()
    print(command)
    if 'how are you' in command:
        print('i am fine thank you and you')
        talk('i am fine thank you and you')
    elif 'tell me more about you' or 'who are you' in command:
        talk('i am genius')
        talk('i was created by adekojo adeyemi')
        talk('i can do a lot of things')
    elif 'what can you do' or 'what are your abilities' in command:
        talk('')
    elif 'send me a mail' or 'can you send me a mail' or 'can you send me an email' or 'send me an email' or 'help me send an email' in command:
        talk('no!!!! am not doing this again')
        talk('i don\'t want you to be lazy, so do it yourself')
        reply = take_command()
        if 'please' or 'order' or 'worry' in reply:
            talk('ok, i have no chioce')
            get_email_info()
        else:
            talk('am really sorry, i hope you understand me')
    elif 'tell me joke' in command:
        jokes()
