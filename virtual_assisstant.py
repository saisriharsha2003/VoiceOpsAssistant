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
            if 'open' in text:
                AppOpener.open("google chrome", match_closest=True)
            elif 'close' in text:
                AppOpener.close("google chrome", match_closest=True)
            elif 'search' in text:
                output("what should i search for you sir?")
                s2=inputCommand()
                driver = webdriver.Chrome("C:\\Users\\ranke\\Downloads\\chromedriver_win32\\chromedriver.exe")
                driver.maximize_window()
                driver.get("http://www.google.com")
                search_bar = driver.find_element(By.NAME, "q")
                search_bar.send_keys(s2)
                search_bar.submit()
                time.sleep(3)
                first_result = driver.find_element(By.CSS_SELECTOR, "h3")
                first_result.click()
                time.sleep(3)
            elif 'close search' in text:
                driver.close() 
        #linkedin automation        
        elif 'linkedin' in text:
            output("which linkedin profile should i search for you sir?")
            s=inputCommand()
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.linkedin.com")
            time.sleep(3)
            result = driver.find_element(By.NAME, "session_key")
            result.send_keys("saisriharsha.r@gmail.com")
            result1 = driver.find_element(By.NAME, "session_password")
            result1.send_keys("Harsha@05")
            result2 = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form[1]/div[2]/button")
            result2.click()
            time.sleep(5)
            s2 = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[1]/input")
            s2.send_keys(s)
            s2.send_keys(Keys.ENTER)
            driver.implicitly_wait(5)
            s3 = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/ul/li/div/a/div/div[1]/div[1]/div/div/span[1]/span/a/span/span[1]")
            s3.click()
            time.sleep(10)    
        #whatsapp automation
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
                output("which video or movie should i play for you sir?")
                video=inputCommand()
                pywhatkit.playonyt(video)  
        #opening visual studio code      
        elif 'vs code' in text or 'visual studio code' in text:
            if 'open' in text:
                AppOpener.open("visual studio code", match_closest=True)
            elif 'close' in text:
                AppOpener.close("visual studio code", match_closest=True)
        #capturing photo
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
        #searching and web browsing using edge using selenium     
        elif 'edge' in text:
            if 'open' in text:
                AppOpener.open("msedge", match_closest=True)
                output('opening edge')
            elif 'close' in text:
                AppOpener.close("msedge", match_closest=True)
            elif 'search' in text:
                s1 = text.split()
                s1.remove("search")
                s1.remove("in")
                s1.remove("edge")
                s2=" ".join(s1)
                edge_options = EdgeOptions()
                edge_options.use_chromium = True
                edge_options.add_argument("start-maximized")
                driver = Edge(executable_path="C:\\Users\\ranke\\Harsha\\webdrivers\\edgedriver_win64\\msedgedriver.exe")
                driver.get("https://www.bing.com")
                search_bar = driver.find_element(By.NAME, "q")
                search_bar.send_keys(s2)
                search_bar.submit()
                time.sleep(3)
                first_result = driver.find_element(By.CSS_SELECTOR,"h2")
                first_result.click()
                time.sleep(10)
            elif 'close search' in text:
                driver.close() 
        #opening telegram               
        elif 'telegram' in text:
            if 'open' in text:
                AppOpener.open("Telegram", match_closest=True)
            elif 'close' in text:
                AppOpener.close("Telegram", match_closest=True)
        #quiting virtual assisstant
        elif "stop" in text or "exit" in text or "bye" in text:
            output("Ok Bye Sir")
            break
        
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"the time is {strTime}")      
        else:
            output("Could you please repeat again")
        
    
