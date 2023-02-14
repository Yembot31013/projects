import wikipedia
import pyttsx3
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


YEMI = 'Master adekojo emmanuel adeyemi is a nigerian and he is the man behind my creation, He is a man of determination and a has a great dreaam to the society. if i have the chance to be a human in my second life, then i will love to be like my master yembot. '

# Text to Speech Conversion


def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


def speaks():
    speak('who or what do you want to search for, sir?')
    correct = input('your response: ').lower()
    if correct == 'yemi' or correct == 'adeyemi' or correct == 'yembot':
        speak(YEMI)
    else:
        result = wikipedia.suggest(correct)
        print(result)
        if result != None:
            speak(f'did you mean {result}, sir?')
            print(f'did you mean {result}, sir?')
            query = input('your response: ').lower()
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
                query = input('your response: ').lower()
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


speaks()
