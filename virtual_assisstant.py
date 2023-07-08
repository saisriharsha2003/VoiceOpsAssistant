import datetime
import webbrowser as wb
import cv2
from config import owmapikey
import pyautogui
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import vobject
from PyDictionary import PyDictionary
from googlesearch import search
import os
from translate import Translator

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
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception as e:
                output("Sorry,I can't hear you!")

    return query


def inputCommand1():
    rec = sr.Recognizer()
    query1 = ""
    count = 0
    while count < 1:
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            output("How can i help you Sir?")
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                query1 = rec.recognize_google(audio, language="en-IN")
                count += 1
            except Exception as e:
                output("Sorry,I can't hear you!")

    return query1


# todo: alarm
# todo: youtube controls
# todo: interrnet speed
# todo: play audio music
# todo :date
# todo : location
# todo: chrome-new tab,switch tab,switch window, close tab,cloase window
# todo : temperature
# todo : daily news
# todo : wakeup function
# todo: passward authentication

def wish_and_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    g_t=time.split(':')
    hrs=int(g_t[0])
    mins=g_t[1]
    secs=g_t[2]
    if hrs>=5 and  hrs<=12:
        print("Good Morning Sir!")
        output("Good Morning Sir!")
    elif hrs>=12 and hrs<=17:
        print("Good Afternoon Sir!")
        output("Good Afternoon Sir!")
    elif hrs>=17 and hrs<=21:
        print("Good Evening Sir!")
        output("Good Evening Sir!")
    else:
        print("Good Night Sir!")
        output("Good Night Sir!")
    
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print("It's " + current_time + " Sir!")
    output("It's "+current_time+" Sir!")
        
        
# chrome searching
def chrome_search():
    output("what should i search for you sir?")
    chrome_query = inputCommand()
    res = "searching" + chrome_query + " for you sir...."
    print(res)
    output(res)
    search_results = search(query, num_results=1)
    first_result = next(search_results, None)
    if first_result:
        wb.open(first_result)


def get_temperature_of_city(city):
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
        return temperature
    else:
        print("Error retrieving temperature data.")
        print("Response:", weather_data)
        return None

    output(f"The temperature in {city} is {temperature}°C.")


# meaning og the word
def meaning_of_word(word):
    meaning_of_word = PyDictionary().meaning(word)
    pos_tag = list(meaning_of_word.keys())
    meanings = list(meaning_of_word.values())
    for i in range(len(meaning_of_word)):
        print("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))
        output("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))


# playing YouTube video
def play_video_in_youtube():
    output("which video or movie should i play for you sir?")
    video = inputCommand()
    pywhatkit.playonyt(video)


# taking screenshot
def screenshot():
    im = pyautogui.screenshot()
    im.save("screenshot.jpg")


# capturing photo
def capture_photo():
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    output("SMILE")
    pyautogui.press("enter")


# sending whatsapp message
def send_whatsapp_message():
    output("For whom should i send the message sir?")
    name = inputCommand()
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
    output("What message should i send to {}".format(name))
    message = inputCommand()
    pywhatkit.sendwhatmsg_instantly(phone_number, message)


# finding file path
def find_file_path():
    output("What is th file name?")
    file = inputCommand()
    output("What is the extension of the file")
    extension = inputCommand()
    file_name = file + '.' + extension
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            file_extension = os.path.splitext(file_name)[1]
            print(file_extension)
            return os.path.abspath(os.path.join(root, file_name))
    return None


# translating word or sentence
def perform_translation():
    output("what is the source language")
    source = inputCommand()
    output("what is the target language")
    target = inputCommand()
    output("what should i translate for you")
    text = inputCommand()
    translator = Translator(from_lang=source, to_lang=target)
    translation = translator.translate(text)
    print(translation)
    output(translation)


# sending_email
def send_mail():
    output("To whom should i send an email Sir?")
    target_email = inputCommand()
    print(target_email)
    output("Which msg should i send to" + target_email)
    msg = inputCommand()
    print(msg)
    pywhatkit.send_mail("rankelassh@gmail.com", "nwpmbjhunqhtjgdb", "Testing", msg, target_email)


if __name__ == '__main__':
    wish_and_time()
    while 1:
        r = sr.Recognizer()
        query = inputCommand1().lower()
        print(query)
        if query == 0:
            continue
        elif 'chrome' in query or 'google' in query:
            if 'search' in query:
                chrome_search()
        elif 'send' in query and 'whatsapp' in query:
            send_whatsapp_message()
        elif 'mail' in query:
            if 'send' in query:
                send_mail()
        elif 'youtube' in query:
            if 'play' in query:
                play_video_in_youtube()
        elif 'meaning' in query and 'word' in query:
            output("Which word do I need to explain the meaning of? Sir!")
            word = inputCommand()
            meaning_of_word(word)
        elif 'translate' in query:
            perform_translation()
        elif 'camera' in query:
            if 'capture a photo' in query:
                capture_photo()
        elif 'screenshot' in query:
            screenshot()
        elif "date" in query:
            c_date = str(datetime.date.today())
            output("Todays Date is " + c_date)
        elif 'search' in query and 'file' in query:
            find_file_path()
        elif "stop" in query or "exit" in query or "bye" in query:
            output("Ok Bye Sir")
            break
        elif 'meaning' in query:
            word = query.split()
            meaning_of_word(word[-1])
        elif 'temperature' in query:
            city = query.split()[-1]
            get_temperature_of_city(city)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"Now the time is {strTime}")
        else:
            output("Could you please repeat again")
