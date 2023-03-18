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
                s1=text.split()
                s1.remove("search")
                s1.remove("in")
                s1.remove("chrome")
                s2=" ".join(s1)
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
        elif 'youtube' in text:
            if 'play' in text:
                output("which video or movie should i play for you sir?")
                video=inputCommand()
                pywhatkit.playonyt(video)

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
        
    
