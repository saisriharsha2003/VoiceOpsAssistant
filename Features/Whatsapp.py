import pywhatkit
import vobject
from CommonFunctions import desktop_assistant, inputCommand, speak, user

def send_whatsapp_message():
    print(desktop_assistant + ": For whom should i send the message?")
    speak("For whom should i send the message?")
    name = inputCommand()
    print(user + ": " + name)
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
    print(desktop_assistant + ": What message should i send to {}".format(name))
    speak("What message should i send to {}".format(name))
    message = inputCommand()
    print(user + ": " + message)
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    print(desktop_assistant + ": Message has been sent to " + name)
    speak("Message has been sent to " + name)