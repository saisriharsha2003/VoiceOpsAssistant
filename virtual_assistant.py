import datetime
import speech_recognition as sr
from Features.Wish import wish_and_time
from Features.Authentication import authenticate
from Features.Web_Browsing import chrome_search
from Features.Network_Speed import check_network_speed
from Features.TemperatureFinder import get_temperature_of_city
from Features.WordMeaning import meaning_of_the_word
from Features.EmailSender import send_mail
from Features.Translate import perform_translation
from Features.FindingFilePath import find_file_path
from Features.Whatsapp import send_whatsapp_message
from Features.CapturePhoto import capture_photo
from Features.Screenshot import screenshot
from Features.YoutubeVideo import play_video_in_youtube
from CommonFunctions import  inputCommand1, speak, user
from MLModel.BestIntent import finding_intents

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
