import pywhatkit
from virtual_assistant import speak, desktop_assistant, user, inputCommand

def send_mail():
    print(desktop_assistant + ": Sir, To whom should I write an email?")
    speak("Sir, To whom should I write an email?")
    target_email = inputCommand()
    print(user + ": " + target_email)
    print(desktop_assistant + ": Sir, What message should I send to " + target_email)
    speak("Sir, What message should I send to " + target_email)
    msg = inputCommand()
    print(user + ": " + msg)
    print(desktop_assistant + ": Sure Sir! wait a while ,let me send the mail to " + target_email)
    speak("Sure Sir! wait a while ,let me send the mail to " + target_email)
    pywhatkit.send_mail("rankelassh@gmail.com", "nwpmbjhunqhtjgdb", "Testing", msg, target_email)
    print(desktop_assistant + ": Sir, The email was successfully delivered to the intended recipient.")
    speak("Sir, The email was successfully delivered to the intended recipient.")
