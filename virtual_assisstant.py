import datetime
import pyttsx3
import speech_recognition as sr
import os
import vobject
import pywhatkit
import webbrowser as wb
import AppOpener
import cv2
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
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
        rec.pause_threshold = 1
        
        # rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            query = rec.recognize_google(audio, language="en-IN")
        except Exception as e:
            output("Sorry,I can't hear you!")
    return query

def inputCommand1():
    rec = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        rec.pause_threshold = 5
        output("How can i help you Sir?")
        # rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            query = rec.recognize_google(audio, language="en-IN")
        except Exception as e:
            output("Sorry,I can't hear you!")
    return query

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
        

if __name__ == '__main__':
    output("Hello Sir! I am your personal desktop assistant")
    while 1:
        r = sr.Recognizer()
        text = inputCommand1().lower()
        print(text)
        if text == 0:
            continue   
        #chrome automation and web browsing         
        elif 'chrome' in text or 'google' in text:
            if 'search' in text:
                chrome_search()
        
        elif 'send' in text and 'whatsapp' in text:
            output("For whom should i send the message sir?")
            name=inputCommand()
            with open('all contacts .vcf') as f:
                vcards = vobject.readComponents(f.read())
            l=[]
            for vcard in vcards:
                if hasattr(vcard, 'fn') and vcard.fn.value.lower() == name.lower():
                    if hasattr(vcard, 'tel') and vcard.tel:
                        for p_no in vcard.contents['tel']:
                            ph_no = str(p_no.value)
                            l.append(ph_no)
            phone_number=l[0]
            if len(phone_number)<13:
                phone_number="+91"+phone_number
            output("What message should i send to {}".format(name))
            message=inputCommand()
            pywhatkit.sendwhatmsg_instantly(phone_number,message)    
        #email automation
        elif 'mail' in text:
            if 'open' in text:
                AppOpener.open("mail")
            elif 'send' in text:
                s1=text.split()
                s1.remove("send")
                s1.remove("mail")
                s1.remove("to")
                s3="".join(s1)
                msg=inputCommand()
                pywhatkit.send_mail("rankelassh@gmail.com","nwpmbjhunqhtjgdb","Testing",msg,s1)
        #youtube automation
        elif 'youtube' in text:
            if 'play' in text:
                play_video_in_youtube()
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
            elif 'close search' in text:
                driver.close() 
        elif "stop" in text or "exit" in text or "bye" in text:
            output("Ok Bye Sir")
            break
        
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"the time is {strTime}")      
        else:
            output("Could you please repeat again")
        
    
