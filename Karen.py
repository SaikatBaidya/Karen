from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Boss!")
    else: 
        speak("Good evening Boss!")
    speak("How may I help you today?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karenaigenjutsu@gmail.com', 'gomugomunoredroc')
    server.sendmail('karenaigenjutsu@gmail.com', to, content)
    server.close()


def takeCommand():
    #takes input from user through mic and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"I heard: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            print("Scanning scriptures...")
            speak("Scanning scriptures...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to ancient scriptures")
            speak("According to ancient scriptures")
            speak(results)
            print(results)
       
        #elif 'open youtube' in query:
            #webbrowser.open("youtube.com")

        #elif 'open google' in query:
            #webbrowser.open("google.com")

        #elif 'open stack overflow' in query:
            #webbrowser.open("stackoveflow.com")

        elif 'open' in query:
            a = query.split()
            b = a[1]
            webbrowser.open(b + '.com')

        elif 'start code' in query:
            codePath = "C:\\Users\\saika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")

        elif 'email to karen' in query:
            try:
                speak('What should the email say?')
                content = takeCommand()
                to = "karenaigenjutsu@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Failed to send the Email")
                speak("Failed to send the Email")
        
        elif 'go to sleep' in query:
            exit()
