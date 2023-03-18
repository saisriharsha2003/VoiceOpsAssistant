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
    output("Hello {}! I am your personal desktop assistant".format(user))
    while 1:
        r = sr.Recognizer()
        text = inputCommand1().lower()
        print(text)
        if text == 0:
            continue
            
        elif 'chrome' in text or 'google' in text:
            if 'open' in text:
                AppOpener.open("google chrome", match_closest=True)
            elif 'close' in text:
                AppOpener.close("google chrome", match_closest=True)
            elif 'search' in text:
                search=inputCommand()
                driver = webdriver.Chrome("C:\\Users\\ranke\\Downloads\\chromedriver_win32\\chromedriver.exe")
                driver.maximize_window()
                driver.get("http://www.google.com")
                search_bar = driver.find_element(By.NAME, "q")
                search_bar.send_keys(search)
                search_bar.submit()
                time.sleep(3)
                first_result = driver.find_element(By.CSS_SELECTOR, "h3")
                first_result.click()
                time.sleep(3)
            elif 'close search' in text:
                driver.close()
                
        elif 'youtube' in text:
            if 'play' in text:
                output("which video or movie should i play for you sir?")
                video=inputCommand()
                pywhatkit.playonyt(video)
                
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
            
        elif 'vs code' in text or 'visual studio code' in text:
            if 'open' in text:
                AppOpener.open("visual studio code", match_closest=True)
            elif 'close' in text:
                AppOpener.close("visual studio code", match_closest=True)
                
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
            elif 'search' in text:
                search=inputCommand()
                edge_options = EdgeOptions()
                edge_options.use_chromium = True
                edge_options.add_argument("start-maximized")
                driver = Edge(executable_path="C:\\Users\\ranke\\Harsha\\webdrivers\\edgedriver_win64\\msedgedriver.exe")
                driver.get("https://www.bing.com")
                search_bar = driver.find_element(By.NAME, "q")
                search_bar.send_keys(search)
                search_bar.submit()
                time.sleep(3)
                first_result = driver.find_element(By.CSS_SELECTOR,"h2")
                first_result.click()
                time.sleep(10)
            elif 'close search' in text:
                driver.close()
                
        elif 'telegram' in text:
            if 'open' in text:
                AppOpener.open("Telegram", match_closest=True)
            elif 'close' in text:
                AppOpener.close("Telegram", match_closest=True)
         
        elif "stop" in text or "exit" in text or "bye" in text:
            output("Ok Bye Sir")
            break
            
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            output(f"the time is {strTime}")  
            
        else:
            output("Could you please repeat again")
        
    
