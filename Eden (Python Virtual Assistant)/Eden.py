import random # for random responses
import time # for sleep() function
import webbrowser # for browser searching response
import speech_recognition as sr # to process audio inputs
from playsound import playsound # for sound-playing response
from gtts import gTTS # using Google Text To Speech API module for audio response from virtual assistant
import os # import os for file handling
import datetime # for time response
import pywhatkit # for searching and playing youtube videos
import wikipedia # for searching on wikipedia


listener = sr.Recognizer() # using Recognizer() function from the speech_recognition library as the listener

'''
Function to start taking voice input
Parameters :
- ask : String, which will be spoken by the program
Return :
voice_data : String generated from speech to text conversion from the voice input
'''
def record(ask):
    playsound("sfx/eden_start.mp3") # starting tone
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = listener.listen(source)
        voice_data = ''
        try:
            voice_data = listener.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't quite get that")
        except sr.RequestError:
            speak("Sorry, my speech service is down right now")
        return voice_data

def respond(voice_data): # responses
    if 'your name' in voice_data:
        speak("My name is Eden, your personal virtual assistant. At your service.")
    elif 'how are you' in voice_data:
        options = ["i'm doing well, thank you", "great! how about you?", "never been better"]
        answer = random.choice(options)
        speak(answer)
    elif ('who is' in voice_data) or ('who are' in voice_data):
        person = voice_data.replace('who is ', '') if 'who is ' in voice_data else voice_data.replace('who are ', '')
        info = wikipedia.summary(person, 1)
        speak(info)
    elif ('what is' in voice_data) or ('what are' in voice_data):
        definition = voice_data.replace('who is ', '') if 'who is ' in voice_data else voice_data.replace('who are ', '')
        info = wikipedia.summary(definition, 1)
        speak(info)
    elif 'play' in voice_data:
        key = voice_data.replace('play ', '')
        pywhatkit.playonyt(key)
        speak(voice_data.replace('play', 'playing,'))
    elif 'search' in voice_data:
        search = record('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak("Here is what I found for " + search)
    elif 'location' in voice_data:
        location = record('What is the location')
        url = 'https://google.nl/maps/place/' + location + "/&amp;"
        webbrowser.get().open(url)
        speak("Here is the location of " + location)
    elif 'date' in voice_data:
        current_date = datetime.date.today().strftime("%d %b %Y")
        speak("Current date is " + current_date)
    elif 'time' in voice_data:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)
    elif 'speak japanese' in voice_data:
        sounds = ['sfx/dame.mp3','sfx/kawaii.mp3','sfx/ohayou.mp3','sfx/explosion.mp3','sfx/moshimoshi.mp3']
        sound = random.choice(sounds)
        playsound(sound)
    elif 'thank you' in voice_data:
        responds = ["You're welcome", 'My pleasure', "No problem"]
        respond = random.choice(responds)
        speak(respond)
        exit()

'''
Function to make a file to contain text for text to speech. At the end it will remove the file automatically
Parameters :
- audio : String, containing response from the program
'''
def speak(audio):
    tts = gTTS(text = audio, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print(audio)
    playsound(audio_file)
    os.remove(audio_file)

'''
Function to start listening
'''
def start():
    print("Listening...")
    with sr.Microphone() as source:
        audio = listener.listen(source)
        data = ''
        try :
            data = listener.recognize_google(audio)
            if 'eden' in data.lower():
                voice_data = record('Yes?')
                voice_data = voice_data.lower()
                respond(voice_data)
            else:
                pass
        except sr.UnknownValueError:
            pass

# starting the program
time.sleep(1)
while(1):
    start()
    

