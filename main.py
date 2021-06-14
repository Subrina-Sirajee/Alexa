import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import smtplib
import cv2
import random
from requests import get


listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<=12:
        talk("good morning")
    elif hr>=12 and hr<=18:
        talk("good afternoon")
    else:
        talk("good evening")
    talk("I am Subrina. How can I help you?")





def take_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold=1
        voice= listener.listen(source,timeout=1,phrase_time_limit=5)

    try:
        command=listener.recognize_google(voice,language="en-in")
        command=command.lower()
        print(f"you said: {command}")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return command


def run_alexa():
    command=take_command()
    if "play a music" in command:
        music_path="D:\\music"
        songs = os.listdir(music_path)
        rd=random.choice(songs)
        os.startfile(os.path.join(music_path,rd))
    elif "play" in command:
        song=command.replace("play","")
        talk("playing" + song)
        print("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("current time is: " + time)

    elif "wikipedia" in command:
        obj=command.replace("wikipedia","")
        info=wikipedia.summary(obj,2)
        print("Searching wikipedia...")
        print("According to wikipedia, "+info)
        talk("According to wikipedia, "+info)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "open youtube" in command:
        webbrowser.open("www.youtube.com")

    elif "open google" in command:
        print("Mam, what should I search on google")
        talk("Mam, what should I search on google")
        cm=take_command()
        webbrowser.open(f"{cm}")

    elif "open facebook" in command:
        webbrowser.open("www.facebook.com")

    elif "open stackoverflow" in command:
        webbrowser.open("www.stackoverflow.com")

    elif "open netbeans"  in command:
        code_path="C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
        os.startfile(code_path)

    elif "open code blocks"  in command:
        code_path="C:\\Program Files\\CodeBlocks\\codeblocks.exe"
        os.startfile(code_path)

    elif "open xampp" in command:
        code_path="C:\\xampp\\xampp-control.exe"
        os.startfile(code_path)

    elif "open notepad" in command:
        code_path="%windir%\\system32\\notepad.exe"
        os.startfile(code_path)

    elif "open command promt" in command:
        code_path="%windir%\\system32\\cmd.exe"
        os.startfile(code_path)

    elif "open camera" in command:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow("webcam",img)
            k=cv2.waitKey(50)
            if k==27:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif "ip address" in command:
        ip=get("https://api.ipify.org").text
        print(ip)
        talk(f"your IP address is: {ip}")


    elif "stop" in command:
        print("Bye sabrina. Talk to you agian")
        talk("Bye sabrina. Talk to you agian")
        exit()
    else:
        talk("Please tell again!!")
if __name__ == "__main__":
    wish()


while True:
    run_alexa()