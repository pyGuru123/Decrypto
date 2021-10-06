import os
from sys import platform
def check_root():
    if os.geteuid() != 0:
        exit("For the first time to run this program You need to have root privileges .After that continue as a normal user . \nPlease try again, this time using 'sudo'. Exiting.")

try:
    import pyaudio
except:
    print("\nPlease wait first time installation ongoing .....")
    if platform == "linux" or platform == "linux2":
        #Linux
        check_root()
        os.system('apt-get install python3-pyaudio')
        quit()
    elif platform == "win32":
        #Windows
        os.system('pipwin install pyaudio')
try:
    import speech_recognition as sr
    import wikipedia
    from gtts import gTTS
    from playsound import playsound
except:
    print("\nPlease install all requirements from requirements.txt file")

speech=sr.Recognizer()
with sr.Microphone() as source:
    print("\nSay something . Listening ......")
    playsound("audio/ss.mp3")
    speech.adjust_for_ambient_noise(source, duration = 1)
    audio=speech.listen(source)

try:
    search=speech.recognize_google(audio)
    search_query=gTTS(search,lang="en")
    search_query.save("audio/search.mp3")
    print("\nSearching for " + search)
    playsound("audio/sf.mp3")
    playsound("audio/search.mp3")

    summary=wikipedia.summary(search,sentences=1)
    print(summary)
    tts=gTTS(summary,lang="en")
    tts.save("audio/wiki.mp3")
    playsound("audio/wiki.mp3")

except:
    print("Some error occured.")
    playsound("audio/error.mp3")