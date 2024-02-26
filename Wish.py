import datetime
from CommonFunctions import speak, desktop_assistant

def wish_and_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    g_t = time.split(':')
    hrs = int(g_t[0])
    if 5 <= hrs <= 12:
        print(desktop_assistant + ": Good Morning Sir!")
        speak("Good Morning Sir!")
    elif 12 <= hrs <= 17:
        print(desktop_assistant + ": Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif 17 <= hrs <= 21:
        print(desktop_assistant + ": Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print(desktop_assistant + ": Good Night Sir!")
        speak("Good Night Sir!")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(desktop_assistant + ": It's " + current_time + " Sir!")
    speak("It's " + current_time + " Sir!")