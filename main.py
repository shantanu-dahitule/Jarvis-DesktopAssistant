'''Library we need '''

'''IF you get error about pyaudio 
step1-> install pip install pywin
step2-> pywin install pyaudio
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
'''
importing voices to make assistant speakable :-p
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) #You can execute 
engine.setProperty('voice',voices[1].id)

'''Creating audio speker function'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour==12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis a static desktop assistant to help you. Please tell me how may I help you....")
'''
Tech command function: 
It takes microphone input and returns string output
'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
       # print(e)

        print("I am unable to get you please speak again...")
        return "None"
    return query
if __name__ == "__main__":
    wish()
    '''
    Now defining task which will Jarvis do

    '''
    
    while True:
        query = takeCommand().lower()

        if 'google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to google")
            speak(result)
            print(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open jio saavn' in query:
            webbrowser.open("https://www.jiosaavn.com/")
        elif 'open chrome' in query:
            codePath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.startfile(codePath)
        elif 'open vtop' in query:
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess") #This line for VIT student 
        elif 'covid update' in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/") # About CoVID Update
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open code' in query:
            codePath = "E:/Visual studio code installed here/Microsoft VS Code/Code.exe"
            os.startfile(codePath)  
        elif 'thank you' in query:
            speak('Happy to help you please run code to call me back, BYE BYE')
            query = query.replace("thank you", "")
            sys.exit()
