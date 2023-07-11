import datetime
import webbrowser as wb
import cv2
import speedtest
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


# TODO: alarm
# TODO: remember
# TODO: GUI
# TODO: make a call
# TODO: youtube controls.3
# TODO: play audio music
# TODO: location
# TODO: chrome-new tab,switch tab,switch window, close tab,close window
# TODO: temperature
# TODO: daily news
# TODO: wakeup function
# TODO: password authentication

def wish_and_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    g_t = time.split(':')
    hrs = int(g_t[0])
    if 5 <= hrs <= 12:
        output("Good Morning Sir!")
        print("Good Morning Sir!")
    elif 12 <= hrs <= 17:
        output("Good Afternoon Sir!")
        print("Good Afternoon Sir!")
    elif 17 <= hrs <= 21:
        output("Good Evening Sir!")
        print("Good Evening Sir!")
    else:
        print("Good Night Sir!")
        output("Good Night Sir!")

    current_time = datetime.datetime.now().strftime("%I:%M %p")
    output("It's " + current_time + " Sir!")
    print("It's " + current_time + " Sir!")


# chrome searching
def chrome_search():
    output("what should i search for you sir?")
    chrome_query = inputCommand()
    res = "searching" + chrome_query + " for you sir...."
    output(res)
    print(res)
    search_results = search(query, num_results=1)
    first_result = next(search_results, None)
    if first_result:
        wb.open(first_result)


def check_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6 
    upload_speed = st.upload() / 10**6  
    print(f"Download Speed is: {download_speed:.2f} Mbps")
    print(f"Upload Speed is: {upload_speed:.2f} Mbps")
    output(f"Download Speed is: {download_speed:.2f} Mbps")
    output(f"Upload Speed is: {upload_speed:.2f} Mbps")


def get_temperature_of_city():
    output("For which location you need its temperature Sir?")
    print("For which location you need its temperature Sir?")
    city = inputCommand()
    output("Sure Sir! Wait a While,let me check the temperature of current location.....")
    print("Sure Sir! Wait a While,let me check the temperature of current location.....")
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
        output(f"The temperature in {city} is {temperature}°C.")
        print(f"The temperature in {city} is {temperature}°C.")
    else:
        output("Error retrieving temperature data.")
        output("Response:", weather_data)
        print("Error retrieving temperature data.")
        print("Response:", weather_data)


# meaning og the word
def meaning_of_word(word):
    meaning_of_word = PyDictionary().meaning(word)
    pos_tag = list(meaning_of_word.keys())
    meanings = list(meaning_of_word.values())
    for i in range(len(meaning_of_word)):
        output("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))
        print("when the " + word + " is a " + pos_tag[i] + ",its meaning is " + str(meanings[i]))


# playing YouTube video
def play_video_in_youtube():
    output("which video or movie should i play for you sir?")
    video = inputCommand()
    output("Playing "+video+" in youtube Sir!")
    print("Playing "+video+" in youtube Sir!")
    pywhatkit.playonyt(video)


# taking screenshot
def screenshot():
    output("Hold the Screen for few seconds Sir.let me take the screenshot")
    print("Hold the Screen for few seconds Sir.let me take the screenshot")
    im = pyautogui.screenshot()
    im.save("screenshot.jpg")
    output("Screenshot successfully saved in current folder")
    print("Screenshot successfully saved in current folder")


# capturing photo
def capture_photo():
    output("Sure Sir! wait a while")
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    output("Smile Please")
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
    print("What message should i send to {}".format(name))
    message = inputCommand()
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    output("Message has been sent to "+name+" Sir!")
    print("Message has been sent to " + name + " Sir!")


# finding file path
def find_file_path():
    output("What is th file name?")
    print("What is th file name?")
    file = inputCommand()
    output("What is the extension of the file")
    print("What is the extension of the file")
    extension = inputCommand()
    output("Sure Sir! wait a while,let me fetch entire C disk for required file....")
    print("Sure Sir! wait a while,let me fetch entire C disk for required file....")
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
    print("what is the source language")
    source = inputCommand()
    output("what is the target language")
    print("what is the target language")
    target = inputCommand()
    output("what should i translate for you")
    print("what should i translate for you")
    text = inputCommand()
    output("Sure Sir! wait a while,let me translate the given text from "+source+" language to "+target+" language")
    print("Sure Sir! wait a while,let me translate the given text from " + source + " language to " + target + " language")
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
    print(target_email)
    msg = inputCommand()
    print(msg)
    output("Sure Sir! wait a while ,let me send the mail to "+target_email)
    print("Sure Sir! wait a while ,let me send the mail to " + target_email)
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
        elif 'network' in query and 'speed' in query:
            check_network_speed()
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
            get_temperature_of_city()
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"Now the time is {strTime}")
        else:
            output("Could you please repeat again")
