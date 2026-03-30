from idlelib import query
from time import strftime
from openai import OpenAI
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import pyaudio
import time

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.0)

def say(text):
    global is_speaking

    import pyttsx3
    engine = pyttsx3.init('sapi5')

    is_speaking = True
    engine.say(text)
    engine.runAndWait()
    is_speaking = False

    time.sleep(1)



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300


        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except:
            return "None"

    try:
        print(" Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" You said: {query}")
        return query.lower()

    except:
        return "None"




# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
#
# def ask_ai(question):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "user", "content": question}
#             ]
#         )
#         return response.choices[0].message.content
#
#     except Exception as e:
#         print("Error:", e)
#         return "Sorry, AI is not available right now"




def manual_ai(text):
    text = text.lower()

    if "what is api" in text:
        return "API means Application Programming Interface. It allows two software to communicate."

    elif "what is python" in text:
        return "Python is a programming language used for AI, web development and more."

    elif "who are you" in text:
        return "I am Kartik AI, your personal assistant."

    elif "time" in text:
        import datetime
        return str(datetime.datetime.now().strftime("%H:%M"))

    elif "who is your founder" in text:
        return "My founder is kartik "


    else:
        return "Sorry, I don't know that yet"

if __name__ == '__main__':
    print('Hello This is Kartik.Ai')
    say("hello i am kartik.Ai")
    last_command = ""
    while True:
        # print("listening...")
        if is_speaking:
            continue
        text = takeCommand()

        if text != 'None':
            say(text)

        sites = [
            ['youtube', 'https://www.youtube.com'],
            ['google', 'https://www.google.com'],
            ['wikipedia', 'https://en.wikipedia.org'],
            ['instagram', 'https://www.instagram.com'],
            ['facebook', 'https://www.facebook.com'],
            ['twitter', 'https://twitter.com'],
            ['linkedin', 'https://www.linkedin.com'],
            ['chatgpt', 'https://chatgpt3.github.io']
        ]

        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"opening {site[0]} sir")
                import webbrowser

                webbrowser.open(site[1])


            if "open vscode" in text.lower():
                say("opening vscode")
                os.startfile("C:\\Users\DELL\AppData\Local\Programs\Microsoft VS Code")



        if 'time' in text.lower():
            strftime = strftime("%I:%M:%S")
            say(f"Sir the current time is {strftime}")

        # text = takeCommand()
        #
        # from openai import OpenAI
        #
        # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        #
        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[{"role": "user", "content": "Hello"}]
        # )
        #
        # print(response.choices[0].message.content)

        text = takeCommand()
        if text == "None":
            continue

        if text == last_command:
            continue

        last_command = text

        response = manual_ai(text)
        print(response)
        say(response)

        time.sleep(2)
        last_command = ""






