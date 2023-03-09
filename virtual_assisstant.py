import datetime
import pyttsx3
import speech_recognition as sr
import os
import webbrowser as wb
import AppOpener
import cv2
import pywhatkit
user = "harsha"
assistant = 'Jarvis'
assistant = pyttsx3.init()
assistant.setProperty('rate', 150)
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
        text = inputCommand().lower()
        print(text)
        if text == 0:
            continue
        elif 'chrome' in text or 'google' in text:
            if 'open' in text:
                AppOpener.open("google chrome", match_closest=True)
            elif 'close' in text:
                AppOpener.close("google chrome", match_closest=True)
            elif 'search' in text:
                output('what should i search for you')
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application %s"
                search1 = inputCommand().lower()
                wb.open_new_tab(search1)
        elif 'youtube' in text:
            if 'play' in text:
                v1=inputCommand().lower()
                v1.replace(' ','+')
                pywhatkit.playonyt(v1)

        elif 'vs code' in text or 'visual studio code' in text:
            if 'open' in text:
                AppOpener.open("visual studio code", match_closest=True)
            elif 'close' in text:
                AppOpener.close("visual studio code", match_closest=True)
        elif 'mail' in text:
            if 'open' in text:
                AppOpener.open('mail')
            elif 'close' in text:
                AppOpener.close('mail')
        elif 'vlc' in text:
            if 'open' in text:
                AppOpener.open('vlc media player')
            elif 'close' in text:
                AppOpener.close('vlc media player')
        elif 'camera' in text:
            if 'open' in text:
                AppOpener.open("camera", match_closest=True)
            elif 'close' in text:
                AppOpener.close("camera", match_closest=True)
            elif 'capture photo' in text:
                c_port = 0
                cam = cv2.VideoCapture(c_port)
                result, image = cam.read()       
                cv2.imshow('photo', image)
                cv2.waitKey(5000)
                cam.release()
                cv2.destroyWindow("photo")
        elif 'edge' in text:
            if 'open' in text:
                AppOpener.open("msedge", match_closest=True)
                output('opening edge')
            elif 'close' in text:
                AppOpener.close("msedge", match_closest=True)
        elif 'telegram' in text:
            if 'open' in text:
                AppOpener.open("Telegram", match_closest=True)
            elif 'close' in text:
                AppOpener.close("Telegram", match_closest=True)
        elif 'whatsapp' in text:
            if 'open' in text:
                AppOpener.open("whatsapp", match_closest=True)
            elif 'close' in text: 
                AppOpener.close("whatsapp", match_closest=True)
        
        elif 'brave' in text:
            if 'open' in text:
                AppOpener.open('brave')
            elif 'close' in text:
                AppOpener.close('brave')   
        elif "stop" in text or "exit" in text or "bye" in text:
            output("Ok Bye Sir")
            break
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"the time is {strTime}")   
        else:
            output("Could you please repeat again")
        
    