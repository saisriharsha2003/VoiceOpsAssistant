import pyttsx3
import speech_recognition as sr
desktop_assistant = "Jarvis"
user = "Harsha"

user = "Harsha"
desktop_assistant = 'Jarvis'
assistant = pyttsx3.init()
assistant.setProperty('rate', 150)
voices = assistant.getProperty("voices")
assistant.setProperty("voice", voices[0].id)


def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()


def inputCommand1():
    rec = sr.Recognizer()
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            print(desktop_assistant + ":How can i help you Sir?")
            speak("How can i help you Sir?")
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query1 = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception:
                print(desktop_assistant + ":Sorry,I can't hear you!")
                speak("Sorry,I can't hear you!")
        print(query1)
        query0 = query1.replace(" ","")
        if query1 == query0:
            print('True')
    return query0


print(inputCommand1())