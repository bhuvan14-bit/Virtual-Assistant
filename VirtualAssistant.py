import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'virtualexa' in command:
                command = command.replace('virtualexa', '')
                print(command)
    except:
        pass
    return command


def run_virtualexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'Lets play game' in command:
        talk('sorry buddy,I have a headache')
    elif 'are you in earth' in command:
        talk('Yes Buddy I am in earth')
    elif 'what are the language spoken in India' in command:
        talk('Hindi Tamil Telugu English Kannada Malayalam Gujarathi Punjabi and many more')
    elif 'Which company presented BMW Cars for his employees' in command:
        talk('It is a leading IT Company in india named Kissflow')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry buddy can you repeat command again.')


while True:
    run_virtualexa()
