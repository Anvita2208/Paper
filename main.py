import speech_recognition as sr
import webbrowser
import pyttsx3
import MuLib
import openai
import requests


recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ENTER_YOUR_API"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = openai.OpenAI(api_keys = "your_API")


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
    messages = [
        {"role": "user", "content": "You are a virtual assistant named Paper, skilled in general tasks like Alexa and Siri."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    if "open Youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    if "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://www.Linkedin.com")
    if "open chatgpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com")
    if "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    if "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MuLib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d06d6435124e47c6ad9045a1c28fc648")
        if r.status_code == 200:
            # paste the json response
            data = r.json

            # extact the aritcles
            articles = data.get("articles", [])

            # print the headlines
            for article in articles:
                speak(article["title"])
    else:
        # let openAI handle the request
        output = aiProcess(c)
        speak(command)
        pass
    

if __name__ == "__main__":
    speak("Paper talking...")
    while True:
        # listen for the wake word "Paper"
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = recogniser.recognize_google(audio)
            if(word.lower() == "paper"):
                speak("yes")
                # listen for command
            with sr.Microphone() as source:
                print("Paper Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                
                processCommand(command)

        except Exception as e:
            print(f"Paper error; {0}".format(e))
