#Project : Building Voice assistant
# Import required modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from playsound import playsound
import cv2
from requests import get
import pyautogui as pg
import pywhatkit
from pywhatkit.remotekit import start_server
from flask import Flask, request
from datetime import timedelta
import sys
import time
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer
    
import pyjokes



# init function to get an engine instance for the speech synthesis
# The pyttsx3 module supports two voices first is male and the second is female which is provided by “sapi5” for windows.

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voice', voices[0].id)  #Use voices[1].id for female voice

#creating speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#creating wishMe function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Vrajesh!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Vrajesh !")
    else:
        speak("Good Evening Vrajesh !")

    speak("How may I help you sir ?")


#creating takeCommand function
def takeCommand():

    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()  # to recognize audio
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said  : {query}\n")

    except Exception as e:      
        print(e)
        print("Say that again please....")
        return "None"
    return query

#creating sendEmail function
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) #default mail submission port
    server.ehlo()
    server.starttls()
    server.login('thisisme@gmail.com','mypwd')
    server.sendmail('thisisme@gmail.com',to,content)
    server.close()



if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    speak("Heyyy!! This is jarvis ...your authentication is required to access my abilities.. what's the password")
    p = takeCommand()
    if(p =="ABCD 123"):
        mixer.init()
        mixer.music.load("C:\\location\\to\\audiofile\\startupsound.mp3") # Paste The audio file location 
        mixer.music.play() 
        time.sleep(6)
        
        speak("Password verified")
        wishMe()

        while True:
            query = takeCommand().lower()

        # to start execution of tasks
            if 'wikipedia' in query:
                 speak("Searching Wikipedia.....")
                 query = query.replace("wikipedia", "")
                 results = wikipedia.summary(query, sentences=3)
                 speak("According to Wikipedia..")
                 print(results)
                 speak(results)
            
            elif 'bored' in query:
                speak("Okay ! Let me tell you a joke")
                joke1 = pyjokes.get_joke(language = 'en',category = 'neutral')
                speak(joke1)
                speak("haha that was funny though")
                 
            elif 'open youtube' in query:
                 speak("Opening youtube..")
                 speak('Alright  ! , What should i search on youtube sir ?')
                 search = takeCommand().lower()
                 speak('Here is what i found on youtube sir !')
                 pywhatkit.playonyt(f"{search}")


            elif 'open google' in query:
                speak('Alright ! , What should I search on google sir ?')
                search = takeCommand().lower()
                speak('Here is your search result sir !')
                webbrowser.open(f"{search}")
            
            elif 'open netflix' in query:
                speak("Oh you want some fun , alright here we go sir!!!!")
                webbrowser.open('netflix.com')

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music on youtube' in query:
                speak('Alright  ! , Which song on youtube sir ?')
                search = takeCommand().lower()
                speak('Here is the song sir !')
                pywhatkit.playonyt(f"{search}")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The time is..{strTime}")

            elif 'open code' in query:
                speak("Opening visual studio code")
                path = "C:\\Users\vraje\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif 'open command prompt' in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif 'open notepad' in query:
                speak("Opening notepad")
                os.system('start Notepad')

            elif 'open camera' in query:
                speak("Doing !!! Make sure your face look good..")
                timeout = time.time() + 20
                cap = cv2.VideoCapture(0)
                while time.time() < timeout:
                    _ , frame = cap.read()
                    k = cv2.waitKey(1)
                    cv2.imshow('Frame', frame)
                   
                cap.release()
                cv2.destroyAllWindows()

            elif 'ip address' in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

          #for whatsApp message | Make Chrome as default browser
            elif 'send whatsapp message to friends group' in query:
                speak('what should I write to your friends sir ??')
                msg = takeCommand()
                ct = datetime.datetime.now()
                n = 2
                ft = ct + timedelta(minutes=n)
                Hours = ft.strftime('%H')
                Minutes = ft.strftime('%M')

                pywhatkit.sendwhatmsg_to_group("Friends group name", f"{msg}", int(Hours), int(Minutes))

            elif 'send whatsapp message to daddy' in query:
                speak('what should I write to your father sir ??')
                msg = takeCommand()
                ct = datetime.datetime.now()
                n = 2
                ft = ct + timedelta(minutes=n)
                Hours = ft.strftime('%H')
                Minutes = ft.strftime('%M')
                #+CC <-- country code followed by mobile number
                pywhatkit.sendwhatmsg("+CC**********", f"{msg}", int(Hours), int(Minutes))

            elif 'send whatsapp message to mom' in query:
                speak('what should I write to your mom sir ??')
                msg = takeCommand()
                ct = datetime.datetime.now()
                n = 2
                ft = ct + timedelta(minutes=n)
                Hours = ft.strftime('%H')
                Minutes = ft.strftime('%M')
                pywhatkit.sendwhatmsg("+CC**********", f"{msg}", int(Hours), int(Minutes))
                width,height = pg.size()
                # pg.click(width/2,height/2)
                # time.sleep(5)
                # prev_color = pg.pixel(int(width/2),int(height/2))
                # while prev_color == pg.pixel(int(width/2),int(height/2)):
                #     pass
                # time.sleep(3)
                pg.press("enter")

            elif 'email to admin' in query:
               try:
                   speak("What should I say to admin sir ?")
                   content = takeCommand()
                   to = "admin@gmail.com"
                   sendEmail(to,content)
                   speak("Email has been sent!!")
               except Exception as e:
                   print(e)
                   speak("Sorry sir! I am not able to send this email")
        
            elif 'bye' in query:
                speak('Bye sir !! Call me if you need any help')
                sys.exit()

            time.sleep(10)      #waits for 10 seconds after each iteration i.e. after executing of each task
            speak("Can i help you in any other work sir ???")

    else:
        speak("You are not my master")


