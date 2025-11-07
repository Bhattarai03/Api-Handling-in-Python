import speech_recognition as sr
import webbrowser
import pyttsx3
import Music_Library


recognizer =sr.Recognizer()
engine =pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
         webbrowser.open("https://google.com")
    elif"open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    elif"open linkedin " in c.lower():
         webbrowser.open("https://linkedin.com")
    elif"open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif"open github " in c.lower():
         webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=Music_Library.Music[song]
        webbrowser.open(link)
    else:
        print("Improper Command")
    
if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
    # Listen for the wake up call
    # Obtain audio from microphone

        r=sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                  print("Listening......")
                  audio=r.listen(source,timeout=2,phrase_time_limit=3)
            
            word=r.recognize_google(audio)
            if (word.lower() =="google"):
                 speak("Yah")
            # Listen for Command
            with sr.Microphone() as source:
                 print("Rhino  Activated")
                 audio=r.listen(source)
                 command=r.recognize_google(audio)

            

                 processcommand(str(command))

    
        except Exception as e:
         print("Error:{0}".format(e))
    

    
