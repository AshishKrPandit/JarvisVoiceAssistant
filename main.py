
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  #User defined module 
import requests



recognizer = sr.Recognizer()

params = {"country": "in",
            "newsapi":"API_KEY" #Add your own NewsApi
          }


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://www.google.com/")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=bdde32e642cc49efab1f3cb93f35d14c", params=params)
        if response.status_code == 200:
            #parse the JSON response
            data = response.json()
            #Extract the artical
            articles = data.get('articles', [])
            #print the top headline
            for article in articles:
                speak(article['title'])
    
    
if __name__ =="__main__":
    speak("Initializing jarvis")

    while True:
        # Listen for the weak word "jarvis"
        # obtain audio from the microphone
    
        r = sr.Recognizer()
        print("recogning..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Recognized:", word)
            print("Condition check:", "jarvis" in word.lower())
            if "jarvis" in word.lower():
                speak("ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                processCommand(command)


        except Exception as e:
            print("error; {0}".format(e))