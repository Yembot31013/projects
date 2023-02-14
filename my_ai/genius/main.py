import requests
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
import webbrowser
from decouple import config

import pyttsx3
import speech_recognition as sr
from decouple import config
import webbrowser
from datetime import datetime
import os
import subprocess as sp
from random import choice
from utils import opening_text
from pprint import pprint
import subprocess
from memory import no_respond

USERNAME = 'yembot'
BOTNAME = 'Genius'
OPENWEATHER_APP_ID = '7c3e99ca85da93503dbcfec9dcc6c98d'
# TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL = 'yembot31013@gmail.com'


YOUTUBE = "https://www.youtube.com"
GOOGLE = "https://www.google.com"
GMAIL = "https: // mail.google.com/mail"
YEMI = 'Master adekojo emmanuel adeyemi is a nigerian and he is the man behind my creation, He is a man of determination and a has a great dreaam to the society. if i have the chance to be a human in my second life, then i will love to be like my master yembot. '

countrys = {
    "nigeria": 234,
    "india": 91
}

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def get_info(query):
    kit.info(query)


def send_whatsapp_message(country, number, message):
    kit.sendwhatmsg_instantly(f"+{country}{number}", message)


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def youtube():
    webbrowser.open_new_tab(YOUTUBE)


def google():
    webbrowser.open_new_tab(GOOGLE)


def gmail():
    webbrowser.open_new_tab(GMAIL)

# Greet the user


def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


def no_respond():
    pass


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(
                f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'who is' in query or 'what is' in query:
            speak('who or what do you want to search for, sir?')
            correct = take_user_input().lower()
            if correct == 'yemi' or correct == 'adeyemi' or correct == 'yembot':
                speak(YEMI)
            else:
                result = wikipedia.suggest(correct)
                print(result)
                if result != None:
                    speak(f'did you mean {result}, sir?')
                    print(f'did you mean {result}, sir?')
                    query = take_user_input().lower()
                    if 'no' in query:
                        results = wikipedia.search(correct)
                    else:
                        results = wikipedia.search(result)
                else:
                    results = wikipedia.search(correct)
                if results == []:
                    ans = wikipedia.summary(result, sentences=2)
                    speak(f"According to Wikipedia, {ans}")
                    speak("For your convenience, I am printing it on the screen sir.")
                    print(ans)
                else:
                    for i in results:
                        speak(f'sorry sir, did you mean {i}')
                        print(f'sorry sir, did you mean {i}')
                        query = take_user_input().lower()
                        if 'yes' in query:
                            ans = wikipedia.summary(i, sentences=2)
                            if ans != None:
                                speak(f"According to Wikipedia, {ans}")
                                speak(
                                    "For your convenience, I am printing it on the screen sir.")
                                print(ans)
                                break
                            else:
                                print('no repond.......')

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        # elif "send whatsapp message" in query:
        #     speak('please tell me the country of the receiver sir')
        #     country = take_user_input().lower()
        #     country = countrys[country]
        #     speak(
        #         'On what number should I send the message sir? Please enter in the console: ')
        #     number = input("Enter the number: ")
        #     speak("What is the message sir?")
        #     message = take_user_input().lower()
        #     send_whatsapp_message(country, number, message)
        #     speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak(
                    "Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(
                f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(
                f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        elif 'who are you' in query or 'what can you do' in query:
            speak(f'I am {BOTNAME} version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by yembot")
            print("I was built by yembot")
        elif "open stackoverflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the current time is {strTime}")

        elif "log off" in query or "sign out" in query:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        # elif 'open gmail' in query or 'open mails' in query:
        #     gmail()
        #     speak("Google Mail open now")

        else:
            speak("sorry sir, i didn't have response to that sir.")
            speak("but i promise to give you a response as soon as possible.")
            no_respond.append(query)
