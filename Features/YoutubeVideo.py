import pywhatkit
from CommonFunctions import inputCommand, speak, desktop_assistant, user

def play_video_in_youtube():
    print(desktop_assistant + ": which video or movie should i play for you sir?")
    speak("which video or movie should i play for you sir?")
    video_name = inputCommand()
    print(user + ":" + video_name)
    print(desktop_assistant + ": Playing " + video_name + " in youtube!")
    speak("Playing " + video_name + " in youtube!")
    pywhatkit.playonyt(video_name)