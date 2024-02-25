from translate import Translator
from virtual_assistant import desktop_assistant, user, speak, inputCommand

def perform_translation():
    print(desktop_assistant + ": What is the original language to be translated?")
    speak("What is the original language to be translated?")
    source = inputCommand()
    print(user + ": " + source)
    print(desktop_assistant + ": What is the target language for translation?")
    speak("What is the target language for translation?")
    target = inputCommand()
    print(user + ": " + target)
    speak("what should i translate for you")
    print("what should i translate for you")
    text = inputCommand()
    print(user + ": " + text)
    print(
        desktop_assistant + ": Sure! wait a while,let me translate the given text from " + source + " language to " + target + " language")
    speak("Sure! wait a while,let me translate the given text from " + source + " language to " + target + " language")
    translator = Translator(from_lang=source, to_lang=target)
    translation = translator.translate(text)
    print(
        desktop_assistant + ": The text that is translated from " + source + " language to " + target + " language is " + translation)
    speak("The text that is translated from " + source + " language to " + target + " language is " + translation)
