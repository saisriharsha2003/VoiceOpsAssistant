import datetime
import webbrowser as wb
import speedtest
from config import owmapikey
import pyautogui
import pyttsx3
from fuzzywuzzy import fuzz
import yaml
import pywhatkit
import requests
from config import authorized_password
import speech_recognition as sr
import vobject
from PyDictionary import PyDictionary
from googlesearch import search
import os
from translate import Translator

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
    with open("C:\\Users\\ranke\\Harsha\\Projects\\Desktop Assistant\\intents.yaml", "r") as yaml_file:
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
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception:
                print(desktop_assistant + ":Sorry,I can't hear you!")
                speak("Sorry,I can't hear you!")
    return query


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


def authenticate(max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        print(desktop_assistant + ": Whats the password?")
        speak("Whats the password?")
        password = inputCommand().replace(" ","")
        if password == authorized_password:
            print("Authentication successful. Starting the virtual assistant.")
            speak("Authentication successful. Starting the virtual assistant.")
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Incorrect password. {remaining_attempts} attempts remaining. Try again.")
                speak(f"Incorrect password. {remaining_attempts} attempts remaining. Try again.")
            else:
                print("Incorrect password. Maximum attempts reached. Exiting.")
                exit()


def wish_and_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    g_t = time.split(':')
    hrs = int(g_t[0])
    if 5 <= hrs <= 12:
        print(desktop_assistant + ":Good Morning Sir!")
        speak("Good Morning Sir!")
    elif 12 <= hrs <= 17:
        print(desktop_assistant + ":Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif 17 <= hrs <= 21:
        print(desktop_assistant + ":Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print(desktop_assistant + ":Good Night Sir!")
        speak("Good Night Sir!")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(desktop_assistant + ":It's " + current_time + " Sir!")
    speak("It's " + current_time + " Sir!")


# chrome searching
def chrome_search():
    print(desktop_assistant + ":what should i search for you sir?")
    speak("what should i search for you sir?")
    chrome_query = inputCommand()
    print(user + ":" + chrome_query)
    res = "searching" + chrome_query + " for you sir...."
    print(desktop_assistant + ":" + res)
    speak(res)
    search_results = search(chrome_query, num_results=1)
    first_result = next(search_results, None)
    if first_result:
        wb.open(first_result)


def check_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10 ** 6
    upload_speed = st.upload() / 10 ** 6
    print(desktop_assistant + f":Download Speed is: {download_speed:.2f} Mbps")
    print(desktop_assistant + f":Upload Speed is: {upload_speed:.2f} Mbps")
    speak(f"Download Speed is: {download_speed:.2f} Mbps")
    speak(f"Upload Speed is: {upload_speed:.2f} Mbps")


def get_temperature_of_city():
    print(desktop_assistant + ":For which location you need its temperature Sir?")
    speak("For which location you need its temperature Sir?")
    city = inputCommand()
    print(user + ":" + city)
    print(desktop_assistant + ":Sure Sir! Wait a While,let me check the temperature of given location.....")
    speak("Sure Sir! Wait a While,let me check the temperature of given location.....")
    api_key = owmapikey
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if "main" in weather_data and "temp" in weather_data["main"]:
        temperature = weather_data["main"]["temp"]
        print(desktop_assistant + f":The temperature in {city} is {temperature}°C.")
        speak(f"The temperature in {city} is {temperature}°C.")
    else:
        print(desktop_assistant + ":Error retrieving temperature data.")
        print(desktop_assistant + ":Response:", weather_data)
        speak("Error retrieving temperature data.")
        speak("Response:" + weather_data)


# meaning of the word
def meaning_of_the_word(word):
    meaning_of_word = PyDictionary().meaning(word)
    pos_tag = list(meaning_of_word.keys())
    meanings = list(meaning_of_word.values())
    for i in range(len(meaning_of_word)):
        print(desktop_assistant + ":when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))
        speak("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))


# playing YouTube video
def play_video_in_youtube():
    print(desktop_assistant + ":which video or movie should i play for you sir?")
    speak("which video or movie should i play for you sir?")
    video_name = inputCommand()
    print(user + ":" + video_name)
    print(desktop_assistant + ":Playing " + video_name + " in youtube!")
    speak("Playing " + video_name + " in youtube!")
    pywhatkit.playonyt(video_name)


# taking screenshot
def screenshot():
    print(desktop_assistant + ":Hold the Screen for few seconds.let me take the screenshot")
    speak("Hold the Screen for few seconds Sir.let me take the screenshot")
    im = pyautogui.screenshot()
    im.save("screenshot.jpg")
    print(desktop_assistant + ":Screenshot successfully saved in current folder")
    speak("Screenshot successfully saved in current folder")


# capturing photo
def capture_photo():
    print(desktop_assistant + ":Sure! wait a while")
    speak("Sure Sir! wait a while")
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    print(desktop_assistant + ":Smile Please")
    speak("Smile Please")
    pyautogui.press("enter")


# sending whatsapp message
def send_whatsapp_message():
    print(desktop_assistant + ":For whom should i send the message?")
    speak("For whom should i send the message?")
    name = inputCommand()
    print(user + ":" + name)
    with open('all contacts .vcf') as f:
        vcards = vobject.readComponents(f.read())
    l = []
    for vcard in vcards:
        if hasattr(vcard, 'fn') and vcard.fn.value.lower() == name.lower():
            if hasattr(vcard, 'tel') and vcard.tel:
                for p_no in vcard.contents['tel']:
                    ph_no = str(p_no.value)
                    l.append(ph_no)
    phone_number = l[0]
    if len(phone_number) < 13:
        phone_number = "+91" + phone_number
    print(desktop_assistant + ":What message should i send to {}".format(name))
    speak("What message should i send to {}".format(name))
    message = inputCommand()
    print(user + ":" + message)
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    print(desktop_assistant + ":Message has been sent to " + name)
    speak("Message has been sent to " + name)


# finding file path
def find_file_path():
    print(desktop_assistant + ":What is th file name?")
    speak("What is th file name?")
    file = inputCommand()
    print(user + ":" + file)
    print(desktop_assistant + ":What is the extension of the file")
    speak("What is the extension of the file")
    extension = inputCommand()
    print(user + ":" + extension)
    print(desktop_assistant + ":Sure! wait a while,let me fetch entire C disk for required file....")
    speak("Sure! wait a while,let me fetch entire C disk for required file....")
    file_name = file + '.' + extension
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            print(desktop_assistant + ":The " + file + " saved in the" + os.path.abspath(os.path.join(root, file_name)))
            speak("The " + file + " saved in the" + os.path.abspath(os.path.join(root, file_name)))
        else:
            print(desktop_assistant + ":The requested file is not currently on the system.")
            speak("The requested file is not currently on the system.")


# translating word or sentence
def perform_translation():
    print(desktop_assistant + ":What is the original language to be translated?")
    speak("What is the original language to be translated?")
    source = inputCommand()
    print(user + ":" + source)
    print(desktop_assistant + ":What is the target language for translation?")
    speak("What is the target language for translation?")
    target = inputCommand()
    print(user + ":" + target)
    speak("what should i translate for you")
    print("what should i translate for you")
    text = inputCommand()
    print(user + ":" + text)
    print(
        desktop_assistant + ":Sure! wait a while,let me translate the given text from " + source + " language to " + target + " language")
    speak("Sure! wait a while,let me translate the given text from " + source + " language to " + target + " language")
    translator = Translator(from_lang=source, to_lang=target)
    translation = translator.translate(text)
    print(
        desktop_assistant + ":The text that is translated from " + source + " language to " + target + " language is " + translation)
    speak("The text that is translated from " + source + " language to " + target + " language is " + translation)


# sending_email
def send_mail():
    print(desktop_assistant + ":Sir, To whom should I write an email?")
    speak("Sir, To whom should I write an email?")
    target_email = inputCommand()
    print(user + ":" + target_email)
    print(desktop_assistant + ":Sir, What message should I send to " + target_email)
    speak("Sir, What message should I send to " + target_email)
    msg = inputCommand()
    print(user + ":" + msg)
    print(desktop_assistant + ":Sure Sir! wait a while ,let me send the mail to " + target_email)
    speak("Sure Sir! wait a while ,let me send the mail to " + target_email)
    pywhatkit.send_mail("rankelassh@gmail.com", "nwpmbjhunqhtjgdb", "Testing", msg, target_email)
    print(desktop_assistant + ":Sir, The email was successfully delivered to the intended recipient.")
    speak("Sir, The email was successfully delivered to the intended recipient.")


if __name__ == '__main__':
    if authenticate():
        wish_and_time()
        while 1:
            r = sr.Recognizer()
            s_query = inputCommand1().lower()
            intent = finding_intents(s_query)
            print(user + ":" + s_query)
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
                print(desktop_assistant + ":Which word do I need to explain its meaning for?!")
                speak("Which word do I need to explain its meaning for?!")
                word = s_query.split()
                meaning_of_the_word(word[-1])
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



