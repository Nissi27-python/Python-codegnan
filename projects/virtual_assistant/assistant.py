# importing modules
import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import datetime

#create engine for text to speech
engine = pyttsx3.init()

#speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# take command functions
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("you said: ", command)
            return command
        except:
            return ""
# run assistant
def run_assistant():
    command = take_command()
    # if command contains time
    if 'time' in command:
        time = datetime.datetime.time()
        speak(f"Current time is: ", time)
        print(f"Current time is: ", time)
    # if command contains open notepad
    elif 'open notepad' in command:
        speak("Opening Notepad")
        print("Opening Notepad")
        os.system('notepad')

    # if command contains open youtube
    elif 'open youtube' in command:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    # if command contains hey Nissi
    elif 'hey Nissi' in command:
        query = command.replace("hey Nissi","")
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            print(f"Searching for {query}")
            webbrowser.open(url)
    # if command contains stop
    elif 'stop' in command:
        speak("Okay, bye see you again")
        exit()
    else:
        print("I am here to assist you ask like current time, open youtube, search for something...")
        
# main
if __name__ == "__main__":
    name = input("Enter your name: ",)
    speak(f"Hey hi {name}, I am here to assist you ask like current time, open youtube, search for something...")
    while True:
        run_assistant()



    
