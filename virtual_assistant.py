import datetime
import pyttsx3
from fuzzywuzzy import fuzz
import yaml
import speech_recognition as sr
from Wish import wish_and_time
from Authentication import authenticate
from Web_Browsing import chrome_search
from Network_Speed import check_network_speed
from TemperatureFinder import get_temperature_of_city
from WordMeaning import meaning_of_the_word
from EmailSender import send_mail
from Translate import perform_translation
from FindingFilePath import find_file_path
from Whatsapp import send_whatsapp_message
from CapturePhoto import capture_photo
from Screenshot import screenshot
from YoutubeVideo import play_video_in_youtube

user = "Harsha"
desktop_assistant = 'Jarvis'
assistant = pyttsx3.init()
assistant.setProperty('rate', 150)
voices = assistant.getProperty("voices")
assistant.setProperty("voice", voices[0].id)

def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()

def calculate_similarity(input_text, examples):
    return max(fuzz.ratio(input_text.lower(), example.lower()) for example in examples)

def finding_intents(user_input):
    with open("intents.yaml", "r") as yaml_file:
        intents_data = yaml.safe_load(yaml_file)
    best_intent = None
    max_similarity = 0
    for intent_data in intents_data["intents"]:
        intent_examples = intent_data["examples"].strip().split("\n")
        similarity = calculate_similarity(user_input, intent_examples)
        if similarity > max_similarity:
            max_similarity = similarity
            best_intent = intent_data["intent"]
    return best_intent

def inputCommand():
    rec = sr.Recognizer()
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 0.5
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query = rec.recognize_sphinx(audio, language="en-IN")
                count += 1
            except Exception:
                print(desktop_assistant + ": Sorry,I can't hear you!")
                speak("Sorry,I can't hear you!")
    return query


def inputCommand1():
    rec = sr.Recognizer()
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            print(desktop_assistant + ": How can i help you Sir?")
            speak("How can i help you Sir?")
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query1 = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception:
                print(desktop_assistant + ": Sorry,I can't hear you!")
                speak("Sorry,I can't hear you!")
    return query1


# TODO: searching chrome not working properly
# TODO: alarm
# TODO: add email address recognizer
# TODO: remember
# TODO: should add more intents to improve accuracy
# TODO: GUI
# TODO: download youtube video and play that video
# TODO: random password generator
# TODO: remember function
# TODO: make a call
# TODO: youtube controls.3
# TODO: play audio music
# TODO: location
# TODO: chrome-new tab,switch tab,switch window, close tab,close window
# TODO: temperature
# TODO: daily news
# TODO: wakeup function
# TODO: password authentication


if __name__ == '__main__':
    if authenticate():
        wish_and_time()
        while 1:
            r = sr.Recognizer()
            s_query = inputCommand1().lower()
            intent = finding_intents(s_query)
            print(user + ": " + s_query)
            print(intent)
            if s_query == 0:
                continue
            elif intent == 'search_chrome':
                chrome_search()
            elif intent == 'send_whatsapp_message':
                send_whatsapp_message()
            elif intent == 'send_email':
                send_mail()
            elif intent == 'play_youtube':
                play_video_in_youtube()
            elif intent == 'find_meaning':
                meaning_of_the_word()
            elif intent == 'translate':
                perform_translation()
            elif intent == 'check_network_speed':
                check_network_speed()
            elif intent == 'capture_photo':
                capture_photo()
            elif intent == 'take_screenshot':
                screenshot()
            elif intent == 'get_date':
                c_date = str(datetime.date.today())
                speak("Today's Date is " + c_date)
            elif intent == 'search_file':
                find_file_path()
            elif intent == 'get_temperature':
                get_temperature_of_city()
            elif intent == 'get_time':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Now the time is {strTime}")
            elif intent == 'stop_assistant':
                speak("Ok Bye Sir")
                break
            else:
                speak("Could you please repeat again")
