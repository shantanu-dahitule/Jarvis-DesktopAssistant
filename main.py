
import pyttsx3
import datetime
import speech_recognition as sr

'''
importing voices to make assistant speakable :-p
'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
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
    speak("I am Jarvis a desktop assistant to help you. Please tell me how may I help you....")
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
        print("Wait for an instance...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
       # print(e)

        print("I am unable to get you please speak again...")
        return "None"
    return query
if __name__ == "__main__":
    wish()
    takeCommand()
