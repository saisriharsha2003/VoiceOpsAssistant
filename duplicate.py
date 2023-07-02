import datetime
import pyttsx3
import speech_recognition as sr
import os
import webbrowser as wb
import AppOpener
import cv2
user = "harsha"
assistant = 'Jarvis'
assistant = pyttsx3.init()
voices = assistant.getProperty("voices")
assistant.setProperty("voice", voices[0].id)


def output(audio):
    assistant.say(audio)
    assistant.runAndWait()


def inputCommand():
    rec = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        output("How can i help you {}?".format(user))
        rec.pause_threshold = 1
        # rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            query = rec.recognize_google(audio, language="en-IN")
        except Exception as e:
            output("Sorry,I can't hear you!")
    return query


if __name__ == '__main__':
    output("Hello {}! I am your personal desktop assistant".format(user))
    while 1:
        r = sr.Recognizer()
        query = inputCommand().lower()
        print(query)
        if query == 0:
            continue
        elif 'chrome' in query or 'google' in query:
            if 'open' in query:
                AppOpener.open("google chrome", match_closest=True)
            elif 'close' in query:
                AppOpener.close("google chrome", match_closest=True)
            elif 'search' in query:
                output('what should i search for you')
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application %s"
                search1 = inputCommand().lower()
                wb.open_new_tab(search1)
        elif 'vs code' in query or 'visual studio code' in query:
            if 'open' in query:
                AppOpener.open("visual studio code", match_closest=True)
            elif 'close' in query:
                AppOpener.close("visual studio code", match_closest=True)
        elif 'mail' in query:
            if 'open' in query:
                AppOpener.open('mail')
            elif 'close' in query:
                AppOpener.close('mail')
        elif 'vlc' in query:
            if 'open' in query:
                AppOpener.open('vlc media player')
            elif 'close' in query:
                AppOpener.close('vlc media player')
        elif 'camera' in query:
            if 'open' in query:
                AppOpener.open("camera", match_closest=True)
            elif 'close' in query:
                AppOpener.close("camera", match_closest=True)
            elif 'capture photo' in query:
                c_port = 0
                cam = cv2.VideoCapture(c_port)
                result, image = cam.read()       
                cv2.imshow('photo', image)
                cv2.waitKey(5000)
                cam.release()
                cv2.destroyWindow("photo")
        elif 'edge' in query:
            if 'open' in query:
                AppOpener.open("msedge", match_closest=True)
                output('opening edge')
            elif 'close' in query:
                AppOpener.close("msedge", match_closest=True)
        elif 'telegram' in query:
            if 'open' in query:
                AppOpener.open("Telegram", match_closest=True)
            elif 'close' in query:
                AppOpener.close("Telegram", match_closest=True)
        elif 'whatsapp' in query:
            if 'open' in query:
                AppOpener.open("whatsapp", match_closest=True)
            elif 'close' in query:
                AppOpener.close("whatsapp", match_closest=True)
        
        elif 'brave' in query:
            if 'open' in query:
                AppOpener.open('brave')
            elif 'close' in query:
                AppOpener.close('brave')   
        elif "stop" in query or "exit" in query or "bye" in text:
            output("Ok Bye Sir")
            break
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"the time is {strTime}")   
        else:
            output("Could you please repeat again")
        
    