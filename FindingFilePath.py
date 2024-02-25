import os
from virtual_assistant import desktop_assistant, user, speak, inputCommand

def find_file_path():
    print(desktop_assistant + ": What is th file name?")
    speak("What is th file name?")
    file = inputCommand()
    print(user + ":" + file)
    print(desktop_assistant + ": What is the extension of the file")
    speak("What is the extension of the file")
    extension = inputCommand()
    print(user + ":" + extension)
    print(desktop_assistant + ": Sure! wait a while,let me fetch entire C disk for required file....")
    speak("Sure! wait a while,let me fetch entire C disk for required file....")
    file_name = file + '.' + extension
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            print(desktop_assistant + ": The " + file + " saved in the" + os.path.abspath(os.path.join(root, file_name)))
            speak("The " + file + " saved in the" + os.path.abspath(os.path.join(root, file_name)))
        else:
            print(desktop_assistant + ": The requested file is not currently on the system.")
            speak("The requested file is not currently on the system.")