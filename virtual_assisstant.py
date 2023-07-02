import datetime
import webbrowser as wb
import cv2
import pyttsx3
import pywhatkit
import speech_recognition as sr
import vobject
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
    with sr.Microphone() as source:
        rec.pause_threshold = 1
        output("How can i help you Sir?")
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            query1 = rec.recognize_google(audio, language="en-IN")
        except Exception as e:
            output("Sorry,I can't hear you!")
    return query1


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


# playing YouTube video
def play_video_in_youtube():
    output("which video or movie should i play for you sir?")
    video = inputCommand()
    pywhatkit.playonyt(video)


# capturing photo
def capture_photo():
    c_port = 0
    cam = cv2.VideoCapture(c_port)
    result, image = cam.read()
    cv2.imshow('photo', image)
    cv2.waitKey(5000)
    cam.release()
    cv2.destroyWindow("photo")


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
    output("Hello Sir! I am your personal desktop assistant")
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
        elif 'translate' in query:
            perform_translation()
        elif 'camera' in query:
            if 'capture a photo' in query:
                capture_photo()
        elif 'search' in query and 'file' in query:
            find_file_path()
        # quiting virtual assistant
        elif "stop" in query or "exit" in query or "bye" in query:
            output("Ok Bye Sir")
            break
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"Now the time is {strTime}")
        else:
            output("Could you please repeat again")
